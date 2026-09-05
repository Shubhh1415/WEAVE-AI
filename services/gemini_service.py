import time
from google import genai

from config.settings import API_KEY


client = genai.Client(api_key=API_KEY)

MODEL = "models/gemini-3.5-flash"


def ask_ai(prompt, max_retries=3):
    """
    Send a prompt to Gemini with automatic retry handling
    for temporary API/service failures.
    """

    last_error = None

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            return response.text

        except Exception as e:

            last_error = e

            error_text = str(e).lower()

            # Retry temporary Gemini availability/rate-limit errors
            retryable_errors = [
                "503",
                "unavailable",
                "high demand",
                "429",
                "resource exhausted",
                "timeout",
                "temporarily"
            ]

            if any(error in error_text for error in retryable_errors):

                if attempt < max_retries - 1:

                    wait_time = 2 ** attempt

                    time.sleep(wait_time)

                    continue

            raise last_error

    raise last_error
def get_gemini_response(prompt):
    """
    Backward-compatible wrapper for older WEAVE-AI services.
    """
    return ask_ai(prompt)