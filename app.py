# app.py

import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_parser import extract_text_from_jd
from match_score import calculate_match_score

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("🧠 AI Resume Analyzer")
st.write("Upload your resume and a job description to see how well they match!")

# Upload Resume
resume_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

# Job Description Input
jd_option = st.radio("How would you like to input the Job Description?", ("Paste Text", "Upload File"))

if jd_option == "Paste Text":
    job_description = st.text_area("Paste Job Description")
else:
    jd_file = st.file_uploader("Upload Job Description (TXT or PDF)", type=["txt", "pdf"])
    job_description = extract_text_from_jd(jd_file) if jd_file else ""

if resume_file and job_description:
    resume_text = extract_text_from_pdf(resume_file)
    match_score, common_skills = calculate_match_score(resume_text, job_description)

    st.subheader("✅ Match Score:")
    st.progress(match_score)
    st.success(f"Match Score: {match_score}%")

    st.subheader("🛠️ Matching Skills Found:")
    st.write(", ".join(common_skills) if common_skills else "No matching keywords found.")

