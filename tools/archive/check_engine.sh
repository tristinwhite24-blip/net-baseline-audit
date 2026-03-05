#!/bin/bash
# =================================================================
# Project: net-baseline-audit (v2.0)
# Description: Network auditor with CSV logging for historical analysis.
# Author: Tristin (Emerald Broadband)
# =================================================================

LOG_FILE="network_log.csv"

# Create CSV header if it doesn't exist
if [ ! -f "$LOG_FILE" ]; then
    echo "Timestamp,Gateway_Latency_ms,System_DNS_ms,Google_DNS_ms" > "$LOG_FILE"
fi

# 1. Capture Data
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Capture RTT avg (The 4th field in the last line of ping output)
GATEWAY_LATENCY=$(ping -c 3 -q 1.1.1.1 | tail -1 | awk -F '/' '{print $5}')

# Capture DNS times (removing the ' msec' text to keep it numeric)
SYSTEM_DNS=$(dig google.com | grep "Query time" | awk '{print $4}')
GOOGLE_DNS=$(dig @8.8.8.8 google.com | grep "Query time" | awk '{print $4}')

# 2. Log to CSV
echo "$TIMESTAMP,$GATEWAY_LATENCY,$SYSTEM_DNS,$GOOGLE_DNS" >> "$LOG_FILE"




