import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

df = pd.read_csv("dataset.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["news"])

model = MultinomialNB()
model.fit(X, df["label"])

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully!")