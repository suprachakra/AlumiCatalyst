"""
Provides simulation-based training for users.
Allows interactive scenarios for dashboard navigation, predictive analytics, and incident response.
"""

import json
import time
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory store for simulation results
simulation_results = []

@app.route('/api/v1/training/simulate', methods=['POST'])
def simulate_training():
    """
    Simulate a training scenario.
    Expects JSON with a scenario description and user responses.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing simulation data"}), 400

    simulation_entry = {
        "id": len(simulation_results) + 1,
        "scenario": data.get("scenario"),
        "userResponse": data.get("userResponse"),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    simulation_results.append(simulation_entry)
    logging.info(f"Simulation result recorded: {simulation_entry}")
    return jsonify({"status": "success", "result": simulation_entry}), 200

@app.route('/api/v1/training/results', methods=['GET'])
def get_simulation_results():
    return jsonify({"simulationResults": simulation_results}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)
