import socket
from concurrent.futures import ThreadPoolExecutor
from service_detection import get_service_name
from os_fingerprinting import os_fingerprint
from report_generator import generate_report

def scan_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            service = get_service_name(port)
            os_name = os_fingerprint(port, service)
            return port, service, os_name  # Return port, service, and OS
        return None  # Port is closed

def scan_ports(host, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, host, port): port for port in range(start_port, end_port + 1)}
        for future in futures:
            port_info = future.result()
            if port_info is not None:
                open_ports.append(port_info)
    return open_ports

if __name__ == '__main__':
    target_host = input("Enter the target host (IP or domain): ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    print(f"Scanning {target_host} from port {start_port} to {end_port}...")
    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print("Open ports, services, and OS:")
        for port, service, os_name in open_ports:
            print(f"Port: {port}, Service: {service}, OS: {os_name}")
        
        # Generate a report
        generate_report(open_ports)
    else:
        print("No open ports found.")
