

import os
import requests

from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


@tool
def github_repository(repo: str) -> str:
    """
    Fetch information about a GitHub repository.

    Input format:
    owner/repository

    Example:
    langchain-ai/langgraph
    """

    print("\n========== GITHUB TOOL ==========")
    print(repo)

    url = f"https://api.github.com/repos/{repo}"

    response = requests.get(
        url,
        headers=HEADERS
    )

    if response.status_code != 200:
        return "Repository not found."

    data = response.json()

    return f"""
Repository : {data['full_name']}

Description : {data['description']}

Language : {data['language']}

Stars : {data['stargazers_count']}

Forks : {data['forks_count']}

Open Issues : {data['open_issues_count']}

Default Branch : {data['default_branch']}

Repository URL :
{data['html_url']}
"""