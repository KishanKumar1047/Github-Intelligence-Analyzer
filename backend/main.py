from fastapi import FastAPI
from github.github_fetcher import fetch_repositories
from analyzers.tech_stack import detect_tech_stack
from analyzers.domain_classifier import classify_domains
from analyzers.commit_analyzer import analyze_commits
from analyzers.complexity_analyzer import estimate_complexity
from analyzers.originality_detector import detect_originality
from scoring.portfolio_score import calculate_score
from report.report_generator import generate_report

app = FastAPI()

@app.get("/analyze/{username}")

def analyze(username:str):

    repos = fetch_repositories(username)

    stack = detect_tech_stack(repos)

    domains = classify_domains(repos)

    score = calculate_score(repos, stack)

    report = generate_report(repos, stack, domains, [], score)

    return report