from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load models
aqi_model = joblib.load("../model/bangalore_aqi_model.pkl")
estimation_model = joblib.load("../model/estimation_model.pkl")

FEATURE_ORDER = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]

latest_data = {
    "aqi": None,
    "category": None,
    "precaution": None,
    "pollutants": {}
}


def get_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Poor"
    elif aqi <= 300:
        return "Very Poor"
    return "Hazardous"


def get_precaution(category):
    messages = {
        "Good": "Air quality is good. Outdoor activities are safe.",
        "Moderate": "Air acceptable but sensitive people should reduce outdoor activity.",
        "Poor": "Air pollution high. Wear mask outside.",
        "Very Poor": "Avoid outdoor exercise and stay indoors.",
        "Hazardous": "Health alert! Stay indoors and close windows."
    }

    return messages.get(category, "")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        if "mq2" in data:
            mq2 = float(data["mq2"])

            gas = np.array([[mq2]])

            pollutants = estimation_model.predict(gas)[0]

            features = np.array(pollutants).reshape(1, -1)

            aqi = aqi_model.predict(features)[0]

        else:
            features = [float(data[x]) for x in FEATURE_ORDER]

            features = np.array(features).reshape(1, -1)

            pollutants = features[0]

            aqi = aqi_model.predict(features)[0]

        category = get_category(aqi)
        precaution = get_precaution(category)

        latest_data["aqi"] = round(float(aqi), 2)
        latest_data["category"] = category
        latest_data["precaution"] = precaution
        latest_data["pollutants"] = dict(zip(FEATURE_ORDER, pollutants))

        return jsonify(latest_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/latest", methods=["GET"])
def latest():
    return jsonify(latest_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
