# aqi_prediction_model.py

import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("../dataset/preprocessed-aqi-dataset.csv")

# Features and target
X = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']]
y = data['AQI']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "aqi_model.pkl")
print("Model saved successfully as aqi_model.pkl")

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n===== Model Evaluation =====")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R² Score: {r2:.4f}")

# Plot Actual vs Predicted AQI
plt.figure(figsize=(8, 5))
plt.scatter(y_test, predictions, alpha=0.7)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--',
    linewidth=2
)

plt.xlabel("Actual AQI")
plt.ylabel("Predicted AQI")
plt.title("Actual vs Predicted AQI")
plt.grid(True)

# Save graph
plt.savefig("actual_vs_predicted.png", dpi=300, bbox_inches="tight")
plt.show()

print("Graph saved successfully as actual_vs_predicted.png")
