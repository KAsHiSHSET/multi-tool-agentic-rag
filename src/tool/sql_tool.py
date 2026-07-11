from langchain_core.tools import tool
from langchain_groq import ChatGroq
from src.config.config import Config


llm = Config.get_llm()


@tool
def sql_generator(task: str) -> str:
    """
    Generate SQL queries.

    Use this tool whenever the user asks for:

    - SQL
    - MySQL
    - PostgreSQL
    - SQLite
    - Database queries
    - Joins
    - GROUP BY
    - Window Functions
    - CTE
    """

    prompt = f"""
You are an expert SQL Engineer.

Generate ONLY SQL.

Rules:

- Return clean SQL.
- Add comments where necessary.
- Use ANSI SQL.
- Explain the query briefly.

User Request:

{task}
"""

    response = llm.invoke(prompt)

    return response.content

