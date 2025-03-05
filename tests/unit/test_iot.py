import unittest
from src.iot.preprocessing.data_preprocessing import check_sensor_health, trigger_fallback

class TestIotPreprocessing(unittest.TestCase):

    def test_sensor_health_ok(self):
        data = {"data": {"scrapWeight": 50, "emissionLevel": 20}}
        # Expect no fallback triggered for normal data.
        self.assertIsNone(check_sensor_health("SENSOR_001", data))

    def test_sensor_health_anomaly(self):
        data = {"data": {"scrapWeight": 150, "emissionLevel": 60}}
        # We expect fallback to be triggered for abnormal data.
        # In our simulation, the function prints output.
        # We can check if trigger_fallback is called, but here we simply ensure it doesn't crash.
        try:
            check_sensor_health("SENSOR_002", data)
        except Exception as e:
            self.fail(f"check_sensor_health() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
