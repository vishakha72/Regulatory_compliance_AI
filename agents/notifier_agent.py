def notify_agent(state):
    print("Running Notification & Reporting Agent")
    # Simulated report
    state["report"] = {
        "title": "RBI Circular Change Alert",
        "summary": state.get("summary", ""),
        "diff": state.get("diff", ""),
        "advisor_note": state.get("advisor_response", "")
    }
    return state