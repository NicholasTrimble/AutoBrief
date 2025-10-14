# tests/test_simulate.py
import unittest
from simulate import generate

class TestSimulate(unittest.TestCase):
    def test_generate_structure(self):

        data = generate()
        # Top-level keys
        self.assertTrue(all(k in data for k in ["commits", "issues", "jira", "slack"]))

        # Commits
        for c in data["commits"]:
            self.assertIn("sha", c)
            self.assertIn("msg", c)
            self.assertIn("author", c)
            self.assertIn("date", c)

        # Issues
        for i in data["issues"]:
            self.assertIn("num", i)
            self.assertIn("title", i)
            self.assertIn("is_pr", i)
            self.assertIn("state", i)
            self.assertIn("author", i)

        # Jira
        for j in data["jira"]:
            self.assertIn("key", j)
            self.assertIn("summary", j)
            self.assertIn("status", j)

        # Slack
        for s in data["slack"]:
            self.assertIn("chan", s)
            self.assertIn("user", s)
            self.assertIn("text", s)
            self.assertIn("ts", s)

if __name__ == "__main__":
    unittest.main()
