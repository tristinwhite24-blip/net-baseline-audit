#!/bin/bash
# =================================================================
# Project: net-baseline-audit
# Description: Real-time network latency and DNS resolution auditor.
# Optimization: Best used with CPU in 'performance' mode.
# Author: Tristin (Emerald Broadband)
# =================================================================

echo "------------------------------------------------"
echo "  Network Infrastructure Audit - Active Session "
echo "------------------------------------------------"

# 1. Latency Check (Public DNS - Cloudflare)
echo "--- LATENCY TO PUBLIC GATEWAY (1.1.1.1) ---"
ping -c 3 -q 1.1.1.1 | grep rtt

# 2. DNS Resolution Speed (Comparing Local System vs Google)
# We use dig to measure the millisecond response of DNS queries
echo "--- DNS RESOLUTION PERFORMANCE ---"
LOCAL_DNS=$(dig google.com | grep "Query time" | awk '{print "System DNS:", $4, $5}')
GOOGLE_DNS=$(dig @8.8.8.8 google.com | grep "Query time" | awk '{print "Google DNS:", $4, $5}')

echo "$LOCAL_DNS"
echo "$GOOGLE_DNS"

echo "------------------------------------------------"
echo " Audit Complete. Session Baseline established."
echo "------------------------------------------------"
