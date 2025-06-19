# def summary_agent(state):
#     print("Running Summarization & Impact Agent")
#     # Simulated summary based on difference
#     diff = state.get("diff", "")
#     summary = "Summary: Detected key changes in RBI compliance policy. Action may be required for KYC norms."
#     state["summary"] = summary
#     return state

from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

impact_template = """Analyze policy changes and identify:
- Affected business units
- Required process changes
- Compliance deadlines
- Penalty risks

Changes: {changes}"""

class ImpactAnalyzer:
    def __init__(self):
        self.chain = LLMChain.from_string(
            llm="gpt-4",
            template=impact_template
        )
    
    async def analyze(self, changes):
        return await self.chain.ainvoke({"changes": changes})
