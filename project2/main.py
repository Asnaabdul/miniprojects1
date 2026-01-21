import streamlit as st
import PyPDF2
import io
import re

st.set_page_config(
    page_title="Resume Critiquer",
    page_icon="📃",
    layout="centered"
)

st.title("📃 Resume Critiquer (Offline)")
st.markdown("Upload your resume and get **rule-based smart feedback** — no AI API required!")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or TXT)",
    type=["pdf", "txt"]
)

job_role = st.text_input("Enter the job role you're targeting (optional)")
analyze = st.button("Analyze Resume")

# ---------- Helpers ----------

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    else:
        return uploaded_file.read().decode("utf-8", errors="ignore")

def analyze_resume(text, job_role=None):
    feedback = []

    word_count = len(text.split())
    lines = text.splitlines()
    lower_text = text.lower()

    # ----- Length Check -----
    if word_count < 300:
        feedback.append("🔴 Resume is too short. Consider adding more details to your experience and projects.")
    elif word_count > 900:
        feedback.append("🟡 Resume is quite long. Try to keep it concise (1–2 pages).")
    else:
        feedback.append("🟢 Resume length looks good.")

    # ----- Section Checks -----
    sections = ["skills", "experience", "education", "projects"]
    missing = [s for s in sections if s not in lower_text]

    if missing:
        feedback.append(f"🔴 Missing important sections: {', '.join(missing).title()}.")
    else:
        feedback.append("🟢 All key resume sections are present.")

    # ----- Action Verbs -----
    action_verbs = [
        "developed", "designed", "implemented", "managed", "built",
        "led", "created", "optimized", "improved", "analyzed"
    ]

    verb_count = sum(lower_text.count(v) for v in action_verbs)
    if verb_count < 5:
        feedback.append("🟡 Use more action verbs (e.g., Developed, Implemented, Led) to strengthen impact.")
    else:
        feedback.append("🟢 Good use of action-oriented language.")

    # ----- Skills Density -----
    skills_keywords = [
        "python", "java", "sql", "html", "css", "javascript",
        "machine learning", "data analysis", "react", "node",
        "git", "docker", "api"
    ]

    skills_found = [s for s in skills_keywords if s in lower_text]

    if len(skills_found) < 5:
        feedback.append("🟡 Skills section could be stronger. Consider adding more relevant technical skills.")
    else:
        feedback.append(f"🟢 Strong skills presence: {', '.join(skills_found[:8])}")

    # ----- Job Role Matching -----
    if job_role:
        role_words = re.findall(r"\w+", job_role.lower())
        matches = [w for w in role_words if w in lower_text]

        if matches:
            feedback.append(f"🟢 Resume aligns with the job role keywords: {', '.join(matches)}")
        else:
            feedback.append("🔴 Resume is not well-tailored to the specified job role. Add role-specific keywords.")

    # ----- Formatting Check -----
    if len(lines) < 20:
        feedback.append("🟡 Resume formatting looks minimal. Consider clearer section headings and spacing.")
    else:
        feedback.append("🟢 Resume formatting appears structured.")

    return feedback


# ---------- Main Logic ----------

if analyze and uploaded_file:
    try:
        resume_text = extract_text_from_file(uploaded_file)

        if not resume_text.strip():
            st.error("Uploaded file contains no readable text.")
            st.stop()

        results = analyze_resume(resume_text, job_role)

        st.markdown("## 📊 Resume Analysis Results")
        for point in results:
            st.markdown(f"- {point}")

        st.markdown("### ✅ Overall Suggestion")
        st.info(
            "Tailor your resume for each job, quantify achievements (numbers/metrics), "
            "and keep bullet points clear and action-driven."
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
