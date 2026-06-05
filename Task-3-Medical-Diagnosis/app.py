import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏥 AI-Powered Medical Diagnosis System")
st.markdown("Predict diseases based on symptoms using Machine Learning.")

st.write("Select your symptoms:")

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
fatigue = st.checkbox("Fatigue")

if st.button("Predict Disease"):
    prediction = model.predict([[fever, cough, headache, fatigue]])
    st.success(f"Predicted Disease: {prediction[0]}")