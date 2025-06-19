from langgraph.graph import StateGraph, END

class ComplianceSupervisor:
    def __init__(self, agents):
        self.workflow = StateGraph()
        
        # Add nodes for each agent
        for agent in agents:
            self.workflow.add_node(agent.name, agent.process)
            
        # Configure conditional edges
        self.workflow.add_conditional_edges(
            "crawler",
            lambda x: "comparator" if x.get("needs_comparison") else END
        )
        
        self.workflow.set_entry_point("crawler")

    async def handle_request(self, query):
        return await self.workflow.ainvoke({"input": query})
