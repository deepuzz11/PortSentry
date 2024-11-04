from flask import Flask, render_template, request, redirect, url_for, flash
import socket
from service_detection import detect_service
from os_fingerprinting import os_fingerprint
from report_generator import generate_report

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

def scan_port(ip, port):
    """Scans a single port on the target IP address to detect the service."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # 1 second timeout for the connection attempt
            result = sock.connect_ex((ip, port))

            if result == 0:
                service_name, version = detect_service(port)
                return (port, service_name, version)
            else:
                return (port, 'Closed', 'N/A')
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return (port, 'Error', 'N/A')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_ip = request.form['ip_address']
        ports = request.form.get('ports')  # Get list of ports from form
        
        try:
            ports = list(map(int, ports.split(',')))  # Convert port strings to integers
        except ValueError:
            flash('Please enter valid port numbers.')
            return redirect(url_for('index'))

        if not target_ip or not ports:
            flash('Please enter a valid IP address and select ports to scan.')
            return redirect(url_for('index'))

        service_results = []
        os_results = []

        for port in ports:
            port_info = scan_port(target_ip, port)
            service_results.append(port_info)

            detected_os = os_fingerprint(port_info[0], port_info[1])
            os_results.append((port_info[0], port_info[1], detected_os))

        # Generate the report
        report = generate_report(service_results, os_results)
        return render_template('report.html', report=report)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
