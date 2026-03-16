def calculate_score(repos, stack):
    
    score = 0

    repo_count = len(repos)

    score += min(repo_count * 2, 30)

    if "Python" in stack:
        score += 10

    if "JavaScript" in stack:
        score += 10

    if "Docker" in stack:
        score += 10

    if "React" in stack:
        score += 10

    if "C++" in stack:
        score += 10

    return min(score,100)