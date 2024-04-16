import requests
import socket
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

# Function to close ports
def close_ports(ports):
    for port in ports:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"])
        subprocess.run(["sudo", "iptables", "-A", "OUTPUT", "-p", "tcp", "--sport", str(port), "-j", "DROP"])

# Main function to run tests
if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Update with your actual base URL
    urls = [f"{base_url}/endpoint1", f"{base_url}/endpoint2"]
    ports_to_check = [27017, 8081]  # MongoDB and additional port

    # Run tests and write results to log file
    with open("test_results.log", "w") as f:
        # Ping URLs
        f.write("Ping URLs:\n")
        results = test_ping_urls(urls)
        for url, result in results.items():
            f.write(f"{url}: {result}\n")

        # Check if ports are open
        f.write("\nCheck if ports are open:\n")
        results = test_ports_open(ports_to_check)
        for port, result in results.items():
            f.write(f"{port}: {result}\n")

        # Close ports
        f.write("\nClosing ports:\n")
        close_ports(ports_to_check)

        # Check if ports are closed after closing
        f.write("\nCheck if ports are closed after closing:\n")
        results = test_ports_closed(ports_to_check)
        for port, result in results.items():
            f.write(f"{port}: {result}\n")

    print("Process completed and ready for the customer")
