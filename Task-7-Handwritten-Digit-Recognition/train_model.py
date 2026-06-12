from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
import pickle

digits = load_digits()

X = digits.data
y = digits.target

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("digit_model.pkl", "wb"))

print("Model trained successfully!")