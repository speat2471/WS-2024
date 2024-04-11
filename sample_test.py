import requests

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    print("Product Names:", data.get("productNames"))  # Print out the productNames
    assert "productNames" in data
    # Add more assertions to check the structure and content of the response

def test_get_products(base_url):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    
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
