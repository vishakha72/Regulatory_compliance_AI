# # import requests
# # from bs4 import BeautifulSoup
# # from difflib import unified_diff
# # from openai import OpenAI
# # import json

# # openai_api_key = "api-key"

# # #crawler agent
# # def crawler_agent(url):
# #     response = requests.get(url)
# #     soup = BeautifulSoup(response.content, "html.parser")
# #     policy_links = [a['href'] for a in soup.find_all('a', href=True) if 'policy' in a['href'].lower()] #check for policy-word
# #     return policy_links

# from langgraph.graph import StateGraph

# from agents.crawler import crawler_agent
# from agents.compare import compare_agent
# from agents.summary import summary_agent
# from agents.advisor import advisor_agent
# from agents.notify import notify_agent

# # Supervisor function to decide which agents to run based on user input
# def supervisor_agent(state):
#     print("Running Supervisor Agent")
#     user_input = state.get("user_input", "")
#     selected_agents = []

#     if "crawl" in user_input.lower():
#         selected_agents.append("crawl")
#     if "compare" in user_input.lower():
#         selected_agents.append("compare")
#     if "summarize" in user_input.lower() or "summary" in user_input.lower():
#         selected_agents.append("summarize")
#     if "ask" in user_input.lower() or "advisor" in user_input.lower():
#         selected_agents.append("advisor")
#     if "report" in user_input.lower() or "notify" in user_input.lower():
#         selected_agents.append("notify")

#     state["selected_agents"] = selected_agents
#     return state

# # Define the shared state structure
# initial_state = {
#     "user_input": "crawl compare summarize advisor report"
# }

# # Build the LangGraph
# graph = StateGraph()

# # Add all nodes (agents)
# graph.add_node("supervisor", supervisor_agent)
# graph.add_node("crawl", crawler_agent)
# graph.add_node("compare", compare_agent)
# graph.add_node("summarize", summary_agent)
# graph.add_node("advisor", advisor_agent)
# graph.add_node("notify", notify_agent)

# # Define routing logic

# def route_after_supervisor(state):
#     next_steps = state.get("selected_agents", [])
#     return next_steps if next_steps else []

# # Add edges from supervisor to selected agents
# graph.add_conditional_edges("supervisor", route_after_supervisor)

# # Finish after all agent calls
# graph.set_entry_point("supervisor")
# graph.set_finish_condition(lambda state: True)

# # Run the graph
# if __name__ == "__main__":
#     result = graph.run(initial_state)
#     print("\nFinal State:")
#     for key, value in result.items():
#         print(f"{key}: {value}")

from agents import *

from agents.crawler_agent import PolicyCrawler
from agents.comparator_agent import DocumentComparator
from agents.impact_agent import ImpactAnalyzer
from agents.advisor_agent import advisor_agent
from agents.notifier_agent import notify_agent
from agents.superviser_agent import ComplianceSupervisor
# from agents import PolicyCrawler, DocumentComparator

async def main():
    crawler = PolicyCrawler()
    comparator = DocumentComparator()
    
    supervisor = ComplianceSupervisor([crawler, comparator])
    response = await supervisor.handle_request(
        "Check EU AI Act updates"
    )
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())





