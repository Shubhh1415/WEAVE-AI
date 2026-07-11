import requests

API_URL = "https://remotive.com/api/remote-jobs"


def search_jobs(keyword, location=""):

    try:

        response = requests.get(API_URL)

        data = response.json()

        jobs = data["jobs"]

        filtered = []

        for job in jobs:

            if keyword.lower() in job["title"].lower():

                if location == "" or location.lower() in job["candidate_required_location"].lower():

                    filtered.append(
                        {
                            "title": job["title"],
                            "company": job["company_name"],
                            "location": job["candidate_required_location"],
                            "url": job["url"]
                        }
                    )

        return filtered

    except Exception as e:

        return []