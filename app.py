import streamlit as st
from services.gemini_service import ask_ai

from tools.job_search import search_jobs
from services.document_loader import load_document, split_document
from services.vector_store import add_documents
from services.rag_service import ask_rag
from services.pdf_service import create_resume_report
from services.ui_service import (
    load_css,
    hero_section,
    metric_card
)
from services.resume_service import (
    extract_resume_text,
    analyze_resume
)
from database.database import (
    create_tables,
    save_job,
    get_saved_jobs,
    delete_job
)

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="WEAVE AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_css()

# -----------------------------
# INITIALIZE DATABASE
# -----------------------------

create_tables()

# -----------------------------
# SESSION STATE
# -----------------------------

if "jobs" not in st.session_state:
    st.session_state.jobs = []

if "keyword" not in st.session_state:
    st.session_state.keyword = ""
if "show_ai" not in st.session_state:
    st.session_state.show_ai = False    

# -----------------------------
# LOAD DATABASE
# -----------------------------

saved_jobs = get_saved_jobs()

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🤖 WEAVE AI")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🔍 Job Search",
            "📚 Knowledge Base",
            "📄  Resume Analyzer",
            "❤️ Saved Jobs",
            "ℹ️ About"
        ]
    )

    st.markdown("---")

    st.info(
        "Capabl AI Internship\n\nTrack A"
    )

# ==================================================
# DASHBOARD
# ==================================================

if page == "🏠 Dashboard":

    st.title("🤖 WEAVE AI")

    st.write(
        "Welcome to your AI-powered Career Assistant."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Jobs Found", len(st.session_state.jobs))

    with col2:
        st.metric("Saved Jobs", len(saved_jobs))

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
      if st.button("🤖 Ask AI", use_container_width=True):
        st.session_state.show_ai = True
        if st.session_state.show_ai:

          st.divider()

    st.subheader("🤖 AI Career Assistant")

    user_prompt = st.text_area(
        "Ask anything about careers, skills, resumes, or interviews"
    )

    if st.button("Send to AI"):

        if user_prompt.strip():

            with st.spinner("Thinking..."):

                response = ask_ai(user_prompt)

            st.success("Response")

            st.write(response)

        else:

            st.warning("Please enter a question.")

# ==================================================
# JOB SEARCH
# ==================================================

elif page == "🔍 Job Search":

    st.title("🔍 Job Search")

    keyword = st.text_input(
        "Enter Job Role",
        value=st.session_state.keyword,
        placeholder="Example: Python Developer"
    )

    if st.button("Search Jobs"):

        if keyword.strip() == "":

            st.warning("Please enter a job role.")

        else:

            st.session_state.keyword = keyword

            with st.spinner("Searching Jobs..."):

                st.session_state.jobs = search_jobs(keyword)

    if len(st.session_state.jobs) == 0:

        st.info("Search for jobs to see results.")

    else:

        st.success(f"{len(st.session_state.jobs)} jobs found")

        for job in st.session_state.jobs:

            with st.container():

                st.subheader(job["title"])

                st.write(f"🏢 **Company:** {job['company']}")

                st.write(f"📍 **Location:** {job['location']}")

                col1, col2 = st.columns(2)

                with col1:

                    if job["url"]:

                        st.link_button(
                            "🚀 Apply Now",
                            job["url"],
                            use_container_width=True
                        )

                with col2:

                    if st.button(
                        "❤️ Save Job",
                        key=f"{job['title']}_{job['company']}"
                    ):

                        save_job(
                            job["title"],
                            job["company"],
                            job["location"],
                            job["url"]
                        )

                        st.success("Job saved successfully!")

                st.divider()


# -----------------------------
# KNOWLEDGE BASE
# -----------------------------               

elif page == "📚 Knowledge Base":

    st.title("📚 Knowledge Base")

    st.write("Upload PDFs or DOCX files and chat with them.")

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "docx"]
    )

    if uploaded_file is not None:

        if st.button("Process Document"):

            with st.spinner("Processing document..."):

                text = load_document(uploaded_file)

                docs = split_document(text)

                add_documents(docs)

            st.success("Document added to Knowledge Base!")

    st.divider()

    question = st.text_input(
        "Ask a question about your uploaded documents"
    )

    if st.button("Ask AI"):

        if question:

            with st.spinner("Searching Knowledge Base..."):

                answer = ask_rag(question)

            st.markdown("### 🤖 WEAVE AI")

            st.write(answer)



# ==================================================
# SAVED JOBS
# ==================================================

elif page == "❤️ Saved Jobs":

    st.title("❤️ Saved Jobs")

    jobs = get_saved_jobs()

    if len(jobs) == 0:

        st.info("No saved jobs yet.")

    else:

        for job in jobs:

           with st.container():

             st.subheader(job[1])

        st.write(f"🏢 Company: {job[2]}")
        st.write(f"📍 Location: {job[3]}")

        col1, col2 = st.columns(2)

        with col1:

            if job[4]:

                st.link_button(
                    "🚀 Apply",
                    job[4],
                    key=f"apply_{job[0]}",
                    use_container_width=True
                )

        with col2:

            if st.button(
                "🗑 Delete",
                key=f"delete_{job[0]}",
                use_container_width=True
            ):

                delete_job(job[0])

                st.success("Job deleted successfully!")

                st.rerun()

        st.divider()

# ==================================================
# RESUME ANALYZER
# ==================================================

elif page == "📄  Resume Analyzer":

    st.title("📄 AI Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload your Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.success("Resume uploaded successfully!")

        if st.button("Analyze Resume", use_container_width=True):

            with st.spinner("Analyzing your resume..."):

                resume_text = extract_resume_text(uploaded_file)

                if not resume_text.strip():

                    st.error("Could not extract text from the resume.")

                else:

                    analysis = analyze_resume(resume_text)

                    st.success("✅ Resume analyzed successfully!")

                    st.divider()

                    st.subheader("📋 AI Resume Report")

                    st.markdown(analysis)
                    pdf_path = create_resume_report(analysis)

                    with open(pdf_path, "rb") as pdf_file:

                      st.download_button(
                        "📥 Download Resume Report",
                           pdf_file,
                           file_name="Resume_Report.pdf",
                            mime="application/pdf",
                            use_container_width=True
                       ) 


# ==================================================
# ABOUT
# ==================================================

elif page == "ℹ️ About":

    st.title("About WEAVE AI")

    st.write("""
### 🤖 WEAVE AI

WEAVE AI is an AI-powered Career Assistant developed as part of the **Capabl AI Internship (Track A).**

### Current Features

- ✅ Live Job Search
- ✅ Public Job API Integration
- ✅ Save Jobs
- ✅ SQLite Database
- ✅ Dashboard
- ✅ Professional Folder Structure

Developed by **Team WEAVE**
""")