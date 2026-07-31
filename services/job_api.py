import requests

BASE_URL = "https://himalayas.app/jobs/api/search" 


def fetch_jobs(query):
    try:
        response = requests.get(
            BASE_URL,
            params= {
                "q": query,
                "sort": "relevant"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()
        raw_jobs = data.get("jobs", [])

        jobs = []
        search = query.lower().strip()

        for job in raw_jobs:

            # ---------- Title ----------
            title = job.get("title", "")

            # ---------- Company ----------
            company = ""

            if isinstance(job.get("company"), dict):
                company = job["company"].get("name", "")
            else:
                company = (
                    job.get("company")
                    or job.get("companyName")
                    or ""
                )

            # ---------- Location ----------
            location = (
                job.get("location")
                or job.get("locationName")
                or "Remote"
            )

            # ---------- URL ----------
            url = (
                job.get("url")
                or job.get("applyUrl")
                or job.get("apply_url")
                or ""
            )

            # ---------- Skills ----------
            skills = ""

            if isinstance(job.get("skills"), list):
                skills = " ".join(job["skills"])

            # ---------- Search Text ----------
            searchable_text = f"{title} {company} {location} {skills}".lower()

            # Skip unrelated jobs
            if search and search not in searchable_text:
                continue

            print(job)
            jobs.append({
                "title": title,
                "company": company if company else "Unknown Company",
                "location": location,
                "url": url
            })

        return jobs

    except Exception as e:
        print(f"Himalayas API Error: {e}")
        return []