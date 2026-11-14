from functools import lru_cache
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from agent import config

@lru_cache(maxsize=1)
def get_llm():
    return ChatGroq(model=config.LLM_MODEL, temperature=0.0)

@lru_cache(maxsize=1)
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)