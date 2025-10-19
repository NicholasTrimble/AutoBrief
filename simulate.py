import random
from utils import iso, short_sha

# Sample users
USERS = ["alicej", "bobchen", "devonp"]

def generate():
    """
    Return a dictionary with simulated commits, issues, Jira tasks, and Slack messages.
    Everything is in memory; no real APIs.
    """

    # -----------------------
    # GitHub commits
    # -----------------------
    commit_messages = [
        "fix(auth): null token",
        "feat(profile): avatars",
        "docs: update README"
    ]
    commits = []
    for msg in commit_messages:
        commit = {}
        commit["sha"] = short_sha()
        commit["msg"] = msg
        commit["author"] = random.choice(USERS)
        commit["date"] = iso(days=random.randint(0, 10))
        commits.append(commit)

    # -----------------------
    # GitHub issues / PRs
    # -----------------------
    issue_titles = ["Improve logging", "Refactor API", "Add CI linter", "Fix header"]
    issues = []
    for i, t in enumerate(issue_titles):
        issue = {}
        issue["num"] = i + 1
        issue["title"] = t
        issue["is_pr"] = (i % 2 == 0)  # every other is a PR
        issue["state"] = random.choice(["open", "closed"])
        issue["author"] = random.choice(USERS)
        issues.append(issue)

    # -----------------------
    # Jira tasks
    # -----------------------
    jira_summaries = ["Login redirect", "Auth tests", "Deploy doc"]
    jira = []
    for i, s in enumerate(jira_summaries):
        task = {}
        task["key"] = f"PROJ-{10+i}"
        task["summary"] = s
        task["status"] = random.choice(["To Do", "In Progress", "Done"])
        jira.append(task)

    # -----------------------
    # Slack messages
    # -----------------------
    slack_texts = ["pushed commit", "merged PR #2", "CI failing", "deploy scheduled"]
    slack = []
    for t in slack_texts:
        msg = {}
        msg["chan"] = "#dev"
        msg["user"] = random.choice(USERS)
        msg["text"] = t
        msg["ts"] = iso(days=random.randint(0, 5))
        slack.append(msg)

    # Return everything together
    return {
        "commits": commits,
        "issues": issues,
        "jira": jira,
        "slack": slack
    }
