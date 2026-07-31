import requests


BASE_URL = "https://www.arbeitnow.com/api/job-board-api"


def fetch_arbeitnow_jobs(query):
    """
    Fetch jobs from Arbeitnow API.
    """

    try:
        response = requests.get(BASE_URL, timeout=10)

        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data.get("data", []):

            title = job.get("title", "")

            if query.lower() not in title.lower():
                continue

            jobs.append({
                "title": title,
                "company": job.get("company_name", "N/A"),
                "location": job.get("location", "Remote"),
                "url": job.get("url", ""),
                "source": "Arbeitnow"
            })

        return jobs

    except Exception as e:
        print(f"Arbeitnow Error: {e}")
        return []