# # import os
# # import requests
# # from bs4 import BeautifulSoup
# # from autogen import AssistantAgent
# # from typing import List

# # # ===== PDF Downloader =====
# # def download_pdf(url: str, save_path: str):
# #     response = requests.get(url)
# #     with open(save_path, 'wb') as f:
# #         f.write(response.content)

# # # ===== Relevance Judger (LLM) =====
# # def get_llm_judgment(llm_agent: AssistantAgent, topic: str, title: str, link: str) -> str:
# #     prompt = f"""
# # You're helping filter documents about: "{topic}".

# # Here is a PDF title: {title}
# # Link: {link}

# # Is this document relevant to the topic? Reply with just "Yes" or "No" and 1-line reasoning.
# # """
# #     message = {"content": prompt, "role": "user"}
# #     response = llm_agent.generate_reply(messages=[message])
# #     return response["content"].strip()


# # # https://www.ofgem.gov.uk/energy-policy-and-regulation/compliance-and-enforcement
# # # https://www.ofgem.gov.uk/publications/riio-2-cyber-resilience-guidelines
# # # ===== Smart Crawler Agent =====
# # def smart_crawler(topic="cyber security policy", target_url="https://www.ofgem.gov.uk/publications/riio-2-cyber-resilience-guidelines", limit=5) -> List[str]:
# #     print(f"\n🌐 Crawling: {target_url}")
# #     response = requests.get(target_url)
# #     soup = BeautifulSoup(response.text, "html.parser")

# #     main_doc_section = soup.find(string="Main Document")
# #     pdf_links = []

# #     if main_doc_section:
# #         parent = main_doc_section.find_parent()
# #         if parent:
# #             pdf_tag = parent.find("a", href=True)
# #             if pdf_tag and pdf_tag['href'].endswith(".pdf"):
# #                 pdf_links.append(pdf_tag['href'])

# #     pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(".pdf")]
# #     pdf_links = pdf_links[:limit]

    

# #     # ---- Ollama LLM Config ----
# #     llm_config = {
# #         "model": "mistral",     # Use "llama3" or "phi3" if preferred
# #         "base_url": "http://localhost:11434",  # Default Ollama host
# #         "api_type": "ollama"
# #     }

# #     llm_agent = AssistantAgent(name="Ollama_RelevanceChecker", llm_config=llm_config)

# #     os.makedirs("docs/filtered_pdfs", exist_ok=True)
# #     saved_files = []

# #     for idx, link in enumerate(pdf_links):
# #         full_link = link if link.startswith("http") else f"{target_url.rstrip('/')}/{link.lstrip('/')}"
# #         title = full_link.split("/")[-1]

# #         print(f"\n🔍 Checking: {title}")
# #         verdict = get_llm_judgment(llm_agent, topic, title, full_link)
# #         print(f"🤖 Agent Decision: {verdict}")

# #         if "yes" in verdict.lower():
# #             save_path = f"docs/filtered_pdfs/doc_{idx+1}.pdf"
# #             download_pdf(full_link, save_path)
# #             saved_files.append(save_path)
# #             print(f"✅ Downloaded: {save_path}")
# #         else:
# #             print("❌ Skipped")

# #     return saved_files

# # # ===== MAIN CALL =====
# # if __name__ == "__main__":
# #     relevant_docs = smart_crawler(
# #         topic="cyber security policy",
# #         target_url="https://www.ofgem.gov.uk/publications/riio-2-cyber-resilience-guidelines",
# #         limit=5
# #     )

# #     print("\n🎯 Relevant PDFs saved:")
# #     for doc in relevant_docs:
# #         print("   →", os.path.abspath(doc))


# # # import os
# # # import requests
# # # import hashlib
# # # from bs4 import BeautifulSoup
# # # from autogen import AssistantAgent
# # # from typing import List

# # # def download_pdf(url: str, save_path: str):
# # #     response = requests.get(url)
# # #     with open(save_path, 'wb') as f:
# # #         f.write(response.content)

# # # def pdf_hash_from_url(url: str) -> str:
# # #     """Hash based on URL or its content to detect versioning."""
# # #     return hashlib.md5(url.encode()).hexdigest()

