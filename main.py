import socket
from service_detection import detect_service
from os_fingerprinting import os_fingerprint
from report_generator import generate_report

def scan_port(ip, port):
    """Scans a single port on the target IP address to detect the service."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))

            if result == 0:
                service_name, version = detect_service(port)
                return (port, service_name, version)
            else:
                return (port, 'Closed', 'N/A')
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return (port, 'Error', 'N/A')

def main(target_ip, ports):
    service_results = []
    os_results = []

    for port in ports:
        port_info = scan_port(target_ip, port)
        service_results.append(port_info)

        detected_os = os_fingerprint(port_info[0], port_info[1])
        os_results.append((port_info[0], port_info[1], detected_os))

    report = generate_report(service_results, os_results)
    print(report)

# if __name__ == '__main__':
#     target_ip = '192.168.1.1'  # Replace with the target IP address
#     ports_to_scan = [22, 80, 443, 21, 25, 53, 3306, 5432, 6379, 23, 3389, 27017]
    
#     main(target_ip, ports_to_scan)
