def analyze_commits(repo):
    
    commits = repo.get_commits()

    count = commits.totalCount

    if count < 5:
        activity = "Low"
    elif count < 20:
        activity = "Medium"
    else:
        activity = "High"

    return {
        "commit_count": count,
        "activity_level": activity
    }