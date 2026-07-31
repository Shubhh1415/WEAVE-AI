import json
from services.gemini_service import ask_ai


def match_resume_with_job(resume_text, job):

    prompt = f"""
You are an ATS Resume Matching Expert.

Compare the resume with the given job.

Resume:
{resume_text}

Job Details:

Title: {job.get('title', '')}
Company: {job.get('company', '')}
Location: {job.get('location', '')}
URL: {job.get('url', '')}

Return ONLY valid JSON.

Do not write markdown.
Do not use code blocks.
Do not explain anything.

Format:

{{
    "score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "suggestions": [],
    "recommendation": ""
}}

Rules:

- score must be an integer between 0 and 100.
- matching_skills should be a list.
- missing_skills should be a list.
- suggestions should contain 3-5 items.
- recommendation should be a short paragraph.
"""

    response = ask_ai(prompt)

    try:
        return json.loads(response)

    except Exception:

        # Remove markdown code block if Gemini adds one
        response = response.replace("```json", "")
        response = response.replace("```", "")

        return json.loads(response)