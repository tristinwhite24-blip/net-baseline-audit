#!/usr/bin/env python3
import subprocess
import os
import csv
import requests
import dns.resolver
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "network_log.csv")

def get_dns_latency(server=None):
    """Query a specific DNS server and return the time in ms."""
    resolver = dns.resolver.Resolver()
    if server:
        resolver.nameservers = [server]
    
    import time
    try:
        start = time.time()
        # Using a fresh random-ish domain to avoid ISP-side caching
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
        return output.split("/")[-3]
    except:
        return "ERROR"

def run_audit():
    print(f"--- Running Direct-Query DNS Audit ---")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    latency = get_ping_stats()
    # Query 1: Default (System/Emerald)
    system_dns = get_dns_latency()
    # Query 2: Explicitly Google (8.8.8.8)
    google_dns = get_dns_latency(server="8.8.8.8")
    
    public_ip, isp = get_network_info()
    new_row = [timestamp, latency, system_dns, google_dns, public_ip, isp]

    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)

    print(f"[{timestamp}] System DNS: {system_dns}ms | Google DNS: {google_dns}ms")

if __name__ == "__main__":
    run_audit()
