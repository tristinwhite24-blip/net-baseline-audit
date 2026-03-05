#!/bin/bash
# =================================================================
# Project: net-baseline-audit (Advanced Scanner v2.0)
# Description: High-speed scanner with MAC/Vendor discovery.
# Author: Tristin (Emerald Broadband)
# =================================================================

NETWORK="10.42.0"

echo "--------------------------------------------------------"
echo " Advanced Network Discovery: $NETWORK.0/24"
echo "--------------------------------------------------------"
printf "%-15s %-20s %-20s\n" "IP Address" "MAC Address" "Vendor (Likely)"
echo "--------------------------------------------------------"

scan_ip() {
    local ip=$1
    if ping -c 1 -W 1 "$ip" > /dev/null 2>&1; then
        # Pull the MAC address from the ARP cache
        local mac=$(ip neighbor show "$ip" | awk '{print $5}')
        
        # If no MAC is found (it's likely our own PC), get our own MAC
        if [ -z "$mac" ]; then
            mac=$(ip link show enp1s0 | grep link/ether | awk '{print $2}')
        fi

        # Simple Vendor Logic (Common at Emerald/Home)
        local vendor="Unknown"
        [[ "$mac" == a4:bb:6d* ]] && vendor="Ubiquiti"
        [[ "$mac" == 3c:18:a0* ]] && vendor="HP"
        [[ "$mac" == b8:27:eb* ]] && vendor="Raspberry Pi"
        [[ "$mac" == 00:15:5d* ]] && vendor="Microsoft/Hyper-V"

        printf "%-15s %-20s %-20s\n" "$ip" "$mac" "$vendor"
    fi
}

export -f scan_ip

# Launch parallel scan
for ip in {1..254}; do
    scan_ip $NETWORK.$ip & 
done

wait
echo "--------------------------------------------------------"
