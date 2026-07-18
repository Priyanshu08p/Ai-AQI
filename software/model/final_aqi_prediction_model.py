import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
data = pd.read_csv("../dataset/Bangalore_AQI_Cleaned.csv")

# Keep only numeric columns
data = data.select_dtypes(include=[np.number])

# Features and target
X = data.drop("AQI", axis=1)
y = data["AQI"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=150,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Model evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# Save model
joblib.dump(model, "bangalore_aqi_model.pkl")

print("Model saved successfully.")
print("Features used:", list(X.columns))
