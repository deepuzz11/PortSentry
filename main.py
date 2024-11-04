import socket
from concurrent.futures import ThreadPoolExecutor

# Function to check if a port is open
def scan_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Set a timeout for the connection
        result = sock.connect_ex((host, port))  # Try to connect to the port
        if result == 0:
            return port  # Port is open
        return None  # Port is closed

# Function to scan a range of ports
def scan_ports(host, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:  # Use threads for faster scanning
        futures = {executor.submit(scan_port, host, port): port for port in range(start_port, end_port + 1)}
        for future in futures:
            port = future.result()
            if port is not None:
                open_ports.append(port)
    return open_ports

# Main function to execute the port scan
if __name__ == '__main__':
    target_host = input("Enter the target host (IP or domain): ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    print(f"Scanning {target_host} from port {start_port} to {end_port}...")
    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")
