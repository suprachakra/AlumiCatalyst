import json
import pandas as pd
import time
import requests

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
    Monitor sensor data for anomalies based on thresholds.
    If thresholds are exceeded, trigger fallback procedures.
    """
    # Check for abnormal scrap weight or emission level values
    if (data["data"]["scrapWeight"] > config.get("max_scrapWeight", 100) or
        data["data"]["emissionLevel"] > config.get("max_emissionLevel", 50)):
        print(f"⚠️ Sensor {sensor_id} reporting abnormal data. Triggering fallback...")
        trigger_fallback(sensor_id)
    else:
        print(f"✅ Sensor {sensor_id} is healthy.")

def trigger_fallback(sensor_id: str):
    """
    Trigger fallback procedures by notifying the Incident Response system.
    """
    fallback_message = {"sensor_id": sensor_id, "issue": "Sensor anomaly detected."}
    print("Fallback activated:", fallback_message)
    try:
        response = requests.post("http://incident-handler/api/report", json=fallback_message)
        if response.status_code == 200:
            print("Incident reported successfully.")
        else:
            print("Error reporting incident:", response.status_code)
    except Exception as e:
        print("Exception while reporting incident:", str(e))

def preprocess_data(data: dict) -> dict:
    """
    Preprocess sensor data:
    - Check sensor health.
    - Convert timestamp to datetime.
    - Normalize numerical values.
    """
    sensor_id = data.get("sensorId", "Unknown")
    check_sensor_health(sensor_id, data)
    
    # Convert timestamp to pandas datetime
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    # Normalize values
    data["data"]["scrapWeight"] = float(data["data"].get("scrapWeight", 0.0))
    data["data"]["emissionLevel"] = float(data["data"].get("emissionLevel", 0.0))
    
    return data

if __name__ == "__main__":
    # Load and process a sample sensor data file
    sample_data = load_sensor_data("sample_sensor_data.json")
    processed_data = preprocess_data(sample_data)
    print("Processed Data:", processed_data)
    time.sleep(2)
