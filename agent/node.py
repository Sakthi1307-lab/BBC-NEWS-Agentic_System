from agent import prompt
from agent.llm import get_llm
from agent.schema import Route, Grade
from agent.state import State
from agent.tools import search_bbc as search_bbc_tool, search_web_doc as search_web_doc_tool
from langchain_core.output_parsers import PydanticOutputParser

grade_parser = PydanticOutputParser(pydantic_object=Grade)


def router(state: State) -> dict:
    decision_result = get_llm().with_structured_output(Route).invoke(
        prompt.ROUTER.format(question=state.get("question", ""))
    )
    decision = Route.model_validate(decision_result)
    return {
        "router": decision.route,
        "steps": [f"router -> {decision.route}"],
    }
def grade(state:State)->dict:
    relevant = []
    for document in state.get("documents", []):
        response = get_llm().invoke(
            prompt.GRADE.format(
                question=state.get("question", ""),
                document=document,
            )
            + "\n\n"
            + grade_parser.get_format_instructions()
        )
        grade_result = grade_parser.parse(str(response.content))
        if grade_result.relevant:
            relevant.append(document)
    return {
            "documents": relevant,
            "steps": [f"grade -> {len(relevant)}"] + state.get("steps", []),
    }

def search_bbc(state: State) -> dict:
    docs = search_bbc_tool(state.get("question", ""))
    return {
            "documents": docs, 
            "steps": state.get("steps", []) + ["search_bbc"]
            }

def search_web_doc(state: State) -> dict:
    docs = search_web_doc_tool(state.get("question", ""))
    return {
            "documents": docs, 
            "steps": state.get("steps", []) + ["search_web_doc"]
            }

def generate(state: State) -> dict:
    answer = get_llm().invoke(prompt.ANSWER.format(
        sources="\n\n".join(state.get("documents", [])),
        question=state.get("question", ""))).content
    return {
            "answer": answer, 
            "steps": state.get("steps", []) + ["generate"]
            }