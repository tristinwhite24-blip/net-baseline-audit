import subprocess
import os
import csv
from datetime import datetime

# 1. Setup paths so it's always in the right place
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "network_log.csv")

def get_ping_stats():
    """Run a ping and return the average latency."""
    try:
        # Run ping -c 3 (3 packets) and capture output
        output = subprocess.check_output(["ping", "-c", "3", "1.1.1.1"], text=True)
        # Extract the 'avg' RTT from the summary line
        avg_latency = output.split("/")[-3]
        return avg_latency
    except Exception:
        return "ERROR"

def run_audit():
    print(f"--- Starting Python Audit ---")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latency = get_ping_stats()

    # 2. Log to CSV (The 'Professional' way)
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        # Add headers if it's a brand new file
        if not file_exists:
            writer.writerow(["Timestamp", "Gateway_Latency_ms", "System_DNS_ms", "Google_DNS_ms"])
        
        # We'll log the latency and put 0/0 for DNS for now to match your format
        writer.writerow([timestamp, latency, 0, 0])

    print(f"Logged: {timestamp} | Latency: {latency}ms")

if __name__ == "__main__":
    run_audit()
