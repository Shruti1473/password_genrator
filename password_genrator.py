import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Function to generate a password
def generate_password():
    length = int(length_entry.get())  # Get password length from user input
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Combine character sets based on user selection
    all_characters = ""
    if lowercase_var.get():
        all_characters += lowercase
    if uppercase_var.get():
        all_characters += uppercase
    if digits_var.get():
        all_characters += digits
    if symbols_var.get():
        all_characters += symbols

    # Ensure at least one type is selected
    if not all_characters:
        messagebox.showerror("Error", "Please select at least one character type!")
        return
    
    # Generate the password
    password = "".join(random.choice(all_characters) for _ in range(length))
    
    # Display password in the entry field
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Heading Label
tk.Label(root, text="Random Password Generator", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

# Password Length Input
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#f0f0f0").pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Default length

# Checkboxes for character types
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var, bg="#f0f0f0").pack()
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var, bg="#f0f0f0").pack()
tk.Checkbutton(root, text="Include Numbers", variable=digits_var, bg="#f0f0f0").pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#f0f0f0").pack()

# Generate Password Button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4caf50", fg="white").pack(pady=10)

# Password Output Field
password_entry = tk.Entry(root, width=30, font=("Arial", 12), justify="center")
password_entry.pack(pady=5)

# Copy to Clipboard Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#2196f3", fg="white").pack(pady=5)

# Run the GUI
root.mainloop()
