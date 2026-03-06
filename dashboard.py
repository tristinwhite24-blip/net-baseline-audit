from flask import Flask, render_template_string
import csv
import os

app = Flask(__name__)
LOG_FILE = "network_log.csv"

# A simple HTML template to display your stats
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Emerald NOC - Local Health</title>
    <meta http-equiv="refresh" content="30">
    <style>
        body { font-family: sans-serif; background: #121212; color: #e0e0e0; text-align: center; }
        .container { margin-top: 50px; }
        .card { background: #1e1e1e; padding: 20px; border-radius: 10px; display: inline-block; margin: 10px; border: 1px solid #333; }
        .stat { font-size: 2em; color: #00ff41; }
        .header { color: #888; text-transform: uppercase; font-size: 0.8em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Emerald Network Health</h1>
        <p>Location: Eugene, OR | ISP: Emerald Broadband</p>
        <div class="card"><div class="header">Gateway Latency</div><div class="stat">{{ latency }}ms</div></div>
        <div class="card"><div class="header">System DNS</div><div class="stat">{{ system_dns }}ms</div></div>
        <div class="card"><div class="header">Google DNS</div><div class="stat">{{ google_dns }}ms</div></div>
        <hr style="width: 50%; border: 0.5px solid #333;">
        <p>Last Update: {{ timestamp }}</p>
    </div>
</body>
</html>
"""

def get_latest_data():
    if not os.path.exists(LOG_FILE):
        return ["N/A"] * 6
    with open(LOG_FILE, "r") as f:
        reader = list(csv.reader(f))
        return reader[-1] if len(reader) > 1 else ["N/A"] * 6

@app.route('/')
def home():
    data = get_latest_data()
    # Mapping: TS, Lat, DNS_Sys, DNS_Goo, IP, ISP
    return render_template_string(HTML_TEMPLATE, 
                                   timestamp=data[0], 
                                   latency=data[1], 
                                   system_dns=data[2], 
                                   google_dns=data[3])

if __name__ == "__main__":
    # Runs on your local network
    app.run(host='0.0.0.0', port=5000)
