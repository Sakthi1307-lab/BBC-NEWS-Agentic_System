from functools import lru_cache

from langchain_core.vectorstores import InMemoryVectorStore
from tavily import TavilyClient

from agent import config
from agent.llm import get_embedding_model

@lru_cache(maxsize=1)
def bbc_store():
    return InMemoryVectorStore.load(config.INDEX_PATH, get_embedding_model())

@lru_cache(maxsize=1)
def tavily():
    return TavilyClient(api_key=config.TAVILY_API_KEY)

def search_bbc(query:str, top_k:int=config.BBC_TOP_K) ->list[str]:
    result =bbc_store().similarity_search(query, top_k=top_k)
    return [f"[BBC archive] {d.page_content}" for d in result]

def search_web_doc(query:str, top_k:int=config.WEB_MAX_RESULTS) ->list[str]:
    result = tavily().search(query, top_k=top_k)
    return [
        f"[web search] {item['url']} {item['content']}"
        for item in result.get("results", [])
    ]