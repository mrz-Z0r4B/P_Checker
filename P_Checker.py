import tkinter as tk
from tkinter import ttk
import re
from zxcvbn import zxcvbn

# Author: Amal Mirza P
# Tool Name: Mrz - Advanced Password Strength Checker
# Date: October 2024

# Function to calculate password strength
def check_password_strength(password):
    strength = zxcvbn(password)
    score = strength['score']
    
    feedback = strength['feedback']['suggestions']
    if not feedback:
        feedback = "Your password is strong!"
    else:
        feedback = "Suggestions: " + " ".join(feedback)

    return score, feedback

# Function to update the UI based on the password strength
def update_password_strength(event):
    password = password_entry.get()
    
    if len(password) == 0:
        strength_label.config(text="Enter a password", foreground="gray")
        strength_bar['value'] = 0
        return
    
    score, feedback = check_password_strength(password)
    
    # Update the strength label and bar color based on the score
    if score == 0:
        strength_label.config(text="Very Weak", foreground="red")
        strength_bar['value'] = 20
        strength_bar_style.configure("red.Horizontal.TProgressbar", background="red")
    elif score == 1:
        strength_label.config(text="Weak", foreground="orange")
        strength_bar['value'] = 40
        strength_bar_style.configure("orange.Horizontal.TProgressbar", background="orange")
    elif score == 2:
        strength_label.config(text="Moderate", foreground="yellow")
        strength_bar['value'] = 60
        strength_bar_style.configure("yellow.Horizontal.TProgressbar", background="yellow")
    elif score == 3:
        strength_label.config(text="Strong", foreground="green")
        strength_bar['value'] = 80
        strength_bar_style.configure("green.Horizontal.TProgressbar", background="green")
    else:
        strength_label.config(text="Very Strong", foreground="#00ff00")
        strength_bar['value'] = 100
        strength_bar_style.configure("green.Horizontal.TProgressbar", background="#00ff00")
    
    feedback_label.config(text=feedback)

# GUI for Mrz
root = tk.Tk()
root.title("Mrz - Advanced Password Strength Checker")
root.geometry("400x300")
root.config(bg="#1c1c1c")

# Style for the progress bar
strength_bar_style = ttk.Style()
strength_bar_style.theme_use('default')
strength_bar_style.configure("TProgressbar", thickness=25)

# Entry field for password input
password_label = tk.Label(root, text="Enter your password:", bg="#1c1c1c", fg="#ffffff", font=("Arial", 12))
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 14), width=30, bg="#333333", fg="#ffffff", insertbackground="#ffffff")
password_entry.pack(pady=10)
password_entry.bind("<KeyRelease>", update_password_strength)

# Password strength label
strength_label = tk.Label(root, text="Enter a password", bg="#1c1c1c", fg="gray", font=("Arial", 12))
strength_label.pack(pady=5)

# Password strength progress bar
strength_bar = ttk.Progressbar(root, style="TProgressbar", orient="horizontal", length=300, mode="determinate")
strength_bar.pack(pady=10)

# Feedback label for password suggestions
feedback_label = tk.Label(root, text="", bg="#1c1c1c", fg="#00ffcc", font=("Arial", 10), wraplength=300)
feedback_label.pack(pady=10)

# Run the main loop
root.mainloop()
