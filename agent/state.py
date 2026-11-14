from typing import TypedDict


class State(TypedDict, total=False):
    question:str
    router :str
    documents :list[str]
    answer: str
    steps: list[str]
