import streamlit as st
import fitz
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Screening System")

st.write("Upload resumes and rank candidates based on required skills.")

required_skills = st.text_area(
    "Enter required skills",
    "python, machine learning, flask, sql, communication"
)

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

def extract_text_from_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text

if st.button("Screen Resumes"):
    if uploaded_files:
        results = []

        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)

            documents = [required_skills, resume_text]

            vectorizer = CountVectorizer().fit_transform(documents)
            similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]

            score = round(similarity * 100, 2)

            results.append({
                "Candidate Resume": file.name,
                "Match Score (%)": score
            })

        df = pd.DataFrame(results)
        df = df.sort_values(by="Match Score (%)", ascending=False)

        st.subheader("Candidate Ranking")
        st.dataframe(df)

        best_candidate = df.iloc[0]

        st.success(
            f"Best Match: {best_candidate['Candidate Resume']} "
            f"with {best_candidate['Match Score (%)']}% match"
        )

    else:
        st.warning("Please upload at least one resume PDF.")