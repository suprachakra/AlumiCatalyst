import unittest
import requests

class TestIntegrationBlockchain(unittest.TestCase):
    BASE_URL = "http://localhost:5000/api/v1"

    def test_blockchain_trace(self):
        # Assuming an event with transactionId=1 exists in the blockchain ledger
        url = f"{self.BASE_URL}/blockchain/trace?transactionId=1"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("transactionId", data)

if __name__ == "__main__":
    unittest.main()
