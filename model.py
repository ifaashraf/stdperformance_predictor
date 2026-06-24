import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load data
data = pd.read_csv("student_dataset.csv")

# Features
X = data[["StudyHours",
          "Attendance",
          "Assignments",
          "PreviousScore"]]

# Target
y = data["FinalScore"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")