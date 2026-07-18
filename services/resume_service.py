import pdfplumber
from docx import Document

from services.gemini_service import ask_ai


def extract_resume_text(uploaded_file):
    """
    Extract text from PDF or DOCX resume.
    """

    file_name = uploaded_file.name.lower()

    # PDF
    if file_name.endswith(".pdf"):

        text = ""

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    # DOCX
    elif file_name.endswith(".docx"):

        document = Document(uploaded_file)

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        return text

    else:

        return ""


def analyze_resume(resume_text):
    """
    Send resume to Gemini for analysis.
    """

    prompt = f"""
You are WEAVE AI, an expert AI Resume Reviewer.

Analyze the following resume and respond ONLY in well-formatted Markdown.

Use this exact format:

# 📊 Resume Score
Give a score out of 100 with one short reason.

# 💪 Strengths
- Point 1
- Point 2
- Point 3

# ⚠️ Weaknesses
- Point 1
- Point 2

# 📚 Missing Skills
- Skill 1
- Skill 2
- Skill 3

# 🚀 Suggestions
- Suggestion 1
- Suggestion 2
- Suggestion 3

# 🎯 Best Suitable Job Roles
- Role 1
- Role 2
- Role 3

Resume:

{resume_text}
"""

    return ask_ai(prompt)