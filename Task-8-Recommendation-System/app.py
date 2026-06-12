import streamlit as st
import pandas as pd

st.title("🎬 AI Recommendation System")

df = pd.read_csv("dataset.csv")

movie = st.selectbox("Select a Movie", df["Movie"])

if st.button("Recommend"):
    genre = df[df["Movie"] == movie]["Genre"].values[0]

    recommendations = df[
        (df["Genre"] == genre) &
        (df["Movie"] != movie)
    ]["Movie"].tolist()

    st.success(f"Recommended Movies based on {movie}")

    for rec in recommendations:
        st.write("⭐", rec)