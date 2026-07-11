from tools.job_search import search_jobs
import streamlit as st

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------
# SIDEBAR
# --------------------------

with st.sidebar:

    st.title("🤖 CareerPilot AI")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🔍 Job Search",
            "❤️ Saved Jobs",
            "ℹ About"
        ]
    )

    st.markdown("---")

    st.info("Capabl AI Internship\n\nTrack A")

# --------------------------
# DASHBOARD
# --------------------------

if page == "🏠 Dashboard":

    st.title("AI Career Assistant")

    st.write(
        "Welcome to your AI-powered career assistant."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Jobs Found", "0")

    with col2:
        st.metric("Saved Jobs", "0")

    with col3:
        st.metric("Resume Score", "--")

    st.divider()

    st.subheader("Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button("🔍 Search Jobs", use_container_width=True)

    with c2:
        st.button("📄 Upload Resume", use_container_width=True)

    with c3:
        st.button("🤖 Ask AI", use_container_width=True)

# --------------------------
# JOB SEARCH
# --------------------------

elif page == "🔍 Job Search":

    st.title("Job Search")

    role = st.text_input("Job Role")

    location = st.text_input("Location")

    if st.button("Search Jobs"):

        jobs = search_jobs(role, location)

        if len(jobs) == 0:

            st.warning("No Jobs Found.")

        else:

            st.success(f"{len(jobs)} Jobs Found")

            for job in jobs:

                st.subheader(job["title"])

                st.write("🏢", job["company"])

                st.write("📍", job["location"])

                st.link_button(
                    "Apply",
                    job["url"]
                )

                st.divider()

# --------------------------
# SAVED JOBS
# --------------------------

elif page == "❤️ Saved Jobs":

    st.title("Saved Jobs")

    st.info("No saved jobs.")

# --------------------------
# ABOUT
# --------------------------

elif page == "ℹ About":

    st.title("About")

    st.write("""
    AI Career Assistant

    Developed during the Capabl AI Internship.

    Version 1.0
    """)