# 🚀 GitHub Intelligence Analyzer

An AI-powered developer analytics tool that analyzes a GitHub profile to understand a developer’s **tech stack, project domains, portfolio strength, and potential job fit**.

The system fetches repository data from GitHub and generates a **developer intelligence report** that helps evaluate a developer's technical profile.

---

## 🌐 Live Demo

Frontend (Vercel):
https://github-intelligence-analyzer.vercel.app

Backend API (Render):
https://github-intelligence-analyzer.onrender.com

Example API request:

```
https://github-intelligence-analyzer.onrender.com/analyze/torvalds
```

---

## ✨ Features

### 🔍 GitHub Profile Analysis

* Fetches repositories using GitHub API
* Extracts repository metadata
* Identifies programming languages used

### 🧠 Tech Stack Detection

Detects developer technologies based on repositories.

Example output:

```
Python
JavaScript
C++
```

---

### 📊 Project Domain Classification

Projects are categorized into domains such as:

* AI / ML
* Backend Development
* Frontend Development
* DevOps
* Other

---

### 📈 Portfolio Strength Score

Generates a **portfolio score** based on:

* number of repositories
* diversity of technologies
* project complexity

Example:

```
Portfolio Score: 78 / 100
```

---

### ⚡ Fast API Backend

Built with **FastAPI** to provide a scalable API for analysis.

Example endpoint:

```
GET /analyze/{github_username}
```

---

### 🎨 Modern Frontend

Simple interface where users can:

1. Enter a GitHub username
2. Click analyze
3. View developer insights

---

## 🏗️ Architecture

```
Frontend (Vercel)
      ↓
API Requests
      ↓
Backend (FastAPI on Render)
      ↓
GitHub API
      ↓
Analysis Engine
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* PyGithub
* Requests

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* Render (Backend)
* Vercel (Frontend)

---

## 📂 Project Structure

```
github-intelligence-analyzer
│
├── backend
│   ├── main.py
│
│   ├── github
│   │   └── github_fetcher.py
│
│   ├── analyzers
│   │   ├── tech_stack.py
│   │   ├── domain_classifier.py
│   │   ├── commit_analyzer.py
│   │   ├── complexity_analyzer.py
│   │   └── originality_detector.py
│
│   ├── scoring
│   │   └── portfolio_score.py
│
│   └── report
│       └── report_generator.py
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

Open the existing project folder:

```
cd C:\Users\kishan\Desktop\projects\Github-Intelligence-Analyzer-main\Github-Intelligence-Analyzer-main
```

Create and activate a virtual environment:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 2️⃣ Install dependencies

```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

### 3️⃣ Run backend server

```
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

API will run at:

```
http://127.0.0.1:8000
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

Example API request:

```
http://127.0.0.1:8000/analyze/torvalds
```

---

### 4️⃣ Run frontend

Open a second PowerShell terminal in the same project folder and run:

```
python -m http.server 5500 -d frontend
```

Then open:

```
http://127.0.0.1:5500
```

in your browser.

The frontend is configured to call the local backend at:

```
http://127.0.0.1:8000
```

---

## 📡 API Example

Request:

```
GET /analyze/{username}
```

Example:

```
/analyze/torvalds
```

Response:

```json
{
  "total_repositories": 20,
  "languages": {
    "Python": 8,
    "C": 5
  },
  "domains": {
    "AI/ML": 3,
    "Backend": 5
  },
  "portfolio_score": 84
}
```

---

## 📈 Future Improvements

Planned upgrades:

* AI project summarization
* repository code quality analysis
* developer skill radar chart
* GitHub contribution analysis
* resume generation from GitHub
* developer comparison tool

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Kishan Kumar

GitHub:
https://github.com/kishankumar1047

---

⭐ If you like this project, consider giving it a star!
