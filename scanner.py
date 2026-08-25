import requests
import socket
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 1. Check HTTP Security Headers
def check_headers(target_url):
    print("\n[+] Checking Security Headers...")
    try:
        response = requests.get(target_url, timeout=5)
        headers = response.headers
        
        important_headers = {
            "X-Frame-Options": "Protects against Clickjacking attacks",
            "X-Content-Type-Options": "Prevents MIME-sniffing",
            "Content-Security-Policy": "Restricts origins of loaded scripts/resources",
            "Strict-Transport-Security": "Enforces HTTPS connections"
        }
        
        for header, description in important_headers.items():
            if header in headers:
                print(f"  [SAFE] {header}: Present")
            else:
                print(f"  [WARNING] Missing {header} ({description})")
    except requests.RequestException as e:
        print(f"  [ERROR] Header check failed: {e}")

# 2. Check for Common Exposed Admin Paths
def check_exposed_paths(target_url):
    print("\n[+] Checking Exposed Files & Admin Paths...")
    common_paths = ["admin/", "login/", "robots.txt", ".env", "config.php", "phpinfo.php"]
    
    for path in common_paths:
        full_url = urljoin(target_url, path)
        try:
            res = requests.get(full_url, timeout=3)
            if res.status_code == 200:
                print(f"  [EXPOSED] Found endpoint: {full_url} (HTTP 200)")
            elif res.status_code == 403:
                print(f"  [FORBIDDEN] Access restricted: {full_url} (HTTP 403)")
        except requests.RequestException:
            pass

# 3. Basic Test for Reflected XSS in HTML Forms
def test_form_xss(target_url):
    print("\n[+] Scanning HTML Forms for XSS Vulnerabilities...")
    try:
        response = requests.get(target_url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        
        if not forms:
            print("  [-] No HTML forms found on main page.")
            return

        payload = "<script>alert('XSS')</script>"
        for i, form in enumerate(forms, 1):
            action = form.get('action')
            method = form.get('method', 'get').lower()
            target_endpoint = urljoin(target_url, action)
            
            data = {}
            for input_tag in form.find_all('input'):
                input_name = input_tag.get('name')
                if input_name:
                    data[input_name] = payload
            
            if method == 'post':
                res = requests.post(target_endpoint, data=data, timeout=5)
            else:
                res = requests.get(target_endpoint, params=data, timeout=5)
                
            if payload in res.text:
                print(f"  [VULNERABLE] Form #{i} at {target_endpoint} reflects unescaped input.")
            else:
                print(f"  [SAFE] Form #{i} safely handled the test input.")
    except requests.RequestException as e:
        print(f"  [ERROR] Form scan failed: {e}")

# 4. Basic Check for SQL Error Indicators
def test_sqli_indicators(target_url):
    print("\n[+] Testing Query Parameters for SQL Error Indicators...")
    sqli_payload = "'"
    test_url = f"{target_url}?id={sqli_payload}"
    sql_errors = ["you have an error in your sql syntax", "unclosed quotation mark", "mysql_fetch_array"]
    
    try:
        res = requests.get(test_url, timeout=5)
        found_error = False
        for error in sql_errors:
            if error in res.text.lower():
                found_error = True
                print(f"  [VULNERABLE] SQL syntax error reflected on parameter 'id'.")
                break
        if not found_error:
            print("  [SAFE] No database errors triggered by basic payload.")
    except requests.RequestException as e:
        print(f"  [ERROR] SQLi test failed: {e}")

# 5. Basic Port Scanner
def scan_common_ports(hostname):
    print("\n[+] Scanning Open Network Ports...")
    ports = [21, 22, 80, 443, 3306, 8080]
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((hostname, port))
        if result == 0:
            print(f"  [OPEN] Port {port} is open")
        sock.close()

if __name__ == "__main__":
    target = input("Enter target URL (e.g., http://example.com): ").strip()
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target

    # Extract hostname for port scanning
    hostname = target.split("//")[-1].split("/")[0].split(":")[0]

    check_headers(target)
    check_exposed_paths(target)
    test_form_xss(target)
    test_sqli_indicators(target)
    scan_common_ports(hostname)