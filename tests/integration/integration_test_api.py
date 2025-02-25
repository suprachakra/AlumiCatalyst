import unittest
import requests

class TestIntegrationAPI(unittest.TestCase):
    BASE_URL = "http://localhost:5000/api/v1"

    def test_sensor_data_ingestion(self):
        url = f"{self.BASE_URL}/iot/sensors"
        payload = {
            "sensorId": "sensor_test",
            "timestamp": "2023-01-01T00:00:00Z",
            "data": {
                "scrapWeight": 50.5,
                "emissionLevel": 20.0
            }
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
