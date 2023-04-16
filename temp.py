import os
import ctypes
import tkinter as tk
from tkinter import messagebox

def is_admin():
    """
    Returns True if the script is running with administrative privileges, False otherwise.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clear_appdata_temp():
    """
    Clears all temporary files in the %AppData%\Local\Temp directory.
    """
    path = os.path.join(os.environ['LOCALAPPDATA'], 'Temp')
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

    messagebox.showinfo("Clear AppData Temp", "Temporary files have been cleared.")

def confirm_clear_appdata_temp():
    """
    Displays a confirmation dialog before clearing temporary files.
    """
    if is_admin():
        if messagebox.askokcancel("Clear AppData Temp", "Are you sure you want to clear all temporary files in the %AppData%\Local\Temp directory?"):
            clear_appdata_temp()
    else:
        messagebox.showerror("Error", "This script must be run with administrative privileges.")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    confirm_clear_appdata_temp()
