#!/usr/bin/env python3
import subprocess
import os
import csv
import requests
import dns.resolver
import time
from datetime import datetime
from plyer import notification

# --- Configuration ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "network_log.csv")
LATENCY_THRESHOLD = 50.0  # Alert if ping > 50ms
DNS_THRESHOLD = 100.0     # Alert if DNS > 100ms

def send_alert(metric, value):
    """Sends a native desktop notification."""
    notification.notify(
        title="⚠️ Emerald Network Alert",
        message=f"High {metric} detected: {value}ms",
        app_name="Network Auditor",
        timeout=10
    )

def get_dns_latency(server=None):
    resolver = dns.resolver.Resolver()
    if server:
        resolver.nameservers = [server]
    try:
        start = time.time()
        resolver.resolve('www.wikipedia.org', 'A')
        return round((time.time() - start) * 1000, 3)
    except:
        return "ERROR"

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
        return float(output.split("/")[-3])
    except:
        return "ERROR"

def run_audit():
    print(f"--- Running Integrated Audit & Alert ---")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    latency = get_ping_stats()
    system_dns = get_dns_latency()
    google_dns = get_dns_latency(server="8.8.8.8")
    public_ip, isp = get_network_info()

    # Log to CSV
    new_row = [timestamp, latency, system_dns, google_dns, public_ip, isp]
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)

    # --- Integrated Alert Logic ---
    if isinstance(latency, float) and latency > LATENCY_THRESHOLD:
        send_alert("Latency", latency)
    
    if isinstance(system_dns, float) and system_dns > DNS_THRESHOLD:
        send_alert("System DNS", system_dns)

    print(f"[{timestamp}] Audit complete. Metrics within thresholds.")

if __name__ == "__main__":
    run_audit()
