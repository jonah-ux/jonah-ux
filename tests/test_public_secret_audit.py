"""Regression checks for public credential discovery and historical Git-object scanning."""
import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.public_secret_audit import public_summary, scan_blob, scan_repository, select_repositories


class PublicSecretAuditTests(unittest.TestCase):
    def test_detects_provider_tokens_without_returning_the_secret(self):
        secret = "ghp_" + hashlib.sha256(b"synthetic-ghp-token").hexdigest()
        findings = scan_blob(("token = '" + secret + "'\n").encode(), "sample.py", "a" * 40)
        self.assertTrue(any(f["kind"] == "github_token" for f in findings))
        self.assertNotIn(secret, json.dumps(findings))

    def test_detects_high_entropy_oauth_refresh_token_assignment(self):
        secret = hashlib.sha256(b"synthetic-refresh-token").hexdigest()
        findings = scan_blob(("refresh_token = '" + secret + "'\n").encode(), "settings.json", "b" * 40)
        self.assertTrue(any(f["kind"] == "assigned_secret" for f in findings))
        self.assertNotIn(secret, json.dumps(findings))

    def test_does_not_flag_empty_env_values_or_placeholders(self):
        content = b"MYTHOPHONE_AI_API_KEY=\nrefresh_token = 'YOUR_REFRESH_TOKEN_GOES_HERE'\n"
        self.assertEqual(scan_blob(content, ".env.example", "a" * 40), [])

    def test_does_not_scan_forks_or_private_repositories(self):
        entries = [
            {"full_name": "jonah-ux/one", "private": False, "fork": False, "archived": False},
            {"full_name": "jonah-ux/fork", "private": False, "fork": True, "archived": False},
            {"full_name": "jonah-ux/hidden", "private": True, "fork": False, "archived": False},
            {"full_name": "jonah-ux/old", "private": False, "fork": False, "archived": True},
        ]
        self.assertEqual(select_repositories(entries), ["jonah-ux/one"])

    def test_public_ci_summary_never_discloses_finding_file_locations(self):
        report = {
            "owner": "jonah-ux", "repositories_scanned": 1, "blobs_scanned": 2,
            "skipped_large_blobs": 0, "errors": [],
            "findings": [{"repository": "jonah-ux/example", "path": "config/private-creds.json",
                          "line": 5, "blob": "a1b2c3d4e5f6", "kind": "github_token"}],
        }
        safe = public_summary(report)
        self.assertEqual(safe["finding_counts_by_category"], {"github_token": 1})
        self.assertEqual(safe["affected_repository_count"], 1)
        self.assertNotIn("config/private-creds.json", json.dumps(safe))
        self.assertNotIn("a1b2c3d4e5f6", json.dumps(safe))
        self.assertNotIn("jonah-ux/example", json.dumps(safe))

    def test_scans_deleted_secrets_in_earlier_git_commits(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "fixture"
            repo.mkdir()
            def git(*args):
                return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True)
            git("init", "-q")
            git("config", "user.name", "Synthetic Test")
            git("config", "user.email", "test@example.invalid")
            secret = "sk-proj-" + hashlib.sha256(b"historical-synthetic-credential").hexdigest()
            (repo / "config.py").write_text("API_KEY='" + secret + "'\n", encoding="utf-8")
            git("add", "config.py")
            git("commit", "-qm", "historical credential")
            (repo / "config.py").write_text("API_KEY=''\n", encoding="utf-8")
            git("add", "config.py")
            git("commit", "-qm", "remove credential")
            result = scan_repository("synthetic/fixture", repo)
            self.assertGreaterEqual(result["blobs_scanned"], 2)
            self.assertTrue(any(f["kind"] == "openai_key" for f in result["findings"]))
            self.assertNotIn(secret, json.dumps(result))


if __name__ == "__main__":
    unittest.main()
