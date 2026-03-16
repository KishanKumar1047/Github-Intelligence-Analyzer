def generate_report(repos, stack, domains, jobs):
    
    report = {
        "total_repositories": len(repos),
        "tech_stack": stack,
        "domains": domains,
        "recommended_roles": jobs
    }

    return report
