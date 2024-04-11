import requests

def test_get_titles(base_url):
    url = f"{base_url}/getTitles"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "productNames" in data
    # Add more assertions to check the structure and content of the response

def test_get_products(base_url):
    url = f"{base_url}/getProducts"
    response = requests.get(url)
    assert response.status_code == 200
    # Add assertions to check the content and structure of the response

#def test_insert_product(base_url):
    #url = f"{base_url}/insertProduct?api_key=letmein"
    #payload = {
      #  "id": "123",
      #  "name": "Test Product",
      #  "cost": 10.99
  #  }
  #  response = requests.post(url, json=payload)
   # assert response.status_code == 201
    # Optionally, check if the product is actually inserted into the database

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    test_get_titles(base_url)
    test_get_products(base_url)
  #  test_insert_product(base_url)
