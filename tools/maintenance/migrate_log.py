import csv
import os

file_path = 'network_log.csv'
temp_file = 'network_log_migrated.csv'
master_headers = ["Timestamp", "Gateway_Latency_ms", "System_DNS_ms", "Google_DNS_ms", "Public_IP", "ISP"]

with open(file_path, 'r') as f_in, open(temp_file, 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    writer.writerow(master_headers)
    next(reader) # Skip the messy existing header

    for row in reader:
        # Case 1: Old 4-column Bash rows (TS, Lat, DNS1, DNS2)
        if len(row) == 4 and "." not in row[2]: 
            # Map: [TS, Lat, DNS1, DNS2, "N/A", "N/A"]
            writer.writerow([row[0], row[1], row[2], row[3], "N/A", "N/A"])
            
        # Case 2: Recent 4-column Python 'Identity' rows (TS, Lat, IP, ISP)
        elif len(row) == 4 and "." in row[2]:
            # Map: [TS, Lat, "N/A", "N/A", row[2], row[3]]
            writer.writerow([row[0], row[1], "N/A", "N/A", row[2], row[3]])
            
        # Case 3: Already 6 columns (Standardize the ISP comma issue)
        elif len(row) >= 6:
            # Join any extra split columns caused by the ISP name comma
            isp_name = " ".join(row[5:]).replace(",", "")
            writer.writerow([row[0], row[1], row[2], row[3], row[4], isp_name])

os.replace(temp_file, file_path)
print("Migration Complete: Data is now in 6-column Master Format.")
