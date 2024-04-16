import requests

def test_get_products(base_url):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    print("Products:", data)  # Print out the products
    assert isinstance(data, list)  # Ensure the response is a list

    # Check each product in the list
    for product in data:
        assert "name" in product
        assert "cost" in product
        assert ("id" in product) or ("_id" in product)  # Check for either "id" or "_id" field

    print("Test passed")

# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_get_products(base_url)
    print("Process completed and ready for the customer")
