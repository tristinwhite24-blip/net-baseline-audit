import csv
import os

file_path = 'network_log.csv'
temp_file = 'network_log_masked.csv'

if not os.path.exists(file_path):
    print("Log file not found.")
    exit()

with open(file_path, 'r') as f_in, open(temp_file, 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    headers = next(reader)
    writer.writerow(headers)

    for row in reader:
        # Check if the row has IP data in the 5th column (index 4)
        if len(row) >= 5 and row[4] != "N/A" and "." in row[4]:
            parts = row[4].split('.')
            if len(parts) == 4:
                # Masking: 70.103.136.234 becomes 70.103.xxx.xxx
                row[4] = f"{parts[0]}.{parts[1]}.xxx.xxx"
        writer.writerow(row)

os.replace(temp_file, file_path)
print("Privacy Masking Complete: Existing IPs are now hidden.")
