import csv
import os

file_path = 'network_log.csv'
temp_file = 'network_log_clean.csv'
headers = ["Timestamp", "Latency_ms", "Public_IP", "ISP"]

with open(file_path, 'r') as f_in, open(temp_file, 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    # Skip the old header
    next(reader)
    writer.writerow(headers)
    
    for row in reader:
        # If the row is short (old format), pad it with "N/A"
        if len(row) < 4:
            new_row = [row[0], row[1], "N/A", "N/A"]
        else:
            # Clean up any weird quotes/spacing from the new format
            new_row = [row[0], row[1], row[2], row[3].strip()]
        writer.writerow(new_row)

# Swap the clean file for the old one
os.replace(temp_file, file_path)
print("Data Cleaned and Standardized!")
