import subprocess
import os
import csv
import requests
import socket
import time
from datetime import datetime

# 1. Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "network_log.csv")

def get_dns_latency(domain="google.com"):
    """Measure how long it takes to resolve a domain name in milliseconds."""
    try:
        start_time = time.time()
        socket.gethostbyname(domain)
        end_time = time.time()
        # Convert to milliseconds
        return round((end_time - start_time) * 1000, 3)
    except:
        return "ERROR"

def get_network_info():
    """Fetch Public IP and ISP info via API."""
    try:
        response = requests.get('http://ip-api.com/json/', timeout=5)
        data = response.json()
        if data['status'] == 'success':
            # Remove comma from ISP name for CSV safety
            return data['query'], data['isp'].replace(",", "")
    except:
        pass
    return "N/A", "N/A"

def get_ping_stats():
    """Run a ping and return the average latency."""
    try:
        output = subprocess.check_output(["ping", "-c", "3", "1.1.1.1"], text=True)
        return output.split("/")[-3]
    except:
        return "ERROR"

def run_audit():
    print(f"--- Running Full Python Network Audit ---")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Capture ALL Metrics
    latency = get_ping_stats()
    system_dns = get_dns_latency()      # Uses your local/ISP DNS
    google_dns = get_dns_latency()      # Second check (acts as a 'Google' check)
    public_ip, isp = get_network_info()

    # 3. The Master Format: TS, Lat, DNS_Sys, DNS_Goo, IP, ISP
    new_row = [timestamp, latency, system_dns, google_dns, public_ip, isp]

    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)

    print(f"[{timestamp}] SUCCESS")
    print(f"Latency: {latency}ms | DNS: {system_dns}ms | ISP: {isp}")

if __name__ == "__main__":
    run_audit()
