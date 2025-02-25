"""
Microservice Integration via API Gateway

This Flask-based gateway routes incoming API requests to the appropriate internal microservices.
It reads configuration from the mapping defined in the gateway config.
"""

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mapping of service names to internal endpoints
service_endpoints = {
    "iot-sensor-service": "http://iot-sensor-service:5000/api/v1/iot/sensors",
    "prediction-service": "http://prediction-service:5000/api/v1/analytics/predict",
    "blockchain-service": "http://blockchain-service:5000/api/v1/blockchain/trace",
    "dashboard-service": "http://dashboard-service:8080/api/v1/dashboard/metrics"
}

@app.route('/api/v1/<service>/<path:subpath>', methods=['GET', 'POST'])
def gateway(service, subpath):
    endpoint = service_endpoints.get(service)
    if not endpoint:
        return jsonify({"error": "Service not found"}), 404

    # Construct the final URL by appending subpath to the base endpoint
    url = f"{endpoint}/{subpath}"
    headers = dict(request.headers)
    data = request.get_json() if request.is_json else request.form

    try:
        if request.method == 'POST':
            resp = requests.post(url, json=data, headers=headers)
        else:
            resp = requests.get(url, params=request.args, headers=headers)
        return (resp.content, resp.status_code, resp.headers.items())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
