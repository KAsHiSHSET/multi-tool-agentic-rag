from langchain_core.tools import tool
import arxiv


@tool
def arxiv_search(query: str) -> str:
    """
    Search research papers from ArXiv.

    Use this whenever the user asks for:
    - research papers
    - AI papers
    - ML papers
    - LLM papers
    - surveys
    """

    search = arxiv.Search(
        query=query,
        max_results=3,
        sort_by=arxiv.SortCriterion.Relevance
    )

    client = arxiv.Client()

    papers = []

    for paper in client.results(search):

        papers.append(
            f"""
Title: {paper.title}

Authors: {", ".join(author.name for author in paper.authors)}

Published: {paper.published.date()}

Summary:
{paper.summary}

PDF:
{paper.pdf_url}
"""
        )

    if len(papers) == 0:
        return "No papers found."

    return "\n\n--------------------------\n\n".join(papers)