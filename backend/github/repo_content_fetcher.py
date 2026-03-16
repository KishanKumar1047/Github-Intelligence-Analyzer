import requests

def fetch_readme(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    headers = {"Accept": "application/vnd.github.v3.raw"}

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return res.text[:2000]

    return ""