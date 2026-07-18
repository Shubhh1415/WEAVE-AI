import requests

BASE_URL = "https://himalayas.app/jobs/api"

def fetch_jobs(query):

    try:

        response = requests.get(
            BASE_URL,
            params={
                "search": query
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("jobs", [])

    except Exception as e:

        print(e)

        return []