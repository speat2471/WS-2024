import requests

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    if response.status_code == 200:
        print("Test for getTitles passed")
    else:
        print("Test for getTitles failed")

    assert response.status_code == 200
    data = response.json()
    print("Product Names:", data.get("productNames"))  # Print out the productNames
    assert "productNames" in data
    
def test_add_product(base_url):
    url = f"{base_url}/insertProducts?api_key=letmein"
    product_data = {
        "id": "123",
        "name": "Sample Product",
        "cost": 10.99
    }
    response = requests.post(url, json=product_data)
    if response.status_code == 201:
        print("Test for insertProducts passed")
    else:
        print("Test for insertProducts failed")
    
# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_add_product(base_url)
    test_get_titles(base_url)
    print("Process completed and ready for the customer")
