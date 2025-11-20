import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('items', response.json)
        self.assertEqual(response.json['items'], ["item1", "item2", "item3"])

    def test_is_return_list(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json['items'], list)

    def test_swagger_ui_accessible(self):
        response = self.client.get('/swagger/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Swagger UI', response.data)

if __name__ == '__main__':
    unittest.main()
