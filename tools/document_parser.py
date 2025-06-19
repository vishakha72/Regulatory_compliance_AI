# utils/document_parser.py
from langchain_community.document_loaders import WebBaseLoader

class PolicyParser:
    def __init__(self):
        self.loader = WebBaseLoader()
        
    async def parse(self, url):
        return await self.loader.aload(url)
