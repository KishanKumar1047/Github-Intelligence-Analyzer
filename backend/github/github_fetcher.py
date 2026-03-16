from github import Github

def fetch_repositories(username):

    g = Github()
    user = g.get_user(username)

    repos_data = []

    for repo in user.get_repos():

        repos_data.append({
            "name": repo.name,
            "description": repo.description,
            "language": repo.language,
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "url": repo.html_url
        })

    return repos_data
