import subprocess
import time
import socket

def check_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} on {host} is open")
    else:
        print(f"Port {port} on {host} is closed")
    sock.close()

def ping_url(url):
    start_time = time.time()
    result = subprocess.run(["ping", "-c", "4", url], capture_output=True, text=True)
    end_time = time.time()
    print(f"Ping to {url} took {end_time - start_time:.2f} seconds")
    print(result.stdout)

if __name__ == "__main__":
    base_url = "127.0.0.1"  # Update with your base URL
    ports_to_check = [8081, 27017]  # Add ports you want to check

    # Check if ports are open
    print("Checking port status:")
    for port in ports_to_check:
        check_port_open(base_url, port)

    # Ping the base URL
    print("\nPinging the base URL:")
    ping_url(base_url)

    print("Process completed and ready for the customer")
