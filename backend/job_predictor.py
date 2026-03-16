def predict_jobs(stack):
    
    jobs = []

    if "Python" in stack:
        jobs.append("Backend Developer")

    if "JavaScript" in stack:
        jobs.append("Full Stack Developer")

    if "Python" in stack and "Jupyter Notebook" in stack:
        jobs.append("AI / ML Engineer")

    if "Docker" in stack:
        jobs.append("DevOps Engineer")

    return jobs
