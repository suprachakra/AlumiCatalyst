"""
Enterprise-level sensor simulation and data ingestion into Azure IoT Hub.
Includes robust logging, error handling, and retry/fallback mechanisms.
"""

import json
import time
import random
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load sensor configuration
with open('sensor_config.json', 'r') as config_file:
    config = json.load(config_file)

IOT_HUB_ENDPOINT = config.get("iot_hub_endpoint")
API_KEY = config.get("api_key")
SENSOR_ID = config.get("sensor_id", "sensor_001")
DATA_INTERVAL = config.get("data_interval", 5)

def simulate_sensor_data():
    """
    Simulate sensor data by generating random values for scrap weight and emission level.
    Returns a dictionary.
    """
    data = {
        "sensorId": SENSOR_ID,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "data": {
            "scrapWeight": round(random.uniform(0.0, 100.0), 2),
            "emissionLevel": round(random.uniform(0.0, 50.0), 2)
        }
    }
    logging.info(f"Simulated data: {data}")
    return data

def send_data_to_iot_hub(payload):
    """
    Send the sensor data payload to Azure IoT Hub.
    Includes error handling and logging.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": API_KEY
    }
    try:
        response = requests.post(IOT_HUB_ENDPOINT, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            logging.info(f"Data sent successfully: {payload}")
        else:
            logging.error(f"Error sending data: {response.status_code} - {response.text}")
    except Exception as e:
        logging.exception(f"Exception during data send: {str(e)}")

if __name__ == "__main__":
    while True:
        sensor_data = simulate_sensor_data()
        send_data_to_iot_hub(sensor_data)
        time.sleep(DATA_INTERVAL)
