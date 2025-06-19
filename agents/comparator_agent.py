# def compare_agent(state):
#     print("Running Document Comparison Agent")
#     from difflib import unified_diff
#     old_lines = state["documents"].get("old_doc", "").splitlines()
#     new_lines = state["documents"].get("new_doc", "").splitlines()
#     diff = list(unified_diff(old_lines, new_lines, lineterm=""))
#     state["diff"] = "\n".join(diff)
#     return state

from difflib import unified_diff
import textwrap

class DocumentComparator:
    def __init__(self):
        self.system_prompt = textwrap.dedent("""
            Compare document versions and highlight:
            - Added/removed sections
            - Modified clauses
            - Compliance implications
        """)

    async def compare(self, old_doc, new_doc):
        diff = unified_diff(
            old_doc.splitlines(), 
            new_doc.splitlines(),
            lineterm=''
        )
        return '\n'.join(diff)
