import subprocess
import os
import csv
import requests
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "network_log.csv")

def get_network_info():
    try:
        response = requests.get('http://ip-api.com/json/', timeout=5)
        data = response.json()
        if data['status'] == 'success':
            return data['query'], data['isp'].replace(",", "")
    except:
        pass
    return "N/A", "N/A"

def get_ping_stats():
    try:
        output = subprocess.check_output(["ping", "-c", "3", "1.1.1.1"], text=True)
        return output.split("/")[-3]
    except:
        return "ERROR"

def run_audit():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latency = get_ping_stats()
    public_ip, isp = get_network_info()

    # The Master Format: TS, Lat, DNS_Sys, DNS_Goo, IP, ISP
    # We use "N/A" for the old DNS columns since Python isn't tracking those right now
    new_row = [timestamp, latency, "N/A", "N/A", public_ip, isp]

    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)

    print(f"[{timestamp}] Logged to Master CSV | Latency: {latency}ms")

if __name__ == "__main__":
    run_audit()
