from services.gemini_service import ask_ai


def get_company_info(company_name):
    """
    Generate company information using Gemini AI.
    """

    prompt = f"""
You are an expert career advisor.

Provide accurate and professional information about the company "{company_name}".

Return the response in Markdown using exactly this format:

# Company Overview
(Brief overview)

# Industry
(Industry)

# Headquarters
(Location)

# Products & Services
(Main products/services)

# Career Opportunities
(Common job roles)

# Skills Required
(Bullet list)

# Why Join This Company?
(Short explanation)

# Interview Preparation Tips
(Bullet list)

If the company does not exist, clearly say:
Company not found.
"""

    try:

        response = ask_ai(prompt)

        if "Company not found" in response:
            return {
                "success": False,
                "error": "Company not found."
            }

        return {
            "success": True,
            "response": response
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }