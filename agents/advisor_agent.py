def advisor_agent(state):
    print("Running Interactive Compliance Advisor Agent")
    user_query = state.get("user_input", "")
    # Simulate a Q&A response
    if "KYC" in user_query:
        answer = "Yes, the new policy affects KYC periodic update cycles."
    else:
        answer = "No relevant changes detected for the specified query."
    state["advisor_response"] = answer
    return state