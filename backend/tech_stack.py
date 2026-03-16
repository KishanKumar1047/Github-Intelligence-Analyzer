def detect_tech_stack(repos):
    
    stack = {}

    for repo in repos:
        lang = repo["language"]

        if lang:
            stack[lang] = stack.get(lang, 0) + 1

    return stack
