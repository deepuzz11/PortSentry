def os_fingerprint(port, service):
    """
    Attempts to identify the operating system based on the service running on the given port.
    
    Parameters:
        port (int): The port number that is open.
        service (str): The service name running on that port.

    Returns:
        str: A string representing the likely operating system.
    """
    if service == 'SSH':
        return 'Linux/Unix'
    elif service == 'HTTP' or service == 'HTTPS':
        return 'Web Server (varies)'
    elif service == 'FTP':
        return 'Linux/Unix or Windows'
    elif service == 'SMTP':
        return 'Mail Server (varies)'
    elif service == 'DNS':
        return 'Linux/Unix or Windows'
    elif service == 'MySQL':
        return 'Database Server (usually Linux/Unix)'
    elif service == 'Redis':
        return 'Database Server (Linux/Unix)'
    elif service == 'Telnet':
        return 'Older Systems (varies, often Linux/Unix)'
    elif service == 'RDP':
        return 'Windows'
    elif service == 'PostgreSQL':
        return 'Database Server (usually Linux/Unix)'
    # Add more known services and their corresponding OS here
    
    return 'Unknown OS'
