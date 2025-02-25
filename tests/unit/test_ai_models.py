import unittest
import numpy as np
from analytics.ai_models.predictive_model import PredictiveModel

class TestAIPredictiveModel(unittest.TestCase):
    def setUp(self):
        # Assuming a pre-trained model exists at the specified path
        self.model = PredictiveModel("analytics/ai_models/model.pkl")
    
    def test_predict(self):
        sample_features = np.array([50.0, 20.0, 30.0])
        prediction = self.model.predict(sample_features)
        self.assertIn("scrapForecast", prediction)
        self.assertIn("emissionForecast", prediction)

if __name__ == "__main__":
    unittest.main()
