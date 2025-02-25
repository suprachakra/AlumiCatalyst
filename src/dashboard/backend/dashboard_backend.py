"""
Dashboard Backend Service
This Flask application serves dashboard data for the AlumiCatalyst platform.
"""

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/v1/dashboard/metrics', methods=['GET'])
def get_metrics():
    # In a real implementation, these values would be retrieved from a database or analytics engine.
    metrics = {
        "scrapLoss": round(random.uniform(5.0, 15.0), 2),
        "carbonEmission": round(random.uniform(10.0, 25.0), 2),
        "equipmentEfficiency": round(random.uniform(75.0, 95.0), 2)
    }
    return jsonify({"metrics": metrics})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
