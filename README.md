# Network Baseline Auditor v2.1
Automated network performance tracking for Emerald Broadband connections.

## Features
- **Gateway Latency:** Measures RTT to Cloudflare (1.1.1.1).
- **Dual-DNS Tracking:** Compares local System DNS against Google Public DNS (8.8.8.8) using direct UDP queries.
- **Identity Logging:** Records Public IP and ISP name (Emerald Broadband LLC) to track failover events.
- **CSV Logging:** Maintains a 6-column historical record for long-term baseline analysis.

## Installation
Ensure you have the required Python libraries:
\`\`\`bash
pip install -r requirements.txt --break-system-packages
\`\`\`

## Usage
Run the auditor directly:
\`\`\`bash
./audit.py
\`\`\`

View the logs in a formatted table:
\`\`\`bash
column -s, -t network_log.csv
\`\`\`
