import socket
import requests

def detect_service(port):
    """
    Returns the service name and version associated with a given port number.
    
    Parameters:
        port (int): The port number.

    Returns:
        tuple: The name of the service running on the port and its version.
    """
    services = {
        22: ('SSH', 'OpenSSH'),          # SSH Service
        23: ('Telnet', 'varies'),        # Telnet Service
        25: ('SMTP', 'varies'),          # Simple Mail Transfer Protocol
        53: ('DNS', 'varies'),           # Domain Name System
        67: ('DHCP', 'varies'),          # Dynamic Host Configuration Protocol
        68: ('DHCP', 'varies'),          # DHCP Client
        80: ('HTTP', 'varies'),          # Hypertext Transfer Protocol
        110: ('POP3', 'varies'),         # Post Office Protocol
        143: ('IMAP', 'varies'),         # Internet Message Access Protocol
        443: ('HTTPS', 'varies'),        # HTTP Secure
        993: ('IMAPS', 'varies'),        # IMAP over SSL
        995: ('POP3S', 'varies'),        # POP3 over SSL
        21: ('FTP', 'varies'),           # File Transfer Protocol
        69: ('TFTP', 'varies'),          # Trivial File Transfer Protocol
        3306: ('MySQL', 'varies'),       # MySQL Database Server
        5432: ('PostgreSQL', 'varies'),  # PostgreSQL Database Server
        6379: ('Redis', 'varies'),       # Redis Key-Value Store
        27017: ('MongoDB', 'varies'),    # MongoDB Database Server
        3389: ('RDP', 'varies'),         # Remote Desktop Protocol
        8080: ('HTTP Alt', 'varies'),    # Alternative HTTP port
        5000: ('Flask', 'varies'),       # Flask Development Server (often used for web apps)
        8000: ('HTTP Alt', 'varies'),    # Another alternative HTTP port
        9200: ('Elasticsearch', 'varies'), # Elasticsearch REST API
        27018: ('MongoDB', 'varies'),    # MongoDB Secondary
        # Add more known services here...
    }

    service_name, default_version = services.get(port, ('Unknown Service', 'N/A'))

    # If the service is HTTP or HTTPS, try to get the version from the server
    if service_name in ['HTTP', 'HTTPS']:
        try:
            protocol = 'https' if service_name == 'HTTPS' else 'http'
            response = requests.get(f'{protocol}://localhost:{port}', timeout=1)
            server = response.headers.get('Server', 'Unknown Version')
            return service_name, server  # Return service name and detected version
        except requests.RequestException:
            return service_name, default_version  # Return service info even if the request fails

    return service_name, default_version  # Return service name and default version if no version detection is performed

# if __name__ == '__main__':
#     # Sample usage for testing
#     test_ports = [22, 23, 25, 53, 80, 443, 3306, 5432, 6379, 8080, 27017]
#     for port in test_ports:
#         service, version = get_service_info(port)
#         print(f"Port: {port}, Service: {service}, Version: {version}")
