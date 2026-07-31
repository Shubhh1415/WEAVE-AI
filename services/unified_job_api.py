from services.job_api import fetch_jobs

# Future providers
# from services.remoteok_api import fetch_remoteok_jobs
# from services.arbeitnow_api import fetch_arbeitnow_jobs


def search_all_jobs(query):
    """
    Unified Job Search Service
    """

    jobs = []

    # Provider 1
    jobs.extend(fetch_jobs(query))

    # Provider 2 (Enable later)
    # jobs.extend(fetch_remoteok_jobs(query))

    # Provider 3 (Enable later)
    # jobs.extend(fetch_arbeitnow_jobs(query))

    # Remove duplicates
    unique = {}

    for job in jobs:

        key = (
            job.get("title", ""),
            job.get("company", "")
        )

        if key not in unique:
            unique[key] = job

    return list(unique.values())