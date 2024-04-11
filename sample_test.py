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

def test_get_titles_returns_expected_data(base_url):
    url = f"{base_url}/getTitles"
    expected_data = {"productNames": ["Product 1", "Product 2", "Product 3"]}  # Define your expected data here
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == expected_data

def test_get_products_returns_expected_data(base_url):
    url = f"{base_url}/getProducts"
    # Define your expected data here
    expected_data = [
        {"id": "1", "name": "Product 1", "cost": 10.99},
        {"id": "2", "name": "Product 2", "cost": 20.99},
        {"id": "3", "name": "Product 3", "cost": 30.99}
    ]
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == expected_data

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_get_titles(base_url)
    test_get_products(base_url)
    test_get_titles_returns_expected_data(base_url)
    test_get_products_returns_expected_data(base_url)
