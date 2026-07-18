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

### 💼 Career Features
- 🔍 AI-powered Job Search
- ❤️ Save & Manage Favorite Jobs
- 🗑️ Remove Saved Jobs
- 💾 Persistent SQLite Database

### 🤖 AI Features
- AI Career Assistant powered by Google Gemini
- Resume Analysis with personalized feedback
- Resume Strengths & Improvement Suggestions
- Download Resume Analysis Report (PDF)

### 📚 Knowledge Base (RAG)
- Upload PDF & DOCX documents
- Automatic document text extraction
- Intelligent text chunking
- Persistent ChromaDB vector database
- Semantic document search
- AI-powered Question Answering over uploaded documents

### 🎨 User Experience
- Modern Streamlit Interface
- Responsive Sidebar Navigation
- Modular Component Architecture
- Dark Theme UI

---

## 🚀 Planned Features

### 🤖 AI Enhancements
- Mock Interview Simulator
- ATS Resume Score Checker
- Resume vs Job Description Matching
- AI Cover Letter Generator
- Personalized Career Roadmap
- Skill Gap Analysis

### 📚 Advanced RAG
- Multi-document Knowledge Base
- Source Citations
- Document Management (View/Delete)
- Better Retrieval & Ranking
- Chat History
- Knowledge Base Categories

### 🎨 UI Improvements
- Premium SaaS Dashboard
- Interactive Analytics Cards
- Glassmorphism Design
- Better Chat Interface
- Dashboard Statistics
- Loading Animations

### ☁️ Future Enhancements
- User Authentication
- Cloud Database Support
- Resume Version History
- Export Chat & Reports
- Admin Dashboard
- Deployment on Streamlit Cloud

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

# 📌 Project Status

### ✅ Completed
- AI Career Assistant (Google Gemini)
- AI Resume Analyzer
- Resume Analysis PDF Report Generation
- Job Search System
- Save & Manage Jobs
- SQLite Database Integration
- Modern Streamlit Dashboard
- Modular Project Architecture
- Document Upload (PDF & DOCX)
- Document Text Extraction
- ChromaDB Integration
- Persistent Vector Database
- Basic Knowledge Base Interface

---

### 🚧 In Progress
- RAG (Retrieval-Augmented Generation) Pipeline
- AI Document Question Answering
- Premium SaaS UI Redesign
- Improved Knowledge Base Experience
- Enhanced Error Handling & Performance

---

### ⏳ Upcoming
- Multi-Document Knowledge Base
- Source Citations for AI Responses
- Resume vs Job Description Matching
- ATS Resume Score Checker
- AI Mock Interview
- AI Cover Letter Generator
- Personalized Career Roadmap
- Skill Gap Analysis
- Dashboard Analytics
- User Authentication
- Cloud Deployment
- Admin Dashboard

---

### 🚀 Overall Progress

**Track A:** ✅ 100% Complete

**Track B:** 🚧 ~80% Complete

**Overall Project:** **~85% Complete**

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
