#aqi_prediction_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("../dataset/preprocessed-aqi-dataset.csv")

# Example feature and target
X = data[['PM2.5']]
y = data['AQI']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy check
mae = mean_absolute_error(y_test, predictions)

print("Model training completed.")
print("Mean Absolute Error:", mae)
