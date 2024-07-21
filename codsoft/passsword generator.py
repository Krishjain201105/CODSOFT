import random
import string
import tkinter as tk
from tkinter import ttk,messagebox
def passgen(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password



def password_execution():
    try:
        length = int(entry_len.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        password = passgen(length)
        entry_pass.delete(0, tk.END)
        entry_pass.insert(0, password)
    except ValueError as error:
        messagebox.showerror("Invalid Input", str(error))


root = tk.Tk()
root.title("Password Generator")

label= ttk.Label(root, text="Password Length:")
label.grid(row=0, column=0, padx=10, pady=10)

entry_len = ttk.Entry(root)
entry_len.grid(row=0, column=1, padx=10, pady=10)

entry_pass= ttk.Entry(root, width=25)
entry_pass.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

button= ttk.Button(root, text="Generate Password", command=password_execution)
button.grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()
