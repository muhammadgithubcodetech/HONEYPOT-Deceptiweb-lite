## HONEYPOT-Deceptiweb-lite
HONEYPOT-Deceptiweb-lite is a deceptive admin login interface designed to detect, analyze, and log suspicious activity by mimicking a real admin panel. It silently captures brute force attempts, injection payloads, and unauthorized access behaviors while appearing legitimate to attackers

**DeceptiWeb Lite** is a lightweight honeypot project designed to mimic a vulnerable admin panel. It detects and logs attacker behavior using predefined payload patterns, while presenting deceptive functionality to keep the attacker engaged.

---

## Project Overview

This project is meant to:

- Attract malicious actors with a realistic-looking login page.
- Detect common attack patterns such as SQL Injection, LDAP Injection, and Brute Force.
- Log all attempts and behaviors for later analysis.
- Provide a fake dashboard with mock functionality to increase realism and collect additional data.

---

## Features

- Simulated Admin Login Page
- Detection of:
  - SQL Injection
  - LDAP Injection
  - Brute Force attempts
- Logging of:
  - IP address
  - User-agent
  - Payloads
  - Actions on the fake dashboard
- Fake dashboard actions:
  - Reset Firewall Logs
  - Clear Admin Logs
  - View System Files
  - User Manager
  - Kill IDS

---
## Visuals


-Screenshot of the fake login UI


<img width="695" height="275" alt="login" src="https://github.com/user-attachments/assets/762004f8-c35d-4152-be61-89e3dae1a760" />





- admin page


<img width="1030" height="852" alt="admin" src="https://github.com/user-attachments/assets/51db241b-7bb7-43c1-a9a2-4c9708e92444" />


 
 


- Screenshot of the deceptive dashboard



<img width="1060" height="771" alt="dashboard" src="https://github.com/user-attachments/assets/ba19f2ac-ca1f-4e09-9319-de2abc06db2f" />






<img width="1072" height="817" alt="reset" src="https://github.com/user-attachments/assets/368e5512-8662-4745-9921-14954814b1f6" />




      
- Sample of `attacks.log` entries


<img width="1047" height="202" alt="logs" src="https://github.com/user-attachments/assets/629d1475-9d2a-43e3-b767-afcb662a6ed7" />






<img width="657" height="128" alt="attack" src="https://github.com/user-attachments/assets/0934fe84-1256-4840-87d5-4d607161a666" />









<img width="468" height="72" alt="logsreset" src="https://github.com/user-attachments/assets/15aae23f-7aef-4d32-95a5-599917fc62c0" />










 

---


## Technologies Used

- Python 3
- Flask
- HTML/CSS
- Regular Expressions (Regex)
- File I/O and Logging

---

## Folder Structure

HONEYPOT-Deceptiweb-lite/
├── app.py # Main Flask app and routes
├── payload_patterns.py # Regex-based detection engine
├── templates/
│ ├── login.html # Fake admin login interface
│ └── dashboard.html # Interactive trap dashboard
├── logs/
│ └── attacks.log # All activity and payload logs
└── README.md


 How It Works

1. **Login Simulation**: The attacker submits a login form.
2. **Pattern Matching**: Input is scanned for malicious payloads using regex.
3. **Threat Logging**: Matches are recorded to `logs/attacks.log` along with metadata.
4. **Conditional Access**: Repeated attempts or severe threats may "grant access" to the fake dashboard.
5. **Engagement Trap**: Interacting with dashboard buttons triggers logging but does nothing.


How to Setup

```bash
 git clone https://github.com/muhammadgithubcodetech/HONEYPOT-Deceptiweb-lite.git
 cd HONEYPOT-Deceptiweb-lite

2. Install Requirements
  pip install flask


3. Start the Server
  python app.py

Then visit
http://127.0.0.1:5000/admin



Disclaimer

This project is for educational and cybersecurity research purposes only. It is not intended for production use and should not be deployed on public-facing servers.
