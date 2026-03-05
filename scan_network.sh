#!/bin/bash
# =================================================================
# Project: net-baseline-audit (Fast Subnet Scanner)
# Description: Parallel pings for near-instant discovery.
# Author: Tristin (Emerald Broadband)
# =================================================================

NETWORK="10.42.0"

echo "---------------------------------------"
echo " Fast Scanning Subnet: $NETWORK.0/24"
echo "---------------------------------------"

# Define the scan function
scan_ip() {
    ping -c 1 -W 1 $1 > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "[+] Host Found: $1"
    fi
}

# Export the function so the sub-shells can use it
export -f scan_ip

# Launch all 254 pings simultaneously in the background
for ip in {1..254}; do
    scan_ip $NETWORK.$ip & 
done

# Wait for all background pings to finish before closing
wait

echo "---------------------------------------"
echo " Scan Complete."
