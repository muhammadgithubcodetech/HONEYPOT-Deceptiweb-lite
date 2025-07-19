import re

# Dictionary of attack types and their regex patterns
ATTACK_PATTERNS = {
    "SQL Injection": [
        r"(?i)(\bUNION\b|\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bDROP\b|\bOR\b|\bAND\b).*(=|--|#|'|\"|;)",
        r"(?i)(\bOR\b\s+1=1)",   # classic auth bypass
        r"(?i)(\bSELECT\b\s+.*\bFROM\b)",
        r"(?i)('|\")\s*--",      # comment-based injection
        r"(?i)(\bEXEC\b|\bEXECUTE\b).*"
    ],
    "Cross-Site Scripting (XSS)": [
        r"(?i)<script.*?>.*?</script>",
        r"(?i)on\w+\s*=",
        r"(?i)javascript:",
        r"(?i)<.*?src\s*=.*?>",
        r"(?i)<iframe.*?>",
        r"(?i)<img\s+.*?onerror\s*=.*?>"
    ],
    "Command Injection": [
        r"(;|\||&&)\s*(ls|whoami|pwd|cat|echo|ping)",
        r"`\s*(ls|id|cat).*?`",
        r"\$\((.*?)\)",
        r"&\s*(dir|net|type)",
    ],
    "Path Traversal": [
        r"\.\./\.\./",
        r"\.\.\\\.\.\\",
        r"/etc/passwd",
        r"([a-zA-Z]:\\|/)?windows\\system32",
        r"/bin/sh"
    ],
    "LDAP Injection": [
        r"(?i)(\*|\(|\)|&|\||!|=).*objectClass",
        r"(?i)(\badmin\b).*?(\*)"
    ],
    "Basic Brute Force": [
        r"admin",
        r"root",
        r"password123",
        r"letmein",
        r"123456"
    ]
}

def detect_attack(input_text):
    matches = []
    for attack_type, patterns in ATTACK_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, input_text):
                matches.append(attack_type)
                break  # Avoid duplicate tagging
    return matches if matches else ["No Threat Detected"]
