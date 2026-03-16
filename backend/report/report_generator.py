def generate_report(repos, stack, domains, jobs, score):
    
    report = {

        "total_repositories": len(repos),

        "tech_stack": stack,

        "domains": domains,

        "recommended_roles": jobs,

        "portfolio_score": score
    }

    return report