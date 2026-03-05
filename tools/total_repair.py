import csv
import os

file_path = 'network_log.csv'
temp_file = 'network_log_fixed.csv'
# 1. Define the 100% Correct Headers
headers = ["Timestamp", "Gateway_Latency_ms", "System_DNS_ms", "Google_DNS_ms", "Public_IP", "ISP"]

def repair():
    with open(file_path, 'r') as f_in, open(temp_file, 'w', newline='') as f_out:
        # We use a custom quotechar to handle those Emerald Broadband quotes
        reader = csv.reader(f_in, skipinitialspace=True)
        writer = csv.writer(f_out)
        
        # Write the correct headers first
        writer.writerow(headers)
        
        # Skip the original messy header row
        next(reader)
        
        for row in reader:
            if not row or "Timestamp" in row or "Gateway" in row:
                continue
            
            # 2. Fix the "Clipped" or "Shifted" Timestamps
            # If the first item is 26-03-05, make it 2026-03-05
            if row[0].startswith("26-"):
                row[0] = "20" + row[0]
            
            # 3. Clean the ISP Column (The 6th column / index 5)
            # We remove quotes and the internal comma so it doesn't break the 'column' command
            if len(row) >= 6:
                row[5] = row[5].replace('"', '').replace(',', '').strip()
            
            # 4. Final Polish: Ensure every row is exactly 6 columns
            while len(row) < 6:
                row.append("N/A")
                
            writer.writerow(row[:6])

    os.replace(temp_file, file_path)
    print("🚀 Repair Complete: Headers restored and quotes purged.")

if __name__ == "__main__":
    repair()
