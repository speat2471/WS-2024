import requests

def test_get_titles(base_url, log_file):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    if response.status_code == 200:
        log_file.write("Test passed: /getTitles\n")
    else:
        log_file.write("Test failed: /getTitles\n")

    assert response.status_code == 200
    data = response.json()
    assert "productNames" in data

def test_get_products(base_url, log_file):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    if response.status_code == 200:
        log_file.write("Test passed: /getProducts\n")
    else:
        log_file.write("Test failed: /getProducts\n")

    assert response.status_code == 200

def test_insert_product(base_url, log_file):
    url = f"{base_url}/insertProduct"
    product_data = {
        "id": "123",
        "name": "Test Product",
        "cost": 10.99
    }
    headers = {"api_key": "letmein"}
    response = requests.post(url, json=product_data, headers=headers)
    if response.status_code == 201:
        log_file.write("Test passed: /insertProduct\n")
    else:
        log_file.write("Test failed: /insertProduct\n")

    assert response.status_code == 201

def test_root_url(base_url, log_file):
    url = f"{base_url}/"
    response = requests.get(url)
    if response.status_code == 200:
        log_file.write("Test passed: / (Root URL)\n")
    else:
        log_file.write("Test failed: / (Root URL)\n")

    assert response.status_code == 200

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    log_file_path = "test_results.log"
    with open(log_file_path, "w") as log_file:
        test_get_titles(base_url, log_file)
        test_get_products(base_url, log_file)
        test_insert_product(base_url, log_file)
        test_root_url(base_url, log_file)
        print("Process completed and ready for the customer")
