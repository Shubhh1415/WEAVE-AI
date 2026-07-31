import streamlit as st


def display_match_report(data):

    score = data.get("score", 0)

    st.subheader("📊 Resume Match Report")

    st.progress(score / 100)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Resume Match Score", f"{score}%")

    with col2:

        if score >= 80:
            st.success("🟢 Excellent Match")

        elif score >= 60:
            st.warning("🟡 Good Match")

        else:
            st.error("🔴 Needs Improvement")

    st.divider()

    st.subheader("✅ Matching Skills")

    for skill in data.get("matching_skills", []):
        st.success(skill)

    st.divider()

    st.subheader("❌ Missing Skills")

    for skill in data.get("missing_skills", []):
        st.error(skill)

    st.divider()

    st.subheader("💡 Suggestions")

    for tip in data.get("suggestions", []):
        st.info(tip)

    st.divider()

    st.subheader("🎯 Final Recommendation")

    st.success(data.get("recommendation", ""))