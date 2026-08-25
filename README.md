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

echo "[+] Step 2: Installing Python 3, Pip, and Git..."
sudo apt install -y python3 python3-pip python3-venv git

echo "[+] Step 3: Setting Up Project Directory..."
mkdir -p ~/vuln-scanner
cd ~/vuln-scanner

echo "[+] Step 4: Setting Up Virtual Environment & Installing Dependencies..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install requests beautifulsoup4

echo "[+] Step 5: Generating requirements.txt..."
pip freeze > requirements.txt

echo "[+] Step 6: Initializing Git Repository..."
git init
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git add .
git commit -m "Setup scanner repository on Kali Linux" || true

echo "[+] Setup Complete!"
echo "----------------------------------------------------"
echo "To run your scanner in the future, execute:"
echo "  cd ~/vuln-scanner"
echo "  source venv/bin/activate"
echo "  python3 scanner.py"
echo "----------------------------------------------------"
echo "To push your project to GitHub, execute:"
echo "  git branch -M main"
echo "  git remote add origin [https://github.com/YOUR-USERNAME/vuln-scanner.git](https://github.com/YOUR-USERNAME/vuln-scanner.git)"
echo "  git push -u origin main"
echo "----------------------------------------------------"

# Run the scanner immediately if scanner.py exists
if [ -f "scanner.py" ]; then
    echo "[+] Launching Scanner..."
    python3 scanner.py
else
    echo "[-] scanner.py not found in ~/vuln-scanner. Please add your scanner.py script to this directory."
fi
