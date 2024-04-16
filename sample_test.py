import requests

def test_root(base_url):
    url = f"{base_url}/"
    response = requests.get(url)
    result = "PASS" if response.status_code == 200 else "FAIL"
    return url, result

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    result = "PASS" if response.status_code == 200 else "FAIL"
    return url, result

def test_get_products(base_url):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    result = "PASS" if response.status_code == 200 else "FAIL"
    return url, result

def test_insert_product(base_url):
    url = f"{base_url}/insertProducts?api_key=letmein"
    product = {
        "id": "123",
        "name": "Test Product",
        "cost": 10.99
    }
    response = requests.post(url, json=product)
    result = "PASS" if response.status_code == 201 else "FAIL"
    return url, result

# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL

    # Run tests and collect results
    results = []
    results.append(test_root(base_url))
    results.append(test_get_titles(base_url))
    results.append(test_get_products(base_url))
    results.append(test_insert_product(base_url))

    # Write results to log file
    with open("test_results.log", "w") as f:
        for url, result in results:
            f.write(f"{url}: {result}\n")

    print("Process completed and ready for the customer")
