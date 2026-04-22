import streamlit as st

st.title("📁My Projects")

projects = {
    "Student Productivity Tracker": "Student can track their progress.",
    "Payment System": "Transport Payment System.",
    "Portfolio Website": "Personal portfolio."
}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)