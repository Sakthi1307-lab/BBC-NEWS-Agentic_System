import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2",
)

INDEX_PATH ="data/bbc_index.json"
NUM_ARTICLES = 50
CHUNK_SIZE=800
CHUNK_OVERLAP =100

BBC_TOP_K = 4
WEB_MAX_RESULTS = 4
MIN_RELEVANT_DOCS = 2

