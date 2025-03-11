"""
Microservice for end-to-end supply chain tracking.
Tracks raw material sourcing, production, and distribution.
Includes API endpoints for updating and retrieving supply chain data.
"""

from flask import Flask, request, jsonify
import logging
import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database for demonstration purposes
supply_chain_data = []

@app.route('/api/v1/supplychain/update', methods=['POST'])
def update_supplychain():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing supply chain data"}), 400
    entry = {
        "id": len(supply_chain_data) + 1,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "rawMaterial": data.get("rawMaterial"),
        "productionStatus": data.get("productionStatus"),
        "distributionStatus": data.get("distributionStatus")
    }
    supply_chain_data.append(entry)
    logging.info(f"Supply chain entry added: {entry}")
    return jsonify({"status": "success", "entry": entry}), 200

@app.route('/api/v1/supplychain/data', methods=['GET'])
def get_supplychain_data():
    return jsonify({"supplyChainData": supply_chain_data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)
