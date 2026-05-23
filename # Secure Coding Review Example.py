# Secure Coding Review Example
# This script checks Python code for some common insecure patterns.

import re

def review_code(code_snippet):
    issues = []

    # Rule 1: Detect use of eval() (dangerous if used with user input)
    if "eval(" in code_snippet:
        issues.append("⚠️ Use of eval() detected. Avoid it, as it can execute malicious code.")

    # Rule 2: Detect hardcoded passwords
    if re.search(r'password\s*=\s*["\'].*["\']', code_snippet, re.IGNORECASE):
        issues.append("⚠️ Hardcoded password found. Store credentials securely instead.")

    # Rule 3: Detect use of os.system (can be exploited with command injection)
    if "os.system(" in code_snippet:
        issues.append("⚠️ Use of os.system detected. Prefer subprocess with safe arguments.")

    # Rule 4: Detect SQL queries built with string concatenation
    if re.search(r'SELECT.*\+.*FROM', code_snippet, re.IGNORECASE):
        issues.append("⚠️ SQL query built with string concatenation. Use parameterized queries.")

    # Final report
    if issues:
        print("=== Security Issues Found ===")
        for issue in issues:
            print(issue)
    else:
        print("✅ No obvious security issues detected.")

# Example: insecure code snippet
sample_code = '''
password = "12345"
query = "SELECT * FROM users WHERE id=" + user_input
os.system("rm -rf /")
eval("print('Hello')")
'''

review_code(sample_code)
