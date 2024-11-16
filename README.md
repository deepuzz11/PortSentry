
# PortSentry

**PortSentry** is a powerful Python-based tool that scans target hosts for open ports to identify potential security vulnerabilities. This web application provides detailed scan reports, offering insights into service results and operating system (OS) detections based on scan data.

## Overview

PortSentry utilizes **Flask** as the backend framework and leverages **HTML** and **CSS** for front-end display. The application is designed to be user-friendly and responsive, making it accessible on various devices.

## Features

- **Service Results Table**: 
    - Displays a list of scanned ports, associated service names, and their versions.
  
- **OS Results Table**: 
    - Shows detected operating systems along with the scanned ports and services.
  
- **User-Friendly Interface**: 
    - Clean and simple design for easy navigation and understanding.
  
- **Responsive Design**: 
    - Adapts to different screen sizes for usability on various devices.

## Installation

To set up the project, follow these steps:

### Prerequisites

- Python 3.6 or later
- pip (Python package installer)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/PortSentry.git
    cd PortSentry
    ```

2. **Set up a virtual environment (optional)**:
    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Access the web application through your browser at the provided URL (e.g., `http://127.0.0.1:5000`).
2. Input the target IP address and specify the ports you want to scan.
3. View the results displayed in tables for services and operating systems.

## File Structure

```
PortSentry/
│
├── app.py                    # Main application file that runs the Flask server.
├── main.py                   # Entry point for port scanning functionality.
├── os_fingerprinting.py      # Module for OS detection based on open ports.
├── report_generator.py       # Generates reports from scan results.
├── service_detection.py      # Handles service detection on scanned ports.
│
├── static/
│   ├── script.js             # JavaScript file for frontend interactivity.
│   └── styles.css            # CSS file for styling the web application.
│
└── templates/
    ├── index.html            # Main HTML file for user input.
    └── report.html           # HTML file to display scan results.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
