# net-baseline-audit

A high-precision Bash utility designed for real-time network infrastructure auditing. This tool was developed to establish stable performance baselines in ISP environments, specifically optimized for high-frequency Intel workstations running KDE Neon.

## 🚀 Key Features
- **Sub-Millisecond Latency Tracking:** Monitors ICMP response times with high granularity.
- **Packet Loss Analytics:** Real-time calculation of drop percentages to identify intermittent routing issues.
- **Environment Aware:** Designed to run in high-performance kernel states to minimize jitter.

## 🛠 Technical Optimization
To ensure the accuracy of the baseline, this tool is intended to be used alongside system-hardening configurations:
- **CPU Governor:** Locked to `performance` mode to eliminate frequency-scaling latency.
- **PCIe Stability:** Optimized for Realtek 8821CE/8111 hardware by disabling ASPM to prevent firmware-level timing desyncs ($H2C$).

## 📋 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/tristinwhite24-blip/net-baseline-audit.git
