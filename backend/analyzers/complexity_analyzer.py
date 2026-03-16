def estimate_complexity(repo):
    
    size = repo.size

    if size < 500:
        level = "Simple"
    elif size < 2000:
        level = "Medium"
    else:
        level = "Advanced"

    return {
        "repo_size": size,
        "complexity": level
    }