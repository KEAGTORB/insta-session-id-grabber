import requests, os, stdiomask
from uuid import uuid4

# Clear the screen and set the title (works on both Windows and Linux)
os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'nt':
    os.system('title Instagram Session Grabber')

# ASCII Art for Header
print(r"""
 _           _                            _                               _               
(_)_ __  ___| |_ __ _   ___  ___  ___ ___(_) ___  _ __     __ _ _ __ __ _| |__   ___ _ __ 
| | '_ \/ __| __/ _` | / __|/ _ \/ __/ __| |/ _ \| '_ \   / _` | '__/ _` | '_ \ / _ \ '__|
| | | | \__ \ || (_| | \__ \  __/\__ \__ \ | (_) | | | | | (_| | | | (_| | |_) |  __/ |   
|_|_| |_|___/\__\__,_| |___/\___||___/___/_|\___/|_| |_|  \__, |_|  \__,_|_.__/ \___|_|   
                                                          |___/  github.com/saltX5                       
""")

# Input for username and password
username = input(f"[+] Enter Username: ")
password = stdiomask.getpass(f"[+] Enter Password: ")

# Headers for the request
headers = {
    "Host": "i.instagram.com",
    "X-Ig-Connection-Type": "WiFi",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Ig-Capabilities": "36r/Fx8=",
    "User-Agent": "Instagram 159.0.0.28.123 (iPhone8,1; iOS 14_1; en_SA@calendar=gregorian; ar-SA; scale=2.00; 750x1334; 244425769) AppleWebKit/420+",
    "X-Ig-App-Locale": "en",
    "Content-Length": "778",
    "Accept-Encoding": "gzip, deflate"
}

# Data for the request
data = {
    "username": username,
    "reg_login": "0",
    "enc_password": f"#PWD_INSTAGRAM:0:&:{password}",
    "device_id": str(uuid4()),
    "login_attempt_count": "0",
    "phone_id": str(uuid4())
}

# URL for the login request
url = "https://i.instagram.com/api/v1/accounts/login/"

try:
    r = requests.post(url=url, headers=headers, data=data)
except requests.exceptions.RequestException as e:
    print(f"[!] Network Error: {e}")
    quit()

# Response handling
if 'The password you entered is incorrect' in r.text:
    print("\n[!] Incorrect password. Exiting...")
    input("[+] Press any key to exit.")
    quit()
elif 'logged_in_user' in r.text:
    print("[+] Logged in successfully!")
else:
    print(f"[!] Login failed. Response: {r.text}")
    input("[+] Press any key to exit.")
    quit()

# Extract the session ID
session_id = r.cookies.get("sessionid")
if session_id:
    print(f"[+] Session ID: {session_id}")
else:
    print("[!] Failed to retrieve session ID.")

input("[+] Press any key to exit.")
