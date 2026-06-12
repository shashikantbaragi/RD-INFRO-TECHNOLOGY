import streamlit as st
from textblob import TextBlob

st.title("😊 AI Sentiment Analysis System")

text = st.text_area("Enter Social Media Post")

if st.button("Analyze Sentiment"):

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        st.success("Positive Sentiment 😊")
    elif polarity < 0:
        st.error("Negative Sentiment 😞")
    else:
        st.info("Neutral Sentiment 😐")

    st.write("Polarity Score:", polarity)