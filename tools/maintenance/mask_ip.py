import csv
import os

file_path = 'network_log.csv'
temp_file = 'network_log_masked.csv'

with open(file_path, 'r') as f_in, open(temp_file, 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    headers = next(reader)
    writer.writerow(headers)

    for row in reader:
        if len(row) >= 5 and row[4] != "N/A":
            # Masking: 70.103.136.234 becomes 70.103.xxx.xxx
            parts = row[4].split('.')
            if len(parts) == 4:
                row[4] = f"{parts[0]}.{parts[1]}.xxx.xxx"
        writer.writerow(row)

os.replace(temp_file, file_path)
print("Privacy Masking Complete: IPs are now hidden.")
