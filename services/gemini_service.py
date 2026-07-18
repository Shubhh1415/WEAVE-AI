import os
import time
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def ask_ai(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the response.
    """
    start = time.time()

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash_lite",
            contents=prompt,
        )

        print(f"Response Time: {time.time() - start:.2f} seconds")

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


def get_gemini_response(prompt: str) -> str:
    """
    Used by the RAG service.
    """
    return ask_ai(prompt)