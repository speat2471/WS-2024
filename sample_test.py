import requests

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    if response.status_code == 200:
        print("Test passed")
    else:
        print("Test failed")

    assert response.status_code == 200
    data = response.json()
    print("Product Names:", data.get("productNames"))  # Print out the productNames
    assert "productNames" in data
    
def test_get_products(base_url):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    if response.status_code == 200:
        print("Test passed")
    else:
        print("Test failed")

    assert response.status_code == 200
    data = response.json()
    print("Products:", data)  # Print out the products
    # Add assertions to check the content and structure of the response
    assert isinstance(data, list)  # Ensure the response is a list
    for product in data:
        assert "_id" in product
        assert "id" in product
        assert "name" in product
        assert "cost" in product
    
# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_get_titles(base_url)
    test_get_products(base_url)
    print("Process completed and ready for the customer")
