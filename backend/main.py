from fastapi import FastAPI

from backend.github.github_fetcher import fetch_repositories
from backend.analyzers.tech_stack import detect_tech_stack
from backend.analyzers.domain_classifier import classify_domains
from backend.analyzers.commit_analyzer import analyze_commits
from backend.analyzers.complexity_analyzer import estimate_complexity
from backend.analyzers.originality_detector import detect_originality
from backend.scoring.portfolio_score import calculate_score
from backend.report.report_generator import generate_report


app = FastAPI()


@app.get("/analyze/{username}")
def analyze(username: str):

    repos = fetch_repositories(username)

    stack = detect_tech_stack(repos)

    domains = classify_domains(repos)

    score = calculate_score(repos, stack)

    report = generate_report(repos, stack, domains, [], score)

    return report