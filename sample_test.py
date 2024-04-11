import requests

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    print("Product Names:", data.get("productNames"))  # Print out the productNames
    assert "productNames" in data
    # Add more assertions to check the structure and content of the response
 if response.status_code == 200:
        print("Test passed")
    else:
        print("Test failed")

# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_get_titles(base_url)
    test_get_products(base_url)
    stop_servers()
    print("Process completed and ready for the customer")
