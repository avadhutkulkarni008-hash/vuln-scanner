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
python --version
git --version
