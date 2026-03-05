import csv
import time
import os
from plyer import notification

LOG_FILE = "network_log.csv"
LATENCY_THRESHOLD = 50.0  # Alert if ping > 50ms
DNS_THRESHOLD = 100.0      # Alert if DNS > 100ms

def check_for_issues():
    if not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, 'r') as f:
        reader = list(csv.reader(f))
        if len(reader) < 2: return
        
        # Get the very last entry
        last_row = reader[-1]
        try:
            timestamp = last_row[0]
            latency = float(last_row[1])
            sys_dns = float(last_row[2])
            
            # Logic: If things are slow, send a pop-up alert
            if latency > LATENCY_THRESHOLD or sys_dns > DNS_THRESHOLD:
                notification.notify(
                    title="⚠️ Network Alert: Eugene",
                    message=f"High Latency Detected!\nPing: {latency}ms\nDNS: {sys_dns}ms",
                    app_name="Emerald Auditor",
                    timeout=10
                )
                print(f"[{timestamp}] Alert Sent: High Latency detected.")
        except ValueError:
            # This handles 'N/A' or 'ERROR' strings in the CSV
            pass

if __name__ == "__main__":
    print("--- Emerald Alert Bot Active ---")
    while True:
        check_for_issues()
        time.sleep(60) # Checks the log every minute
