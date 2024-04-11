import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL

    def test_get_titles(self):
        url = f"{self.base_url}/getTitles"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        data = response.json()
        self.assertIn("productNames", data)  # Check if the expected key is present in the response
        # Add more assertions to check the structure and content of the response if needed

    def test_get_products(self):
        url = f"{self.base_url}/getProducts"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        # Add assertions to check the content and structure of the response

    def test_insert_product(self):
        url = f"{self.base_url}/insertProduct"
        # Example payload for inserting a product
        payload = {
            "id": "123",
            "name": "Test Product",
            "cost": 10.99
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 201)
        # Optionally, check if the product is actually inserted into the database

if __name__ == "__main__":
    unittest.main()
