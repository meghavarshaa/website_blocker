# website_blocker.py
"""
Website Blocker Script
----------------------
Blocks specified websites by mapping them to localhost in the system's hosts file.
Works on both Linux/Mac and Windows.

Usage:
    python website_blocker.py
"""

from datetime import datetime
import sys
import os

# ===== CONFIG =====
end_time = datetime(2024, 6, 16, 12)  # (year, month, day, hour)
redirect = "127.0.0.1"

# Adjust hosts file path depending on OS
if os.name == "nt":  # Windows
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:  # Linux/Mac
    hosts_path = "/etc/hosts"

# ===== MAIN FUNCTION =====
def block_websites(sites_to_block):
    if datetime.now() < end_time:
        print("[INFO] Blocking sites...")
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostfile.write(redirect + " " + site + "\n")
    else:
        print("[INFO] Unblocking sites...")
        with open(hosts_path, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
            hostfile.truncate()


if __name__ == "__main__":
    input_string = input("Enter websites to block (space-separated):\n")
    sites_to_block = input_string.split()
    block_websites(sites_to_block)
