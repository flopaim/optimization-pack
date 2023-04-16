import subprocess
import tkinter as tk
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def flush_dns():
    subprocess.call('ipconfig /flushdns')

def release_ip():
    subprocess.call('ipconfig /release')

def renew_ip():
    subprocess.call('ipconfig /renew')

def reset_winsock():
    subprocess.call('netsh winsock reset')

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

else:
    root = tk.Tk()
    root.title('Network Optimizer')

    dns_frame = tk.Frame(root)
    dns_frame.pack(side='top', padx=10, pady=10)
    dns_label = tk.Label(dns_frame, text='DNS Settings')
    dns_label.pack(side='top', padx=10, pady=10)
    flush_button = tk.Button(dns_frame, text='Flush DNS', command=flush_dns)
    flush_button.pack(side='left', padx=10, pady=10)
    release_button = tk.Button(dns_frame, text='Release IP', command=release_ip)
    release_button.pack(side='left', padx=10, pady=10)
    renew_button = tk.Button(dns_frame, text='Renew IP', command=renew_ip)
    renew_button.pack(side='left', padx=10, pady=10)
    reset_button = tk.Button(dns_frame, text='Reset Winsock', command=reset_winsock)
    reset_button.pack(side='left', padx=10, pady=10)

    root.mainloop()
