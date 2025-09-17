import unittest
from functions.app import app

class TestShelfSense(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.app.app.testing = True

    def test_add_stock(self):
        response = self.client.post('/stock', json={'item': 'Toyota Camry', 'quantity': 5})
        self.assertEqual(response.status_code, 200)

    def test_get_stock(self):
        response = self.client.get('/stock')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()