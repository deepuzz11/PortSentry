def get_service_name(port):
    """
    Returns the service name associated with a given port number.
    
    Parameters:
        port (int): The port number.

    Returns:
        str: The name of the service running on the port, or 'Unknown Service' if not recognized.
    """
    services = {
        22: 'SSH',
        80: 'HTTP',
        443: 'HTTPS',
        21: 'FTP',
        25: 'SMTP',
        53: 'DNS',
        3306: 'MySQL',
        6379: 'Redis',
        23: 'Telnet',
        3389: 'RDP',
        5432: 'PostgreSQL',
        # Add more known services here
    }
    return services.get(port, 'Unknown Service')
