# autobrief/collector.py
from datetime import datetime

def normalize(sim):
    """
    Convert simulated data into readable one-line updates.
    sim = dict returned by simulate.generate()
    """
    lines = []
    lines.append(f"[COLLECTED_AT {datetime.utcnow().isoformat()}] Repository: demo/repo")

    # Commits
    for c in sim["commits"]:
        line = f"GitHub Commit {c['sha']}: \"{c['msg']}\" (author: {c['author']}, date: {c['date']})"
        lines.append(line)

    # Issues / PRs
    for it in sim["issues"]:
        kind = "PR" if it["is_pr"] else "Issue"
        line = f"GitHub {kind} #{it['num']}: \"{it['title']}\" (state: {it['state']}, author: {it['author']})"
        lines.append(line)

    # Jira
    for j in sim["jira"]:
        line = f"Jira {j['key']}: \"{j['summary']}\" (status: {j['status']})"
        lines.append(line)

    # Slack
    for s in sim["slack"]:
        line = f"Slack {s['chan']} [{s['ts']}] {s['user']}: {s['text']}"
        lines.append(line)

    return lines
