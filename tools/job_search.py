from services.job_api import fetch_jobs


def search_jobs(keyword):
    """
    Fetch jobs from API and format them for the UI.
    """

    jobs = fetch_jobs(keyword)

    results = []

    for job in jobs:

        results.append({
            "title": job.get("title") or "Job Title Not Available",
            "company": job.get("companyName") or "Company Not Available",
            "location": job.get("location") or "Remote / Not Specified",
            "url": job.get("url") or ""
        })

    return results