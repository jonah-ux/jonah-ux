"""Refusal regressions for the public review packet consistency gate."""

from __future__ import annotations

import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts import validate_review_packet as validator


class ReviewPacketTests(unittest.TestCase):
    def setUp(self) -> None:
        self.lock = json.loads(validator.LOCK_PATH.read_text(encoding="utf-8"))
        self.packet = validator.PACKET_PATH.read_text(encoding="utf-8")
        self.head = "a" * 40

    def report(self, lock=None, packet=None, expected_head=None):
        with (
            patch.object(
                validator,
                "_load",
                return_value=(
                    self.lock if lock is None else lock,
                    self.packet if packet is None else packet,
                ),
            ),
            patch.object(validator, "_git_head", return_value=self.head),
        ):
            return validator.validate(expected_head)

    def assert_blocked(self, report, code):
        self.assertEqual(report["result"], "blocked", report)
        self.assertIn(code, report["errors"])
        json.dumps(report)

    def test_checked_in_packet_passes(self):
        report = self.report()
        self.assertEqual(report["result"], "pass", report)
        self.assertEqual(report["owners"], 13)
        self.assertEqual(report["verified_artifacts"], 13)

    def test_lock_root_must_be_an_object(self):
        with patch.object(validator, "_load", return_value=([], self.packet)):
            self.assert_blocked(validator.validate(), "lock_not_object")

    def test_non_scalar_owner_identity_is_refused(self):
        self.lock["owners"][0]["repository"] = {"unexpected": "object"}
        self.lock["owners"][0]["source_head"] = [self.head]
        report = self.report()
        self.assert_blocked(report, "owner_repository_invalid:owner_0")
        self.assertIn("source_head_invalid:owner_0", report["errors"])

    def test_duplicate_owner_identities_are_refused(self):
        self.lock["owners"][1] = copy.deepcopy(self.lock["owners"][0])
        report = self.report()
        self.assert_blocked(report, "owner_repositories_not_unique")
        self.assertIn("owner_source_heads_not_unique", report["errors"])

    def test_repository_must_match_the_owner_id(self):
        self.lock["owners"][0]["owner"] = "another-owner"
        self.assert_blocked(
            self.report(), "owner_repository_mismatch:jonah-ux/forgeyard"
        )

    def test_swapped_packet_heads_are_refused_even_if_both_exist(self):
        first = self.lock["owners"][0]["source_head"]
        second = self.lock["owners"][1]["source_head"]
        packet = self.packet.replace(first, "TEMP").replace(second, first)
        packet = packet.replace("TEMP", second)
        report = self.report(packet=packet)
        self.assert_blocked(
            report, "source_head_does_not_match_packet:jonah-ux/forgeyard"
        )

    def test_snapshot_base_must_match_the_packet(self):
        self.lock["profile"]["snapshot_base_head"] = self.head
        self.assert_blocked(self.report(), "profile_snapshot_base_missing_from_packet")

    def test_wrong_published_head_remains_a_stable_refusal(self):
        self.assert_blocked(
            self.report(expected_head=self.head),
            "lock_published_head_does_not_match_expected_parent",
        )

    def test_verified_label_without_artifact_evidence_is_refused(self):
        self.lock["owners"][0]["artifact"] = {"state": "verified"}
        report = self.report()
        self.assert_blocked(report, "artifact_digest_invalid:jonah-ux/forgeyard")
        self.assertEqual(report["verified_artifacts"], 12)

    def test_artifact_digest_must_be_a_sha256(self):
        self.lock["owners"][0]["artifact"]["artifacts"][0]["sha256"] = "invalid"
        self.assert_blocked(self.report(), "artifact_digest_invalid:jonah-ux/forgeyard")

    def test_python_artifact_pair_cannot_be_two_wheels(self):
        artifact = self.lock["owners"][0]["artifact"]
        artifact["artifacts"][1]["name"] = "another-0.5.0-py3-none-any.whl"
        self.assert_blocked(self.report(), "artifact_set_invalid:jonah-ux/forgeyard")

    def test_artifact_names_cannot_contain_paths(self):
        artifact = self.lock["owners"][0]["artifact"]
        artifact["artifacts"][0]["name"] = "../fixture.whl"
        self.assert_blocked(self.report(), "artifact_set_invalid:jonah-ux/forgeyard")

    def test_failed_consumer_cannot_keep_a_verified_artifact(self):
        self.lock["owners"][0]["artifact"]["consumer_install"] = "failed"
        self.assert_blocked(
            self.report(), "artifact_consumer_not_verified:jonah-ux/forgeyard"
        )

    def test_slipstream_requires_digest_and_consumer_readback(self):
        owner = next(
            item for item in self.lock["owners"] if item["owner"] == "slipstream"
        )
        owner["artifact"]["artifact_sha256"] = None
        owner["artifact"]["consumer_self_test"] = "failed"
        report = self.report()
        self.assert_blocked(report, "artifact_digest_invalid:jonah-ux/slipstream")
        self.assertIn(
            "artifact_consumer_not_verified:jonah-ux/slipstream", report["errors"]
        )

    def test_missing_git_head_is_a_structured_refusal(self):
        with patch.object(
            validator, "_git_head", side_effect=ValueError("unavailable")
        ):
            report = validator.validate()
        self.assert_blocked(report, "current_git_head_unavailable")
        self.assertIsNone(report["source"]["revision"])

    def test_invalid_utf8_is_refused_without_a_private_path(self):
        with tempfile.TemporaryDirectory() as directory:
            lock_path = Path(directory) / "fixture.json"
            lock_path.write_bytes(b"\xff")
            with patch.object(validator, "LOCK_PATH", lock_path):
                report = validator.validate()
        self.assert_blocked(report, "load_failed:invalid_utf8")
        self.assertNotIn(directory, json.dumps(report))

    def test_duplicate_json_keys_are_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            lock_path = Path(directory) / "fixture.json"
            lock_path.write_text(
                '{"schema":"first","schema":"second"}', encoding="utf-8"
            )
            with patch.object(validator, "LOCK_PATH", lock_path):
                report = validator.validate()
        self.assert_blocked(report, "load_failed:duplicate_json_key")

    def test_oversized_input_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            lock_path = Path(directory) / "fixture.json"
            lock_path.write_bytes(b" " * (validator.MAX_INPUT_BYTES + 1))
            with patch.object(validator, "LOCK_PATH", lock_path):
                report = validator.validate()
        self.assert_blocked(report, "load_failed:input_too_large")

    def test_symlinked_input_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fixture.json"
            target.write_text(json.dumps(self.lock), encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            with patch.object(validator, "LOCK_PATH", link):
                report = validator.validate()
        self.assert_blocked(report, "load_failed:symlink_input")

    def test_symlinked_input_directory_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "source"
            target.mkdir()
            (target / "fixture.json").write_text(
                json.dumps(self.lock), encoding="utf-8"
            )
            link = Path(directory) / "projection"
            link.symlink_to(target, target_is_directory=True)
            with patch.object(validator, "LOCK_PATH", link / "fixture.json"):
                report = validator.validate()
        self.assert_blocked(report, "load_failed:symlink_input")

    def test_missing_input_is_refused_without_a_private_path(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(validator, "LOCK_PATH", Path(directory) / "absent.json"):
                report = validator.validate()
        self.assert_blocked(report, "load_failed:invalid_input")
        self.assertNotIn(directory, json.dumps(report))

    def test_invalid_profile_fields_are_not_echoed(self):
        self.lock["profile"]["snapshot_base_head"] = "/synthetic/private/path"
        self.lock["profile"]["extra"] = "synthetic-private-value"
        report = self.report()
        self.assert_blocked(report, "profile_snapshot_base_head_invalid")
        self.assertNotIn("/synthetic/private/path", json.dumps(report))
        self.assertNotIn("synthetic-private-value", json.dumps(report))

    def test_unknown_review_state_remains_explicit(self):
        self.lock["review_route"]["adoption"] = "invented"
        self.assert_blocked(self.report(), "adoption_state_changed")

    def test_cli_refusal_emits_json_and_exit_two(self):
        self.lock["owners"][0]["artifact"] = {"state": "verified"}
        stdout = io.StringIO()
        with (
            patch.object(validator, "_load", return_value=(self.lock, self.packet)),
            patch.object(validator, "_git_head", return_value=self.head),
            redirect_stdout(stdout),
        ):
            exit_code = validator.main(["--json"])
        self.assertEqual(exit_code, 2)
        self.assertEqual(json.loads(stdout.getvalue())["result"], "blocked")


if __name__ == "__main__":
    unittest.main()
