import requests

# Test for '/getTitles' endpoint
def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "productNames" in data
    # Add more assertions to check the structure and content of the response
    expected_names = ["eggs", "bread", "Coffee beans"]  # Update with your expected product names
    assert data["productNames"] == expected_names

# Test for '/getProducts' endpoint
def test_get_products(base_url):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    # Add assertions to check the content and structure of the response
    assert len(data) == 3  # Assuming there are 3 products in the database
    # Define your expected data here
    expected_data = [
        {"id": "", "name": "eggs", "cost": 2.99},
        {"id": "", "name": "bread", "cost": 1.99},
        {"id": "1", "name": "Coffee Beans", "cost": 7.99}
    ]
    assert data == expected_data

# Function to stop the servers
def stop_servers():
    # Add code to stop your servers here
    print("Servers stopped")

# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_get_titles(base_url)
    test_get_products(base_url)
    stop_servers()
    print("Process completed and ready for the customer")