# # # def get_llm_judgment(llm_agent: AssistantAgent, topic: str, title: str, link: str) -> str:
# # #     prompt = f"""
# # # You're helping filter documents about: "{topic}".

# # # Here is a PDF title: {title}
# # # Link: {link}

# # # Is this document relevant to the topic? Reply with just "Yes" or "No" and 1-line reasoning.
# # # """
# # #     message = {"content": prompt, "role": "user"}
# # #     response = llm_agent.generate_reply(messages=[message])
# # #     return response["content"].strip()

# # # def smart_crawler(topic="cyber security policy", target_url="https://www.ofgem.gov.uk/publications/riio-2-cyber-resilience-guidelines", limit=5) -> List[str]:
# # #     print(f"\n🌐 Crawling: {target_url}")
# # #     response = requests.get(target_url)
# # #     soup = BeautifulSoup(response.text, "html.parser")

# # #     pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(".pdf")]
# # #     pdf_links = pdf_links[:limit]

# # #     llm_config = {
# # #         "model": "mistral",
# # #         "base_url": "http://localhost:11434",
# # #         "api_type": "ollama"
# # #     }
# # #     llm_agent = AssistantAgent(name="Ollama_RelevanceChecker", llm_config=llm_config)

# # #     os.makedirs("docs/old_pdfs", exist_ok=True)
# # #     os.makedirs("docs/new_pdfs", exist_ok=True)

# # #     saved_files = []

# # #     for idx, link in enumerate(pdf_links):
# # #         full_link = link if link.startswith("http") else f"{target_url.rstrip('/')}/{link.lstrip('/')}"
# # #         title = full_link.split("/")[-1]
# # #         pdf_hash = pdf_hash_from_url(full_link)
# # #         old_pdf_path = os.path.join("docs/old_pdfs", f"{pdf_hash}.pdf")
# # #         new_pdf_path = os.path.join("docs/new_pdfs", f"{pdf_hash}.pdf")

# # #         print(f"\n🔍 Checking: {title}")
# # #         verdict = get_llm_judgment(llm_agent, topic, title, full_link)
# # #         print(f"🤖 Agent Decision: {verdict}")

# # #         if "yes" in verdict.lower():
# # #             if os.path.exists(old_pdf_path):
# # #                 print(f"📁 Already exists (old): {old_pdf_path}")
# # #             else:
# # #                 # Save as new
# # #                 download_pdf(full_link, new_pdf_path)
# # #                 saved_files.append(new_pdf_path)
# # #                 print(f"🆕 Downloaded new: {new_pdf_path}")
# # #         else:
# # #             print("❌ Skipped (irrelevant)")

# # #     return saved_files

# # # if __name__ == "__main__":
# # #     relevant_docs = smart_crawler(
# # #         topic="cyber security policy",
# # #         target_url="https://www.ofgem.gov.uk/publications/riio-2-cyber-resilience-guidelines",
# # #         limit=5
# # #     )

# # #     print("\n🎯 Relevant PDFs saved:")
# # #     for doc in relevant_docs:
# # #         print("   →", os.path.abspath(doc))

# import os
# import requests
# from bs4 import BeautifulSoup
# from autogen import AssistantAgent
# from typing import List
# import duckduckgo_search  # pip install duckduckgo-search

# from duckduckgo_search import DDGS

# # ===== PDF Downloader =====
# def download_pdf(url: str, save_path: str):
#     response = requests.get(url)
#     with open(save_path, 'wb') as f:
#         f.write(response.content)

# # ===== Relevance Judger (LLM) =====
# def get_llm_judgment(llm_agent: AssistantAgent, topic: str, title: str, link: str) -> str:
#     prompt = f"""
# You're helping filter documents about: "{topic}".

# Here is a PDF title: {title}
# Link: {link}

# Is this document relevant to the topic? Reply with just "Yes" or "No" and 1-line reasoning.
# """
#     message = {"content": prompt, "role": "user"}
#     response = llm_agent.generate_reply(messages=[message])
#     return response["content"].strip()

