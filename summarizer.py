# autobrief/summarizer.py

def summarize(lines):
    """
    Produce a simple text summary based on keywords.
    This is deterministic and explainable for interviews.
    """
    text = " ".join(lines).lower()
    completed = []

    if "merged" in text or "merged pr" in text:
        completed.append("Merged recent pull requests.")
    if "fix(" in text or "fix " in text:
        completed.append("Applied bug fixes.")
    if "tests" in text or "ci" in text:
        completed.append("Added/updated tests or CI.")
    if not completed:
        completed.append("No explicit completions found.")

    blockers = ["No major blockers reported." if "failing" not in text else "CI/tests failing; investigation ongoing."]
    next_steps = ["Complete PR reviews.", "Run integration tests and deploy to staging."]

    out = "Status: Active development with commits and PR activity.\n\n"
    out += "Completed:\n" + "\n".join(f"- {c}" for c in completed) + "\n\n"
    out += "Blockers:\n" + "\n".join(f"- {b}" for b in blockers) + "\n\n"
    out += "Next steps:\n" + "\n".join(f"- {n}" for n in next_steps)

    return out
