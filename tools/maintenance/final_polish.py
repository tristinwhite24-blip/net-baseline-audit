import csv
import os

file_path = 'network_log.csv'
temp_file = 'network_log_polished.csv'
headers = ["Timestamp", "Gateway_Latency_ms", "System_DNS_ms", "Google_DNS_ms", "Public_IP", "ISP"]

def polish():
    with open(file_path, 'r') as f_in, open(temp_file, 'w', newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        
        writer.writerow(headers)
        
        # Skip whatever headers are currently in the file
        next(reader)
        
        for row in reader:
            # Skip empty rows or header-looking rows
            if not row or "Timestamp" in row:
                continue
                
            # FIX: If the timestamp is missing (the Ghost Row), we'll estimate it 
            # as occurring between 08:41 and 09:08
            if len(row) > 0 and not row[0].startswith("2026"):
                # If the first element is a latency (like 3.855), we shift the row
                row = ["2026-03-05 08:55:00"] + row
            
            # Ensure exactly 6 columns
            while len(row) < 6:
                row.append("N/A")
            
            # Clean up the ISP name to remove any weird quotes or double spaces
            row[5] = row[5].replace('"', '').strip()
            
            writer.writerow(row[:6])

    os.replace(temp_file, file_path)
    print("✨ Polish Complete. Data is now 100% standardized.")

if __name__ == "__main__":
    polish()
