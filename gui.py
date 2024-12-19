import tkinter as tk
from tkinter import messagebox
import requests
import stdiomask
from uuid import uuid4
import tkinter.font as tkFont

# Function to handle login and grab cookies
def grab_cookies(platform, username, password):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }

    if platform == "Instagram":
        url = "https://i.instagram.com/api/v1/accounts/login/"
        data = {
            "username": username,
            "reg_login": "0",
            "enc_password": f"#PWD_INSTAGRAM:0:&:{password}",
            "device_id": str(uuid4()),
            "login_attempt_count": "0",
            "phone_id": str(uuid4())
        }
    elif platform == "Netflix":
        url = "https://www.netflix.com/Login"
        data = {
            "email": username,
            "password": password,
            "rememberMe": "true",
            "flow": "websiteSignUp",
            "mode": "login",
            "action": "loginAction"
        }
    elif platform == "Facebook":
        url = "https://www.facebook.com/login/device-based/regular/login/"
        data = {
            "email": username,
            "pass": password
        }
    elif platform == "Twitter":
        url = "https://twitter.com/sessions"
        data = {
            "username": username,
            "password": password
        }
    elif platform == "LinkedIn":
        url = "https://www.linkedin.com/uas/login-submit"
        data = {
            "session_key": username,
            "session_password": password
        }

    try:
        r = requests.post(url=url, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", f"Network Error: {e}")
        return

    if 'incorrect' in r.text or 'login_error' in r.text:
        messagebox.showerror("Login Failed", "Incorrect username or password.")
    elif 'home' in r.text or 'login-success' in r.text or 'feed' in r.text:
        cookies = r.cookies.get_dict()
        if cookies:
            messagebox.showinfo("Login Successful", f"Cookies: {cookies}")
        else:
            messagebox.showerror("Failed", "Failed to retrieve cookies.")
    else:
        messagebox.showerror("Login Failed", f"Response: {r.text}")

# GUI Setup
def create_gui():
    window = tk.Tk()
    window.title("Cookie Grabber - Author: saltx5")
    window.geometry("500x400")
    window.config(bg="#2C3E50")  # Set background color

    # Custom font
    header_font = tkFont.Font(family="Helvetica", size=18, weight="bold")
    label_font = tkFont.Font(family="Helvetica", size=12)
    button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

    # Header
    header_label = tk.Label(window, text="Cookie Grabber", font=header_font, fg="#9CFF1E", bg="#2C3E50")
    header_label.pack(pady=10)

    # Author Name
    author_label = tk.Label(window, text="Author: saltx5", font=label_font, fg="#BDC3C7", bg="#2C3E50")
    author_label.pack(pady=5)

    # Platform Selection
    platform_label = tk.Label(window, text="Select Platform:", font=label_font, fg="#BDC3C7", bg="#2C3E50")
    platform_label.pack(pady=10)

    platforms = ["Instagram", "Netflix", "Facebook", "Twitter", "LinkedIn"]
    platform_var = tk.StringVar(value=platforms[0])
    platform_menu = tk.OptionMenu(window, platform_var, *platforms)
    platform_menu.config(font=label_font, width=20)
    platform_menu.pack()

    # Username/Email Input
    username_label = tk.Label(window, text="Username/Email:", font=label_font, fg="#BDC3C7", bg="#2C3E50")
    username_label.pack(pady=5)
    username_entry = tk.Entry(window, font=label_font, width=30)
    username_entry.pack()

    # Password Input
    password_label = tk.Label(window, text="Password:", font=label_font, fg="#BDC3C7", bg="#2C3E50")
    password_label.pack(pady=5)
    password_entry = tk.Entry(window, font=label_font, show="*", width=30)
    password_entry.pack()

    # Submit Button
    def on_submit():
        platform = platform_var.get()
        username = username_entry.get()
        password = password_entry.get()
        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
        else:
            grab_cookies(platform, username, password)

    submit_button = tk.Button(window, text="Grab Cookies", command=on_submit, font=button_font, bg="#9CFF1E", fg="black", width=20, height=2)
    submit_button.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
