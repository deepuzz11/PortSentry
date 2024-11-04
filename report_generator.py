# report_generator.py

def generate_report(service_results, os_results):
    """Generates a report from the scanned results."""
    report = {
        'service_results': service_results,
        'os_results': os_results
    }
    return report
