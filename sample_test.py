import requests

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()
    assert "productNames" in data
    product_names = data.get("productNames")
    assert isinstance(product_names, list)
    assert all(isinstance(name, str) for name in product_names)
    
    print("Test passed")
    print("Product Names:", product_names)
    
# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_get_titles(base_url)
    print("Process completed and ready for the customer")
