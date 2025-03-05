"""
Prediction API
A Flask-based RESTful API to serve predictions using the trained predictive model.
"""
from flask import Flask, request, jsonify
import numpy as np
from analytics.ai_models.predictive_model import PredictiveModel

app = Flask(__name__)

# Load the predictive model at startup
model = PredictiveModel("analytics/ai_models/model.pkl")

@app.route('/api/v1/analytics/predict', methods=['GET'])
def predict():
    sensor_id = request.args.get('sensorId')
    # Expecting comma-separated feature values in the query parameter 'features'
    features_str = request.args.get('features')
    if not features_str:
        return jsonify({"error": "Missing features parameter"}), 400
    
    try:
        features = np.array([float(x) for x in features_str.split(',')])
    except ValueError:
        return jsonify({"error": "Invalid feature values"}), 400

    prediction = model.predict(features)
    prediction["sensorId"] = sensor_id

    # Additional logging: For carbon management reporting, log emission forecast
    app.logger.info(f"Sensor {sensor_id} - Emission Forecast: {prediction['emissionForecast']}")
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
