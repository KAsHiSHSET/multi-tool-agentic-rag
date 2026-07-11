from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()


@tool
def web_search(query: str) -> str:
    """
    Search the web using DuckDuckGo.

    Use this tool whenever the answer is not likely to be found
    in the uploaded documents.
    """

    return search.run(query)