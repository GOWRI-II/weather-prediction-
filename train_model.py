
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load the weather dataset
data = pd.read_csv("weather.csv")

print("First five rows:")
print(data.head())

# 2. Separate input features and target
X = data[
    ["Temperature", "Humidity", "Wind_Speed", "Pressure"]
]

y = data["Rain_Tomorrow"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Create the machine learning model
model = RandomForestClassifier(
    n_estimators=100, random_state=42
)

# 5. Train the model
model.fit(X_train, y_train)

print("\nModel training completed!")

# 6. Test the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model accuracy:", round(accuracy * 100, 2), "%")

# 7. Save the trained model
with open("weather_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as weather_model.pkl")

# 8. Make a sample prediction
sample = pd.DataFrame(
    [[24, 85, 20, 1005]],
    columns=["Temperature", "Humidity", "Wind_Speed", "Pressure"]
)

prediction = model.predict(sample)

print("Rain prediction:", prediction[0])
