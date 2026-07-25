import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

MODEL = "models/gemini-3.5-flash"


def ask_ai(prompt: str) -> str:
    """
    Send prompt to Gemini.
    """

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text


def get_gemini_response(prompt: str) -> str:
    return ask_ai(prompt)