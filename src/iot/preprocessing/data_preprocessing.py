"""
Preprocesses raw sensor data by validating, normalizing, and performing sensor health monitoring.
Includes fallback logic and integration with the incident response system.
"""

import json
import pandas as pd
import time
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load preprocessing configuration
with open("preprocessing_config.json", "r") as f:
    config = json.load(f)

def load_sensor_data(file_path: str) -> dict:
    """
    Load raw sensor data from a JSON file.
    """
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def check_sensor_health(sensor_id: str, data: dict):
    """
    Monitors sensor data for anomalies based on pre-defined thresholds.
    If thresholds are exceeded, triggers fallback procedures.
    """
    scrap = data["data"].get("scrapWeight", 0.0)
    emission = data["data"].get("emissionLevel", 0.0)
    max_scrap = config.get("max_scrapWeight", 100)
    max_emission = config.get("max_emissionLevel", 50)

    if scrap > max_scrap or emission > max_emission:
        logging.warning(f"Sensor {sensor_id} reporting abnormal data: Scrap={scrap}, Emission={emission}")
        trigger_fallback(sensor_id)
    else:
        logging.info(f"Sensor {sensor_id} is healthy.")

def trigger_fallback(sensor_id: str):
    """
    Activates fallback procedures:
    - Notifies the Incident Response system.
    - Logs the fallback event.
    """
    fallback_message = {"sensor_id": sensor_id, "issue": "Sensor data anomaly detected."}
    logging.info(f"Fallback activated for {sensor_id}: {fallback_message}")
    try:
        response = requests.post("http://incident-handler/api/report", json=fallback_message, timeout=5)
        if response.status_code == 200:
            logging.info("Incident reported successfully.")
        else:
            logging.error(f"Error reporting incident: {response.status_code}")
    except Exception as e:
        logging.exception(f"Exception while reporting incident: {str(e)}")

def preprocess_data(data: dict) -> dict:
    """
    Preprocesses sensor data:
    - Checks sensor health.
    - Converts timestamp to a datetime object.
    - Normalizes numerical values.
    """
    sensor_id = data.get("sensorId", "Unknown")
    check_sensor_health(sensor_id, data)
    
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    data["data"]["scrapWeight"] = float(data["data"].get("scrapWeight", 0.0))
    data["data"]["emissionLevel"] = float(data["data"].get("emissionLevel", 0.0))
    return data

if __name__ == "__main__":
    sample_data = load_sensor_data("sample_sensor_data.json")
    processed_data = preprocess_data(sample_data)
    logging.info(f"Processed Data: {processed_data}")
    time.sleep(2)
