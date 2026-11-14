import random
from pathlib import Path
from typing import Any, cast

from datasets import load_dataset
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

from agent import config
from agent.llm import get_embedding_model

def main():
    ds = load_dataset("SetFit/bbc-news",split = "train")
    articles = cast(
        list[dict[str, Any]],
        random.Random(42).sample(list(ds), config.NUM_ARTICLES),
    )

    docs = [
        Document(page_content=article["text"], metadata={"category": article["label_text"]})
        for article in articles]
    chunks = RecursiveCharacterTextSplitter(chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP).split_documents(docs)


    store =InMemoryVectorStore.from_documents(chunks, get_embedding_model())

    Path(config.INDEX_PATH).parent.mkdir(parents=True, exist_ok=True)
    store.dump(config.INDEX_PATH)

if __name__ == "__main__":
    main()
    