import subprocess
import os
import csv
import requests
from datetime import datetime

# 1. Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "network_log.csv")

def get_network_info():
    """Fetch Public IP and ISP info via API."""
    try:
        response = requests.get('http://ip-api.com/json/', timeout=5)
        data = response.json()
        if data['status'] == 'success':
            return data['query'], data['isp']
    except:
        pass
    return "Unknown", "Unknown"

def get_ping_stats():
    """Run a ping and return the average latency."""
    try:
        output = subprocess.check_output(["ping", "-c", "3", "1.1.1.1"], text=True)
        return output.split("/")[-3]
    except:
        return "ERROR"

def run_audit():
    print(f"--- Running Combined Emerald Audit ---")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Capture everything
    latency = get_ping_stats()
    public_ip, isp = get_network_info()

    # Log to CSV
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Latency_ms", "Public_IP", "ISP"])
        writer.writerow([timestamp, latency, public_ip, isp])

    print(f"[{timestamp}] Latency: {latency}ms | ISP: {isp}")

if __name__ == "__main__":
    run_audit()
