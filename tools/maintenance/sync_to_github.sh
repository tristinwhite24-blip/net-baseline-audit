#!/bin/bash

# Navigate to the project directory
cd /home/tristin/Projects/net-baseline-audit

# Add the log file
git add network_log.csv

# Commit with a timestamped message
git commit -m "Automated Daily Sync: $(date +'%Y-%m-%d %H:%M:%S')"

# Push to GitHub
git push origin main
