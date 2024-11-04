def generate_report(service_results, os_results):
    """
    Generates a report based on the scanned results.

    Parameters:
        service_results (list): A list of tuples containing port, service name, and version.
        os_results (list): A list of tuples containing port, service name, and detected OS.

    Returns:
        str: A formatted report string.
    """
    report_lines = []
    report_lines.append("Port Scan Report\n")
    report_lines.append("=" * 30 + "\n")

    report_lines.append("Service Detection Results:\n")
    report_lines.append("{:<10} {:<25} {:<20}\n".format("Port", "Service Name", "Version"))
    report_lines.append("=" * 60 + "\n")

    for port, service, version in service_results:
        report_lines.append("{:<10} {:<25} {:<20}\n".format(port, service, version))

    report_lines.append("\nOS Fingerprinting Results:\n")
    report_lines.append("{:<10} {:<25} {:<20}\n".format("Port", "Service Name", "Detected OS"))
    report_lines.append("=" * 60 + "\n")

    for port, service, detected_os in os_results:
        report_lines.append("{:<10} {:<25} {:<20}\n".format(port, service, detected_os))

    return ''.join(report_lines)
