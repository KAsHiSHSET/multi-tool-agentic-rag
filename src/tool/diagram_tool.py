from langchain_core.tools import tool

from src.config.config import Config

llm = Config.get_llm()


@tool
def diagram_generator(prompt: str) -> str:
    """
    Generate Mermaid diagrams.

    Use whenever the user asks for

    - architecture
    - flowchart
    - sequence diagram
    - ER diagram
    - class diagram
    - UML
    """

    response = llm.invoke(
        f"""
You are a software architect.

Generate ONLY Mermaid code.

Do not explain.

Request:

{prompt}
"""
    )

    diagram = response.content

    diagram = diagram.replace("```mermaid", "")

    diagram = diagram.replace("```", "")

    return diagram.strip()