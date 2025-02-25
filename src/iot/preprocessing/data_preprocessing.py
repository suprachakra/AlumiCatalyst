import json
import pandas as pd

def load_sensor_data(file_path):
    """
    Load raw sensor data from a JSON file.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def preprocess_data(data):
    """
    Preprocess the sensor data:
    - Convert timestamp strings to datetime objects.
    - Ensure numerical values for scrap weight and emission level.
    """
    # Convert timestamp to pandas datetime
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    # Ensure numerical conversion with default values if missing
    data["data"]["scrapWeight"] = float(data["data"].get("scrapWeight", 0.0))
    data["data"]["emissionLevel"] = float(data["data"].get("emissionLevel", 0.0))
    # Additional cleaning logic can be added here
    return data

if __name__ == "__main__":
    sample_file = 'sample_sensor_data.json'
    raw_data = load_sensor_data(sample_file)
    clean_data = preprocess_data(raw_data)
    print("Processed Data:", clean_data)
