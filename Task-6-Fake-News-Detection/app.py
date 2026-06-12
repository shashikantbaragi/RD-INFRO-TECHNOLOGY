import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📰 AI Fake News Detection")

news = st.text_area("Enter News Article")

if st.button("Check News"):
    data = vectorizer.transform([news])
    prediction = model.predict(data)[0]

    if prediction == "REAL":
        st.success("✅ This News appears REAL")
    else:
        st.error("❌ This News appears FAKE")