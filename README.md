# Web Vulnerability Scanner

A lightweight Python-based tool designed to scan web applications for common security misconfigurations, exposed administrative endpoints, missing security headers, Cross-Site Scripting (XSS), SQL Injection indicators, and open network ports.

> **Disclaimer**: This tool is created for educational and authorized security assessment purposes only. Do not perform scans against targets without explicit prior written authorization.

---

## 🚀 Features

- **HTTP Security Header Audit**: Detects missing headers such as `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, and `X-Content-Type-Options`.
- **Exposed Endpoint Detection**: Checks for publicly accessible administrative pages and sensitive files (e.g., `.env`, `robots.txt`, `config.php`).
- **Reflected XSS Scanner**: Identifies HTML forms that do not properly sanitize user inputs.
- **SQL Error Indicator Check**: Tests query parameters against database error signature indicators.
- **Port Scanner**: Performs basic socket checks on key service ports (`21`, `22`, `80`, `443`, `3306`, `8080`).

---

## 🛠️ Complete List of Project Commands

### 1. System Verification
Check that Python and Git are properly installed on your system:
```powershell
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
echo "  git remote add origin https://github.com/YOUR-USERNAME/vuln-scanner.git"
echo "  git push -u origin main"
echo "----------------------------------------------------"

# Run the scanner immediately if scanner.py exists
if [ -f "scanner.py" ]; then
    echo "[+] Launching Scanner..."
    python3 scanner.py
else
    echo "[-] scanner.py not found in ~/vuln-scanner. Please add your scanner.py script to this directory."
fi
