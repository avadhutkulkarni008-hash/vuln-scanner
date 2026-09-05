# Web Vulnerability Scanner on Kali Linux

A lightweight Python-based tool designed to scan web applications for common security misconfigurations, exposed administrative endpoints, missing security headers, Cross-Site Scripting (XSS), SQL Injection indicators, and open network ports.

> **Disclaimer**: This tool is created for educational and authorized security assessment purposes only. Do not perform scans against targets without explicit prior written authorization.

---

## ⚡ Quick Start Script (`setup_and_run.sh`)

You can automate the entire setup, virtual environment configuration, dependency installation, and initial execution using the script below.

### 1. Create the Script File
```bash
nano setup_and_run.sh
#!/bin/bash

# Exit on error
set -e

echo "[+] Step 1: Updating System Packages..."
sudo apt update -y

echo "[+] Step 3: Setting Up Project Directory..."
mkdir -p ~/vuln-scanner
cd ~/vuln-scanner

echo "[+] Step 4: Setting Up Virtual Environment & Installing Dependencies..."
python3 -m venv venv
source venv/bin/activate
pip install requests beautifulsoup4

# Run the scanner immediately if scanner.py exists
if [ -f "scanner.py" ]; then
    echo "[+] Launching Scanner..."
    python3 scanner.py
else
    echo "[-] scanner.py not found in ~/vuln-scanner. Please add your scanner.py script to this directory."
fi
