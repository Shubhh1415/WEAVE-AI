# 🤖 WEAVE-AI

<div align="center">

### Weaving Opportunities with Artificial Intelligence

**An AI-Powered Career Assistant developed as part of the Capabl AI Agent Internship (Track A).**

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 📖 Overview

WEAVE-AI is an intelligent career assistant that helps users discover job opportunities through an interactive web application.

The project is being developed during the **Capabl AI Agent Internship (Track A)** using Python and Streamlit while following clean software engineering principles, modular architecture, and version control best practices.

---

# 🎯 Problem Statement

Searching for relevant job opportunities often requires visiting multiple platforms, applying filters repeatedly, and manually organizing useful openings.

WEAVE-AI aims to simplify this process by providing a single platform where users can search opportunities and gradually expand the experience with AI-powered career assistance.

---

## ✨ Current Features

### 🤖 AI Features
- AI Career Assistant powered by Google Gemini
- AI-powered Resume Analysis
- Personalized Resume Feedback & Suggestions
- Company Research with AI-generated Career Insights
- Knowledge Base with RAG Foundation

### 💼 Career Features
- Job Search
- Saved Jobs Management
- Resume Parsing (PDF & DOCX)
- Company Information Lookup

### 📚 Knowledge Base
- Upload PDF Documents
- Upload DOCX Documents
- Automatic Document Processing
- Text Chunking
- ChromaDB Vector Database
- Semantic Search Foundation

### 💾 Data Management
- SQLite Database Integration
- Persistent Saved Jobs
- Persistent Vector Store

### 🎨 User Interface
- Modern Streamlit Dashboard
- Responsive Sidebar Navigation
- Modular Project Architecture
- Dark Theme Interface
---

## 🚀 Planned Features

### 🤖 AI Enhancements
- ATS Resume Score Checker
- Resume vs Job Description Matching
- AI Cover Letter Generator
- Mock Interview Preparation
- Personalized Career Roadmap
- Skill Gap Analysis

### 📚 Advanced Knowledge Base
- Multi-Document Support
- Source Citations
- Document Management
- Conversation Memory
- Advanced Semantic Retrieval

### 💼 Career Features
- Unified Job Search
- Intelligent Job Matching
- Company Comparison
- Career Recommendation Engine
- Learning Resource Recommendations

### 🎨 User Experience
- Premium SaaS Dashboard
- Interactive Analytics
- Better Visualizations
- Mobile-Friendly Interface
- Enhanced Performance

### ☁️ Deployment
- Cloud Deployment
- User Authentication
- Admin Dashboard
- Usage Analytics
---

# 🏗 System Architecture

```text
                  User
                    │
                    ▼
        Streamlit Web Application
                    │
                    ▼
          Application Controller
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 Job Search     AI Assistant    Database
      │                           │
      ▼                           ▼
 Public Job API               SQLite
```

---

# 📂 Project Structure

```text
WEAVE-AI/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
├── .gitignore
│
├── assets/
├── components/
├── config/
├── database/
├── docs/
├── pages/
├── services/
├── tools/
└── utils/
```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| Version Control | Git & GitHub |
| Database | SQLite *(Planned)* |
| AI Model | Google Gemini *(Planned)* |
| AI Framework | LangChain *(Planned)* |
| API Integration | Requests |
| Data Handling | Pandas |

---

# ⚙ Installation

```bash
git clone https://github.com/Shubhh1415/WEAVE-AI.git

cd WEAVE-AI

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 📈 Project Status

### ✅ Completed
- AI Career Assistant
- Job Search System
- Saved Jobs Management
- Resume Analyzer
- Resume Parsing (PDF & DOCX)
- Resume Analysis PDF Report
- Company Research Module
- AI-powered Company Insights
- Company Information Lookup
- Knowledge Base Foundation
- ChromaDB Integration
- SQLite Database
- Modular Project Architecture
- Gemini AI Integration

---

### 🚧 In Progress
- Unified Job Search
- Job Matching Engine
- End-to-End RAG Workflow Optimization
- Knowledge Base Improvements
- UI & Performance Enhancements

---

### ⏳ Planned
- Resume vs Job Description Matching
- ATS Resume Score Checker
- Skill Gap Analysis
- AI Cover Letter Generator
- Mock Interview Assistant
- Personalized Career Roadmap
- Dashboard Analytics
- User Authentication
- Cloud Deployment

---

# 👥 Team

| Name | Branch |
|------|------|
| **Shubh Lakhmani** | AI & DS |
| **Chhavi Mishra** | AI & DS |
| **Pritha** | CSE |

**Global Institute of Technology & Management (GITM)**

---

# 🤝 Contributing

This project is being developed as part of the Capabl AI Agent Internship.

Suggestions, improvements, and contributions are always welcome through pull requests and issue discussions.

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### ⭐ If you like this project, consider giving it a star.

**Built with ❤️ by Team WEAVE**

</div>
