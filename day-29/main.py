import tkinter as tk
from tkinter import messagebox
import pyperclip
import random

# -------------------- PASS GEN -------------------- #

def generate_secret(entry):
    n_letters = 8
    n_specials = 5
    n_nums = 5
    
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "!@#$%^&*()"
    
    pwd = []
    
    pwd += [random.choice(letters) for _ in range(n_letters)]
    pwd += [random.choice(special) for _ in range(n_specials)]
    pwd += [random.choice(numbers) for _ in range(n_nums)]
    
    random.shuffle(pwd)
    
    password = "".join(pwd)
            
    entry.delete(0, tk.END)
    entry.insert(0, password)
    pyperclip.copy(password)
    return pwd

def pass_secret():
    generate_secret(ui_secret_input)

# -------------------- SAVE PWD -------------------- #

def save_secrets(entry1, entry2):    
    web = ui_website_input.get()
    mail = ui_user_input.get()
    pwd = ui_secret_input.get()
    
    if len(web) == 0 or len(mail) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    
    is_ok = messagebox.askokcancel(title=web, message=f"These are the details: \nEmail: {mail}"
                                                      f"\nPassword: {pwd}\nIs it okay to save?")
    
    if is_ok:
        with open("data.txt", 'a') as f:
            f.write(f"{web} | {mail} | {pwd}\n")
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
    
def save_and_discard_inputs():
    save_secrets(ui_website_input, ui_secret_input)

# -------------------- UI SETUP -------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")
window.minsize(650, 525)
window.maxsize(650, 525)

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, sticky="e")

# Labels
ui_label_1 = tk.Label(text="Website:", font=("Adwaita Sans", 11, "bold"), bg="white", padx=25, pady=5)
ui_label_1.grid(row=1, column=0)

ui_label_2 = tk.Label(text="Email/Username:", font=("Adwaita Sans", 11, "bold"), bg="white", padx=25, pady=5)
ui_label_2.grid(row=2, column=0)

ui_label_3 = tk.Label(text="Password:", font=("Adwaita Sans", 11, "bold"), bg="white", padx=25, pady=5)
ui_label_3.grid(row=3, column=0)

# Input
ui_website_input = tk.Entry(width=50)
ui_website_input.grid(row=1, column=1, columnspan=2)
ui_website_input.focus()

ui_user_input = tk.Entry(width=50)
ui_user_input.grid(row=2, column=1, columnspan=2)
ui_user_input.insert(0, "numair@email.com")

ui_secret_input = tk.Entry(width=25)
ui_secret_input.grid(row=3, column=1, sticky="w")

# Buttons
ui_generate_button = tk.Button(text="Generate Password", width=10, bg="white", padx=30, pady=5, command=pass_secret)
ui_generate_button.grid(row=3, column=2, sticky="e")

ui_add_button = tk.Button(text="Add", width=44, bg="white", padx=25, pady=5, command=save_and_discard_inputs)
ui_add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()