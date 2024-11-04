import json

def generate_report(open_ports, filename='scan_report.json'):
    """
    Generates a JSON report of the open ports, services, and OS.

    Parameters:
        open_ports (list): A list of tuples containing open port information.
        filename (str): The name of the file to save the report to.
    """
    report = {
        "open_ports": []
    }
    for port, service, os_name in open_ports:
        report["open_ports"].append({"port": port, "service": service, "os": os_name})

    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"Report generated: {filename}")
