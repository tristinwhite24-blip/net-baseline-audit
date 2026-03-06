# Emerald NOC Suite v3.0
Automated network performance tracking and security auditing for Emerald Broadband.

## Features
- **Continuous Audit:** Logs Gateway Latency and Dual-DNS benchmarks every 5 minutes.
- **Live Dashboard:** Real-time Flask telemetry available at http://localhost:5000.
- **Port Scanner:** Active security auditing for common ISP services (SSH, DNS, HTTP, HTTPS).
- **Privacy Masking:** Automatically redacts public IPs (70.103.xxx.xxx) for security compliance.

## Installation
Ensure you have the required Python libraries:
\`\`\`bash
pip install -r requirements.txt --break-system-packages
\`\`\`

## Usage
- **Audit:** \`./audit.py\` (Best run via Cron for a 5-minute baseline)
- **Dashboard:** \`python3 dashboard.py\` (Best run as a systemd service)
- **Scanner:** \`./scanner.py\`
