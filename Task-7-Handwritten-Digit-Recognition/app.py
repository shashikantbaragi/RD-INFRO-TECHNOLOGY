import streamlit as st
import pickle
from sklearn.datasets import load_digits

model = pickle.load(open("digit_model.pkl", "rb"))

st.title("✍️ Handwritten Digit Recognition")

digits = load_digits()

digit_number = st.slider("Select a sample digit", 0, len(digits.images)-1)

image = digits.images[digit_number]

st.image(image / 16.0, width=200)

if st.button("Predict"):
    prediction = model.predict([digits.data[digit_number]])
    st.success(f"Predicted Digit: {prediction[0]}")