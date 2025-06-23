A LLM-powered intelligent URL filter and ranker:

Takes a topic (e.g., “ofgem cyber security policy india”).

Uses DuckDuckGo to search the top relevant URLs.

Uses an LLM (via AutoGen + Ollama) to:

Judge if each URL is relevant to the topic.

Then optionally rank the relevant URLs to pick the most relevant one.


| Component        | What You Used                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------- |
| **Web Search**   | [`duckduckgo_search`] to get top URLs                 |
| **AI Framework** | [**AutoGen**]to define an `AssistantAgent` that can generate responses |
| **LLM Backend**  | [**Ollama**]a local LLM server                                                           |
| **LLM Model**    | `"mistral"` — a **7B open-weight model** good for reasoning and lightweight filtering                           |
