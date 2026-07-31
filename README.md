# 🤖 WEAVE-AI

<div align="center">

## 🚀 Your AI-Powered Career Assistant

**An intelligent career assistant that helps users analyze resumes, search jobs, match resumes with job descriptions, research companies, and receive AI-powered career guidance.**

Developed as part of the **Capabl AI Agent Internship (Track A)**.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-red?style=for-the-badge&logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google)
![LangChain](https://img.shields.io/badge/LangChain-AI-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)

</div>

---

# 📖 Overview

WEAVE-AI is an AI-powered career assistant designed to simplify the job search process while helping users improve their resumes and career readiness.

The application combines **Google Gemini**, **LangChain**, **RAG (Retrieval-Augmented Generation)**, **SQLite**, and **ChromaDB** to provide intelligent career assistance through a clean Streamlit interface.

---

# ✨ Key Features

## 📄 Resume Analyzer

- Upload PDF or DOCX resumes
- AI-powered resume analysis
- ATS-style feedback
- Resume strengths & weaknesses
- Skill improvement suggestions
- Resume report download (PDF)

---

## 🎯 Resume Match Engine

Compare your resume with any job opening and receive:

- Resume Match Score
- Matching Skills
- Missing Skills
- Personalized Suggestions
- Final Recommendation
- Download Match Report as PDF

---

## 💼 Smart Job Search

- Unified Job Search
- Search remote jobs
- Save favourite jobs
- Multiple job API integration
- SQLite-based saved jobs

---

## 🏢 Company Research

Research any company using AI.

Provides:

- Company Overview
- Required Skills
- Career Opportunities
- Interview Tips
- Industry Insights

---

## 🤖 AI Career Assistant

Ask career-related questions including:

- Resume improvement
- Career guidance
- Learning roadmap
- Interview preparation
- Skill recommendations

---

## 📚 Knowledge Base (RAG)

- Upload PDF Documents
- Upload DOCX Documents
- Automatic Document Processing
- Text Chunking
- ChromaDB Vector Database
- Semantic Search
- AI Knowledge Retrieval

---

# 🚀 Project Highlights

- Google Gemini Integration
- Resume Parsing
- Resume Analyzer
- Resume vs Job Matching
- Company Research
- AI Career Chat
- Retrieval-Augmented Generation (RAG)
- SQLite Database
- ChromaDB Vector Store
- PDF Report Generation
- Modular Architecture

---

# 🏗 System Architecture

```text
                    User
                      │
                      ▼
             Streamlit Web App
                      │
        ┌─────────────┼──────────────┐
        ▼             ▼              ▼
 Resume Analyzer  Job Search   Company Research
        │             │              │
        └─────────────┼──────────────┘
                      ▼
               Gemini AI Service
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
     RAG Engine               SQLite Database
        │
        ▼
   ChromaDB Vector Store
```

---

# 📂 Project Structure

```text
WEAVE-AI/
│
├── assets/
├── components/
├── config/
├── database/
├── docs/
├── models/
├── pages/
├── services/
├── tools/
├── utils/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini 3.5 Flash |
| AI Framework | LangChain |
| Vector Database | ChromaDB |
| Database | SQLite |
| PDF Reports | ReportLab |
| Resume Parsing | PyPDF2, python-docx |
| API Integration | Requests |
| Version Control | Git & GitHub |

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Shubhh1415/WEAVE-AI.git
```

Move into the project

```bash
cd WEAVE-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

Add screenshots of:

- 🏠 Dashboard
- 📄 Resume Analyzer
- 💼 Job Search
- 🎯 Resume Match Report
- 🏢 Company Research
- 🤖 AI Career Assistant

---

# 📈 Current Project Status

## ✅ Completed

- AI Career Assistant
- Resume Parsing (PDF & DOCX)
- Resume Analyzer
- Resume Report PDF
- Smart Job Search
- Saved Jobs
- Company Research
- AI Company Insights
- Resume Match Engine
- Match Score System
- Match Report PDF
- Google Gemini Integration
- LangChain Integration
- ChromaDB Vector Database
- RAG Knowledge Base
- SQLite Database
- Modular Architecture

---

# 🔮 Future Enhancements

- AI Cover Letter Generator
- Mock Interview Assistant
- LinkedIn Profile Analysis
- Skill Gap Visualizer
- Career Roadmap Generator
- User Authentication
- Cloud Deployment
- Dashboard Analytics
- Resume Version History
- Learning Resource Recommendations

---

# 👥 Team

| Name | Role |
|------|------|
| **Shubh Lakhmani** | AI & DS |
| **Chhavi Mishra** | AI & DS |
| **Pritha** | CSE |

**Global Institute of Technology & Management (GITM)**

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a Star!

### Built with ❤️ by Team WEAVE

</div>
