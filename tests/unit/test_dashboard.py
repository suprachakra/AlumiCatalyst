import unittest
from dashboard.backend import dashboard_backend

class TestDashboardBackend(unittest.TestCase):
    def setUp(self):
        dashboard_backend.app.config['TESTING'] = True
        self.app = dashboard_backend.app.test_client()
    
    def test_get_metrics(self):
        response = self.app.get('/api/v1/dashboard/metrics')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("metrics", data)

if __name__ == "__main__":
    unittest.main()
