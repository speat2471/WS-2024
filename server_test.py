import requests
import socket
import subprocess
import time
import pymongo

# Function to ping URLs
def test_ping_urls(urls):
    results = {}
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results[url] = "PASS"
            else:
                results[url] = "FAIL"
        except requests.exceptions.RequestException:
            results[url] = "FAIL (Connection Error)"
    return results

# Function to ping URLs with variables
def test_ping_urls_with_vars(base_url, variables):
    results = {}
    for var in variables:
        url = f"{base_url}/{var}"
        results[url] = test_ping_urls([url])
    return results

# Function to check if ports are open
def test_ports_open(ports):
    results = {}
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(("localhost", port))
            if result == 0:
                results[f"Port {port}"] = "PASS"
            else:
                results[f"Port {port}"] = "FAIL"
    return results

# Function to check if ports are closed
def test_ports_closed(ports):
    results = {}
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(("localhost", port))
            if result != 0:
                results[f"Port {port}"] = "PASS"
            else:
                results[f"Port {port}"] = "FAIL"
    return results

# Function to test Flask app to DB connection
def test_flask_app_db_connection():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client.test_database
        db.test_collection.insert_one({"test_key": "test_value"})
        return "PASS"
    except Exception as e:
        return f"FAIL ({str(e)})"

# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    urls = [f"{base_url}/endpoint1", f"{base_url}/endpoint2"]
    variables = ["var1", "var2"]
    ports_to_check = [80, 443, 27017]  # Example ports to check

    # Run tests and write results to log file
    with open("test_results.log", "w") as f:
        # Ping URLs
        f.write("Ping URLs:\n")
        results = test_ping_urls(urls)
        for url, result in results.items():
            f.write(f"{url}: {result}\n")

        # Ping URLs with variables
        f.write("\nPing URLs with variables:\n")
        results = test_ping_urls_with_vars(base_url, variables)
        for url, inner_results in results.items():
            f.write(f"{url}:\n")
            for inner_url, inner_result in inner_results.items():
                f.write(f"\t{inner_url}: {inner_result}\n")

        # Check if ports are open
        f.write("\nCheck if ports are open:\n")
        results = test_ports_open(ports_to_check)
        for port, result in results.items():
            f.write(f"{port}: {result}\n")

        # Check if ports are closed
        f.write("\nCheck if ports are closed:\n")
        results = test_ports_closed(ports_to_check)
        for port, result in results.items():
            f.write(f"{port}: {result}\n")

        # Test Flask app to DB connection
        f.write("\nTest Flask app to DB connection:\n")
        result = test_flask_app_db_connection()
        f.write(f"{result}\n")

    print("Process completed and ready for the customer")
