import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
API_KEY = os.getenv("ADZUNA_API_KEY")

BASE_URL = "https://api.adzuna.com/v1/api/jobs/in/search/1"


def fetch_adzuna_jobs(query):
    """
    Fetch jobs from the Adzuna API.
    """

    try:
        params = {
            "app_id": APP_ID,
            "app_key": API_KEY,
            "results_per_page": 10,
            "what": query,
            "content-type": "application/json"
        }

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data.get("results", []):

            jobs.append({
                "title": job.get("title", "N/A"),
                "company": job.get("company", {}).get("display_name", "N/A"),
                "location": job.get("location", {}).get("display_name", "N/A"),
                "url": job.get("redirect_url", ""),
                "source": "Adzuna"
            })

        return jobs

    except Exception as e:
        print(f"Adzuna Error: {e}")
        return []