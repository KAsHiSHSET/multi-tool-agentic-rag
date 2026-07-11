import io
import contextlib

from langchain_core.tools import tool

from src.config.config import Config


llm = Config.get_llm()


@tool
def python_executor(task: str) -> str:
    """
    Generate Python code, execute it,
    and return both code and output.
    """

    prompt = f"""
You are an expert Python programmer.

Write ONLY executable Python code.

Do NOT explain anything.

Task:
{task}
"""

    code = llm.invoke(prompt).content

    # Remove markdown
    code = (
        code.replace("```python", "")
            .replace("```", "")
            .strip()
    )

    stdout = io.StringIO()

    try:

        with contextlib.redirect_stdout(stdout):

            exec(code, {})

        output = stdout.getvalue()

    except Exception as e:

        output = str(e)

    return f"""
Generated Python Code

{code}

-------------------------

Execution Output

{output}
"""