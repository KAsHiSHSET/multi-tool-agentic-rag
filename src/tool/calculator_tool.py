from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Example:
    25*16+40
    """

    print("\n========== CALCULATOR TOOL ==========")
    print(expression)

    try:
        result = eval(expression)

        return str(result)

    except Exception as e:
        return str(e)