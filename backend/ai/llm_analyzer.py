import ollama

def analyze_repo_ai(readme):

    prompt = f"""
    Analyze this GitHub project description.

    Identify:
    - project purpose
    - tech stack
    - domain
    - difficulty level

    README:
    {readme}
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]