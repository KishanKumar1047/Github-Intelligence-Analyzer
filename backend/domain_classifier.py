def classify_domains(repos):
    
    domains = {
        "AI/ML":0,
        "Backend":0,
        "Frontend":0,
        "DevOps":0,
        "Other":0
    }

    for repo in repos:

        desc = (repo["description"] or "").lower()
        name = repo["name"].lower()

        text = name + " " + desc

        if "ai" in text or "ml" in text or "chatbot" in text:
            domains["AI/ML"] += 1

        elif "api" in text or "backend" in text:
            domains["Backend"] += 1

        elif "react" in text or "frontend" in text or "website" in text:
            domains["Frontend"] += 1

        elif "docker" in text or "kubernetes" in text:
            domains["DevOps"] += 1

        else:
            domains["Other"] += 1

    return domains
