import unittest
from src.iot.sensor_ingestion import iot_sensor_integration

class TestIotSensorIntegration(unittest.TestCase):
    def test_simulate_sensor_data(self):
        data = iot_sensor_integration.simulate_sensor_data()
        self.assertIn("sensorId", data)
        self.assertIn("timestamp", data)
        self.assertIn("data", data)
    
    def test_send_data_to_iot_hub_invalid(self):
        # Placeholder test; in practice, use mocking for requests.post
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
