def os_fingerprint(port, service):
    """
    Performs OS fingerprinting based on the service detected.

    Parameters:
        port (int): The port number.
        service (str): The detected service name.

    Returns:
        str: A string indicating the detected OS.
    """
    if service == 'SSH':
        return 'Linux/Unix'
    elif service == 'HTTP':
        return 'Web Server (varies)'
    elif service == 'FTP':
        return 'Linux/Unix'
    elif service == 'SMTP':
        return 'Linux/Unix or Windows'
    elif service == 'DNS':
        return 'Linux/Unix'
    elif service == 'MySQL':
        return 'Linux/Unix or Windows'
    elif service == 'PostgreSQL':
        return 'Linux/Unix'
    elif service == 'Redis':
        return 'Linux/Unix'
    elif service == 'Telnet':
        return 'Linux/Unix or Windows'
    elif service == 'RDP':
        return 'Windows'
    elif service == 'MongoDB':
        return 'Linux/Unix'
    return 'Unknown OS'
