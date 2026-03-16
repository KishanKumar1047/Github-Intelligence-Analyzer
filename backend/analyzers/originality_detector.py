def detect_originality(repo):
    
    commits = repo.get_commits().totalCount
    forks = repo.forks_count

    if commits < 3:
        return "Likely Tutorial"

    if forks > 50:
        return "Popular Template"

    return "Likely Original"