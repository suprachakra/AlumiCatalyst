import json
import time
import random
import requests

# Load sensor configuration
with open('sensor_config.json', 'r') as config_file:
    config = json.load(config_file)

IOT_HUB_ENDPOINT = config.get("iot_hub_endpoint", "https://example-iothub.azure-devices.net/messages/events")
API_KEY = config.get("api_key", "YOUR_API_KEY_HERE")
SENSOR_ID = config.get("sensor_id", "sensor_001")

def simulate_sensor_data():
    """
    Simulate sensor data by generating random values for scrap weight and emission level.
    """
    data = {
        "sensorId": SENSOR_ID,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "data": {
            "scrapWeight": round(random.uniform(0.0, 100.0), 2),
            "emissionLevel": round(random.uniform(0.0, 50.0), 2)
        }
    }
    return data

def send_data_to_iot_hub(payload):
    """
    Send the sensor data payload to the IoT Hub.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": API_KEY
    }
    response = requests.post(IOT_HUB_ENDPOINT, headers=headers, json=payload)
    if response.status_code == 200:
        print("Data sent successfully:", payload)
    else:
        print("Error sending data:", response.status_code, response.text)

if __name__ == "__main__":
    while True:
        sensor_data = simulate_sensor_data()
        send_data_to_iot_hub(sensor_data)
        time.sleep(config.get("data_interval", 5))
