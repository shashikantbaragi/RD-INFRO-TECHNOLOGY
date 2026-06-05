import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("dataset.csv")

X = data[['fever', 'cough', 'headache', 'fatigue']]
y = data['disease']

model = DecisionTreeClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")
