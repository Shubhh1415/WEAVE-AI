import sqlite3

DATABASE_NAME = "database/weave.db"


# ---------------------------------
# DATABASE CONNECTION
# ---------------------------------

def get_connection():
    return sqlite3.connect(DATABASE_NAME)


# ---------------------------------
# CREATE TABLES
# ---------------------------------

def create_tables():

    with get_connection() as conn:

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS saved_jobs(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                title TEXT NOT NULL,

                company TEXT NOT NULL,

                location TEXT,

                url TEXT UNIQUE
            )
        """)

        conn.commit()


# ---------------------------------
# SAVE JOB
# ---------------------------------

def save_job(title, company, location, url):

    with get_connection() as conn:

        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO saved_jobs
            (title, company, location, url)

            VALUES (?, ?, ?, ?)
        """, (
            title,
            company,
            location,
            url
        ))

        conn.commit()


# ---------------------------------
# GET SAVED JOBS
# ---------------------------------

def get_saved_jobs():

    with get_connection() as conn:

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *

            FROM saved_jobs

            ORDER BY id DESC
        """)

        jobs = cursor.fetchall()

    return jobs


# ---------------------------------
# DELETE JOB
# ---------------------------------

def delete_job(job_id):

    with get_connection() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM saved_jobs
            WHERE id = ?
            """,
            (job_id,)
        )

        conn.commit()


# ---------------------------------
# COUNT SAVED JOBS
# ---------------------------------

def get_saved_job_count():

    with get_connection() as conn:

        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)

            FROM saved_jobs
        """)

        count = cursor.fetchone()[0]

    return count


# ---------------------------------
# CLEAR DATABASE (Testing)
# ---------------------------------

def clear_saved_jobs():

    with get_connection() as conn:

        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM saved_jobs
        """)

        conn.commit()