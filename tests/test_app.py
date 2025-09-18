import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    from functions.app import app
except ImportError as e:
    print(f"ImportError: {e}")
    raise

class TestShelfSense(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.testing = True

    def test_add_stock(self):
        response = self.client.post('/stock', json={'item': 'Toyota Camry', 'quantity': 5})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Added 5 of Toyota Camry', response.data)

    def test_get_stock(self):
        response = self.client.get('/stock')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
