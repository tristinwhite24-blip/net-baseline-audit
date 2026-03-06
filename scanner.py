#!/usr/bin/env python3
import socket
from datetime import datetime

def scan_port(ip, port):
    """Attempt to connect to a specific port on an IP address."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Fast timeout for efficiency
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def run_scanner(target_ip):
    print(f"\n--- Emerald Security Audit: {target_ip} ---")
    
    # Common ports relevant to Emerald Broadband infrastructure
    common_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 
        53: "DNS", 80: "HTTP", 443: "HTTPS", 
        3389: "RDP", 8080: "Proxy/Alt-HTTP"
    }
    
    start_time = datetime.now()
    open_ports = 0
    
    for port, service in common_ports.items():
        if scan_port(target_ip, port):
            print(f"[OPEN]   Port {port:4} | Service: {service}")
            open_ports += 1
        else:
            print(f"[CLOSED] Port {port:4} | Service: {service}")
            
    duration = datetime.now() - start_time
    print(f"\n--- Scan Complete: {open_ports} open ports found in {duration.total_seconds():.2f}s ---")

if __name__ == "__main__":
    target = input("Enter IP to scan (default 127.0.0.1): ")
    if not target: target = "127.0.0.1"
    run_scanner(target)
