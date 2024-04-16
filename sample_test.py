import requests

def test_root(base_url):
    url = f"{base_url}/"
    response = requests.get(url)
    print("Root URL test:")
    if response.status_code == 200:
        print("PASS")
    else:
        print("FAIL")

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    print("\ngetTitles test:")
    if response.status_code == 200:
        print("PASS")
    else:
        print("FAIL")

    data = response.json()
    print("Product Names:", data.get("productNames"))  # Print out the productNames
    assert "productNames" in data

def test_get_products(base_url):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    print("\ngetProducts test:")
    if response.status_code == 200:
        print("PASS")
    else:
        print("FAIL")

    data = response.json()
    print("Products:", data)  # Print out the products
    assert isinstance(data, list)  # Ensure the response is a list

    # Check each product in the list
    for product in data:
        assert "name" in product
        assert "cost" in product
        assert ("id" in product) or ("_id" in product)  # Check for either "id" or "_id" field

def test_insert_product(base_url):
    url = f"{base_url}/insertProducts?api_key=letmein"
    product = {
        "id": "123",
        "name": "Test Product",
        "cost": 10.99
    }
    response = requests.post(url, json=product)
    print("\ninsertProducts test:")
    if response.status_code == 201:
        print("PASS")
    else:
        print("FAIL")

# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_root(base_url)
    test_get_titles(base_url)
    test_get_products(base_url)
    test_insert_product(base_url)
