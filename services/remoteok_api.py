import requests


def fetch_remoteok_jobs(query):
    """
    Fetch jobs from the RemoteOK API.
    """

    try:
        response = requests.get(
            "https://remoteok.com/api",
            headers={"User-Agent": "WEAVE-AI"},
            timeout=10
        )

        response.raise_for_status()

        jobs = response.json()

        results = []

        # First element contains metadata
        for job in jobs[1:]:

            title = job.get("position", "")

            if query.lower() not in title.lower():
                continue

            results.append({
                "title": title,
                "company": job.get("company", "Unknown"),
                "location": job.get("location", "Remote"),
                "url": job.get("url", ""),
                "source": "RemoteOK"
            })

        return results

    except Exception as e:
        print(f"RemoteOK Error: {e}")
        return []