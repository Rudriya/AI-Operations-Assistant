import requests

GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"

def search_github(query: str):
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    response = requests.get(GITHUB_SEARCH_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()["items"][:5]

    return [
        {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "description": repo["description"]
        }
        for repo in data
    ]