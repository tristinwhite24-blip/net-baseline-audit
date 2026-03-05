import csv
import os

file_path = 'network_log.csv'
temp_file = 'network_log_migrated.csv'
# The Master 6-Column Header
master_headers = ["Timestamp", "Gateway_Latency_ms", "System_DNS_ms", "Google_DNS_ms", "Public_IP", "ISP"]

with open(file_path, 'r') as f_in, open(temp_file, 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    # Write the new master header
    writer.writerow(master_headers)
    
    # Skip the original messy header from the file
    next(reader)
    
    for row in reader:
        # 1. Handle Old Bash Rows (4 columns)
        if len(row) == 4 and "." not in row[2]: # row[2] is 0, not an IP
            # Map: [TS, Lat, DNS1, DNS2, "N/A", "N/A"]
            writer.writerow([row[0], row[1], row[2], row[3], "N/A", "N/A"])
        
        # 2. Handle the Recent Python "Identity" Rows
        elif len(row) == 4 and "." in row[2]: # row[2] is an IP address
            # Map: [TS, Lat, "N/A", "N/A", IP, ISP]
            writer.writerow([row[0], row[1], "N/A", "N/A", row[2], row[3]])

# Swap the files
os.replace(temp_file, file_path)
print("Migration Complete: Data is now in 6-column Master Format.")