# # ===== DuckDuckGo Search =====
# def get_top_urls(topic: str, max_results: int = 5) -> List[str]:
#     with DDGS() as ddgs:
#         results = ddgs.text(topic, max_results=max_results)
#         return [res["href"] for res in results if res["href"].startswith("http")]

# # ===== Crawl and Filter PDFs =====
# def crawl_and_filter(topic="cyber security policy", max_sites=5, pdf_limit=3) -> List[str]:
#     urls = get_top_urls(topic, max_results=max_sites)

#     print(f"\n🌐 Searching top URLs for topic: {topic}")
#     for u in urls:
#         print("→", u)

#     # Ollama LLM setup
#     llm_config = {
#         "model": "mistral",
#         "base_url": "http://localhost:11434",
#         "api_type": "ollama"
#     }
#     llm_agent = AssistantAgent(name="Ollama_RelevanceChecker", llm_config=llm_config)

#     os.makedirs("docs/filtered_pdfs", exist_ok=True)
#     saved_files = []

#     for site_url in urls:
#         print(f"\n🔎 Visiting: {site_url}")
#         try:
#             response = requests.get(site_url, timeout=10)
#             soup = BeautifulSoup(response.text, "html.parser")

#             pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(".pdf")]
#             pdf_links = pdf_links[:pdf_limit]

#             for idx, link in enumerate(pdf_links):
#                 full_link = link if link.startswith("http") else f"{site_url.rstrip('/')}/{link.lstrip('/')}"
#                 title = full_link.split("/")[-1]

#                 print(f"🧾 Checking: {title}")
#                 verdict = get_llm_judgment(llm_agent, topic, title, full_link)
#                 print(f"🤖 Verdict: {verdict}")

#                 if "yes" in verdict.lower():
#                     save_path = f"docs/filtered_pdfs/{title}"
#                     download_pdf(full_link, save_path)
#                     saved_files.append(save_path)
#                     print(f"✅ Downloaded: {save_path}")
#                 else:
#                     print("❌ Skipped")
#         except Exception as e:
#             print(f"⚠️ Failed to process {site_url}: {e}")

#     return saved_files

# # ===== MAIN CALL =====
# if __name__ == "__main__":
#     topic = "ofgem cyber security policy"
#     docs = crawl_and_filter(topic=topic, max_sites=5, pdf_limit=2)

#     print("\n🎯 Final Downloaded PDFs:")
#     for d in docs:
#         print(" →", os.path.abspath(d))


import requests
from duckduckgo_search import DDGS
from autogen import AssistantAgent
from typing import List


def get_top_urls(query: str, max_results: int = 10) -> List[str]:
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        return [res["href"] for res in results if res["href"].startswith("http")]


def get_llm_judgment(agent: AssistantAgent, topic: str, url: str) -> str:
    prompt = f"""
You're helping filter websites related to the topic: "{topic}"

Here is a URL: {url}

Is this website likely to contain official or highly relevant documents or information about the topic? 
Reply with just "Yes" or "No" and a 1-line reason.
"""
    message = {"content": prompt, "role": "user"}
    response = agent.generate_reply(messages=[message])
    return response["content"].strip()


def get_relevant_websites(topic: str, top_n: int = 10) -> List[str]:
    print(f"\n🔍 Searching for: {topic}")
    urls = get_top_urls(topic, max_results=top_n)

    llm_config = {
        "model": "mistral",
        "base_url": "http://localhost:11434",  # Ollama default
        "api_type": "ollama"
    }
    agent = AssistantAgent(name="Ollama_RelevanceJudge", llm_config=llm_config)

    relevant_urls = []
    for url in urls:
        print(f"\n🌐 Checking: {url}")
        verdict = get_llm_judgment(agent, topic, url)
        print(f"🤖 Verdict: {verdict}")
        if "yes" in verdict.lower():
            relevant_urls.append(url)

    return relevant_urls

if __name__ == "__main__":
    topic = "ofgem cyber security policy india"
    top_sites = get_relevant_websites(topic, top_n=5)

    print("\n🎯 Most Relevant Websites:")
    for site in top_sites:
        print("→", site)
