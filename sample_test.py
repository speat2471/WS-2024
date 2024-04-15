import requests

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "productNames" in data
    # Add more assertions to check the structure and content of the response

def test_get_products(base_url):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    assert response.status_code == 200
    # Add assertions to check the content and structure of the response

def test_invalid_api_key(base_url):
    url = f"{base_url}/insertProduct"
    product = {
        "id": "123",
        "name": "Test Product",
        "cost": 10.99
    }
    headers = {"api_key": "invalid_key"}
    response = requests.post(url, json=product, headers=headers)
    assert response.status_code == 401
    # Check if the response indicates that the API key is invalid

def test_missing_data(base_url):
    url = f"{base_url}/insertProduct"
    product = {
        "name": "Test Product",
        "cost": 10.99
    }
    headers = {"api_key": "letmein"}
    response = requests.post(url, json=product, headers=headers)
    assert response.status_code == 400
    # Check if the response indicates that required data is missing

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_get_titles(base_url)
    test_get_products(base_url)
    test_invalid_api_key(base_url)
    test_missing_data(base_url)
