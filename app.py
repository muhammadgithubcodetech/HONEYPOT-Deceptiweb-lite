from flask import Flask, render_template, request, redirect, url_for
from payload_patterns import detect_attack
import os
from datetime import datetime, timezone

app = Flask(__name__)
os.makedirs("logs", exist_ok=True)
attempt_counter = {}

# Logging functions
def log_event(ip, user_agent, action):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"[{timestamp}] IP: {ip}\n"
        f"  → Action: {action}\n"
        f"  → User-Agent: {user_agent}\n"
        + "-" * 60 + "\n"
    )
    with open("logs/attacks.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

def log_attack(ip, username, password, threats, user_agent):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"[{timestamp}] IP: {ip}\n"
        f"  → Username: {username}\n"
        f"  → Password: {password}\n"
        f"  → Detected Threats: {', '.join(threats) if threats else 'None'}\n"
        f"  → User-Agent: {user_agent}\n"
        + "-" * 60 + "\n"
    )
    with open("logs/attacks.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

# Routes
@app.route('/')
def home():
    return "Welcome to DeceptiWeb Lite"

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        full_input = f"{username} {password}"

        threats = detect_attack(full_input)
        attempt_counter[ip_address] = attempt_counter.get(ip_address, 0) + 1
        attempt_count = attempt_counter[ip_address]

        print("\n[!] Login Attempt Detected")
        print(f"  → Username: {username}")
        print(f"  → Password: {password}")
        print(f"  → Detected Threats: {', '.join(threats) if threats else 'None'}")
        print(f"  → IP Address: {ip_address}")
        print(f"  → User-Agent: {user_agent}")
        print(f"  → Attempt Count: {attempt_count}")
        print("-" * 60)

        log_attack(ip_address, username, password, threats, user_agent)

        if attempt_count >= 3 or any(t in threats for t in ['Brute Force', 'SQL Injection']):
            return redirect(url_for('dashboard'))

        return render_template("login.html", message="Invalid login. Try again.")

    return render_template("login.html", message="")

@app.route('/dashboard')
def dashboard():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited /dashboard")
    msg = request.args.get("msg", "")
    return render_template("dashboard.html", message=msg)

@app.route('/trigger-reset', methods=['POST'])
def trigger_reset():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Clicked 'Reset Firewall Logs'")
    return redirect(url_for('dashboard', msg="Firewall logs reset."))

@app.route('/clear-logs', methods=['POST'])
def clear_logs():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Clicked 'Clear Admin Logs'")
    return redirect(url_for('dashboard', msg="Admin logs cleared."))

@app.route('/view-files')
def view_files():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited 'View System Files'")
    return redirect(url_for('dashboard', msg="Opened system files."))

@app.route('/user-manager')
def user_manager():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Visited 'User Manager'")
    return redirect(url_for('dashboard', msg="User manager loaded."))

@app.route('/kill-ids', methods=['POST'])
def kill_ids():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_event(ip, ua, "Attempted to 'Kill IDS'")
    return redirect(url_for('dashboard', msg="IDS terminated."))

if __name__ == '__main__':
    app.run(debug=True)