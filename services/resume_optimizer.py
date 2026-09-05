import json
from services.gemini_service import ask_ai


def optimize_resume(resume_text, job_description):
    """
    Analyze a resume against a job description and provide
    ATS optimization, keyword suggestions, skills gap analysis,
    learning recommendations, and LinkedIn optimization.
    """

    prompt = f"""
You are WEAVE AI, an expert ATS Resume Optimization and Career Assistant.

Analyze the candidate's resume against the target job description.

========================
RESUME
========================

{resume_text}

========================
JOB DESCRIPTION
========================

{job_description}

========================
TASK
========================

Perform a detailed career optimization analysis.

Return ONLY valid JSON.

Do NOT use Markdown.
Do NOT use code blocks.
Do NOT add explanations outside the JSON.

Use EXACTLY this structure:

{{
    "ats_score": 0,

    "ats_analysis": [
        "point 1",
        "point 2",
        "point 3"
    ],

    "matching_keywords": [
        "keyword 1",
        "keyword 2"
    ],

    "missing_keywords": [
        "keyword 1",
        "keyword 2",
        "keyword 3"
    ],

    "keyword_recommendations": [
        "recommendation 1",
        "recommendation 2",
        "recommendation 3"
    ],

    "skills_gap": [
        {{
            "skill": "skill name",
            "importance": "High",
            "reason": "short explanation"
        }}
    ],

    "learning_recommendations": [
        {{
            "skill": "skill name",
            "resource_type": "Course / Project / Practice",
            "recommendation": "what the candidate should learn or practice"
        }}
    ],

    "resume_improvements": [
        "improvement 1",
        "improvement 2",
        "improvement 3",
        "improvement 4"
    ],

    "tailored_resume": {{
        "professional_summary": "ATS-friendly professional summary",
        "key_skills": [
            "skill 1",
            "skill 2",
            "skill 3"
        ],
        "experience_improvements": [
            "suggested bullet point 1",
            "suggested bullet point 2",
            "suggested bullet point 3"
        ]
    }},

    "linkedin_optimization": {{
        "headline": "optimized LinkedIn headline",
        "about_section": "optimized LinkedIn About section",
        "skills_to_add": [
            "skill 1",
            "skill 2"
        ],
        "profile_tips": [
            "tip 1",
            "tip 2",
            "tip 3"
        ]
    }},

    "final_recommendation": "short final recommendation"
}}

========================
RULES
========================

1. ats_score must be an integer from 0 to 100.

2. Compare the resume ONLY against the provided job description.

3. Never invent experience, education, certifications, projects,
   employers, achievements, or skills that are not supported by
   the resume.

4. Missing keywords should be relevant keywords from the job
   description that are absent or weakly represented in the resume.

5. Skills gap should prioritize skills that materially improve
   the candidate's suitability for the job.

6. Learning recommendations should be realistic and actionable.

7. The tailored resume must remain truthful to the candidate's
   actual background.

8. Suggestions should be ATS-friendly.

9. LinkedIn suggestions should be concise and professional.

10. Return valid JSON only.
"""

    response = ask_ai(prompt)

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        cleaned = response.strip()

        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]

        if cleaned.startswith("```"):
            cleaned = cleaned[3:]

        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]

        cleaned = cleaned.strip()

        return json.loads(cleaned)