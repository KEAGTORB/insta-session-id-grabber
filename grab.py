import requests, os, stdiomask
from uuid import uuid4

# Clear the screen and set the title (works on both Windows and Linux)
os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'nt':
    os.system('title Cookie Grabber - Instagram, Netflix, Facebook, Twitter, LinkedIn')

# ASCII Art for Header
print(r"""
    _____ _____            ____            _____ ____   ____  _  _______ ______  _____ 
  / ____|  __ \     /\   |  _ \          / ____/ __ \ / __ \| |/ /_   _|  ____|/ ____|  
 | |  __| |__) |   /  \  | |_) |_____   | |   | |  | | |  | | ' /  | | | |__  | (___  
 | | |_ |  _  /   / /\ \ |  _ <______|  | |   | |  | | |  | |  <   | | |  __|  \___ \ 
 | |__| | | \ \  / ____ \| |_) |        | |___| |__| | |__| | . \ _| |_| |____ ____) |
  \_____|_|  \_\/_/    \_\____/          \_____\____/ \____/|_|\_\_____|______|_____/ 
                                                                    github.com/saltX5                  

[+] Author: saltx5 [+]                             
""")

# Menu for selecting platform
print("Select a platform to grab cookies from:")
print("[1] Instagram")
print("[2] Netflix")
print("[3] Facebook")
print("[4] Twitter")
print("[5] LinkedIn")
choice = input("[+] Enter your choice (1, 2, 3, 4, or 5): ")

if choice == '1':
    # Instagram Cookie Grabber
    print("\n[+] Instagram Login")
    username = input(f"[+] Enter Username: ")
    password = stdiomask.getpass(f"[+] Enter Password: ")

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

    data = {
        "username": username,
        "reg_login": "0",
        "enc_password": f"#PWD_INSTAGRAM:0:&:{password}",
        "device_id": str(uuid4()),
        "login_attempt_count": "0",
        "phone_id": str(uuid4())
    }

    url = "https://i.instagram.com/api/v1/accounts/login/"

    try:
        r = requests.post(url=url, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        print(f"[!] Network Error: {e}")
        quit()

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

    session_id = r.cookies.get("sessionid")
    if session_id:
        print(f"[+] Instagram Session ID: {session_id}")
    else:
        print("[!] Failed to retrieve Instagram session ID.")

elif choice == '2':
    # Netflix Cookie Grabber
    print("\n[+] Netflix Login")
    email = input(f"[+] Enter Email: ")
    password = stdiomask.getpass(f"[+] Enter Password: ")

    headers = {
        "Host": "www.netflix.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "X-Netflix.os.fullname": "Windows 10",
        "X-Netflix.os.version": "10.0",
        "X-Netflix.browser": "Chrome",
        "X-Netflix.browser.version": "96.0.4664.93",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }

    data = {
        "email": email,
        "password": password,
        "rememberMe": "true",
        "flow": "websiteSignUp",
        "mode": "login",
        "action": "loginAction"
    }

    url = "https://www.netflix.com/Login"

    try:
        r = requests.post(url=url, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        print(f"[!] Network Error: {e}")
        quit()

    if 'Incorrect password' in r.text or 'Sorry, we can\'t find an account with this email address.' in r.text:
        print("\n[!] Incorrect email or password. Exiting...")
        input("[+] Press any key to exit.")
        quit()
    elif 'login-success' in r.text:
        print("[+] Logged in successfully!")
    else:
        print(f"[!] Login failed. Response: {r.text}")
        input("[+] Press any key to exit.")
        quit()

    cookies = r.cookies.get_dict()
    if cookies:
        print(f"[+] Netflix Cookies: {cookies}")
    else:
        print("[!] Failed to retrieve Netflix cookies.")

elif choice == '3':
    # Facebook Cookie Grabber
    print("\n[+] Facebook Login")
    email = input(f"[+] Enter Email: ")
    password = stdiomask.getpass(f"[+] Enter Password: ")

    headers = {
        "Host": "www.facebook.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }

    data = {
        "email": email,
        "pass": password
    }

    url = "https://www.facebook.com/login/device-based/regular/login/"

    try:
        r = requests.post(url=url, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        print(f"[!] Network Error: {e}")
        quit()

    if 'login_error' in r.text:
        print("\n[!] Incorrect email or password. Exiting...")
        input("[+] Press any key to exit.")
        quit()
    elif 'home' in r.text:
        print("[+] Logged in successfully!")
    else:
        print(f"[!] Login failed. Response: {r.text}")
        input("[+] Press any key to exit.")
        quit()

    cookies = r.cookies.get_dict()
    if cookies:
        print(f"[+] Facebook Cookies: {cookies}")
    else:
        print("[!] Failed to retrieve Facebook cookies.")

elif choice == '4':
    # Twitter Cookie Grabber
    print("\n[+] Twitter Login")
    username = input(f"[+] Enter Username: ")
    password = stdiomask.getpass(f"[+] Enter Password: ")

    headers = {
        "Host": "api.twitter.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }

    data = {
        "username": username,
        "password": password
    }

    url = "https://twitter.com/sessions"

    try:
        r = requests.post(url=url, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        print(f"[!] Network Error: {e}")
        quit()

    if 'incorrect username' in r.text:
        print("\n[!] Incorrect username or password. Exiting...")
        input("[+] Press any key to exit.")
        quit()
    elif 'home' in r.text:
        print("[+] Logged in successfully!")
    else:
        print(f"[!] Login failed. Response: {r.text}")
        input("[+] Press any key to exit.")
        quit()

    cookies = r.cookies.get_dict()
    if cookies:
        print(f"[+] Twitter Cookies: {cookies}")
    else:
        print("[!] Failed to retrieve Twitter cookies.")

elif choice == '5':
    # LinkedIn Cookie Grabber
    print("\n[+] LinkedIn Login")
    email = input(f"[+] Enter Email: ")
    password = stdiomask.getpass(f"[+] Enter Password: ")

    headers = {
        "Host": "www.linkedin.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }

    data = {
        "session_key": email,
        "session_password": password
    }

    url = "https://www.linkedin.com/uas/login-submit"

    try:
        r = requests.post(url=url, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        print(f"[!] Network Error: {e}")
        quit()

    if 'incorrect' in r.text:
        print("\n[!] Incorrect email or password. Exiting...")
        input("[+] Press any key to exit.")
        quit()
    elif 'feed' in r.text:
        print("[+] Logged in successfully!")
    else:
        print(f"[!] Login failed. Response: {r.text}")
        input("[+] Press any key to exit.")
        quit()

    cookies = r.cookies.get_dict()
    if cookies:
        print(f"[+] LinkedIn Cookies: {cookies}")
    else:
        print("[!] Failed to retrieve LinkedIn cookies.")

else:
    print("[!] Invalid choice. Exiting...")

input("[+] Press any key to exit.")
