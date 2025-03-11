"""
Flask application to serve dashboard metrics for AlumiCatalyst.
Aggregates data from various sources for real-time insights.
"""

from flask import Flask, jsonify
import random
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/api/v1/dashboard/metrics', methods=['GET'])
def get_metrics():
    metrics = {
        "scrapLoss": round(random.uniform(5.0, 15.0), 2),
        "carbonEmission": round(random.uniform(10.0, 25.0), 2),
        "equipmentEfficiency": round(random.uniform(75.0, 95.0), 2)
    }
    logging.info(f"Returning dashboard metrics: {metrics}")
    return jsonify({"metrics": metrics})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
