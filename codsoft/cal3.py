import tkinter as tk
from tkinter import ttk,messagebox


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_variable.get()

        if operation == 1:
            result = num1 + num2
        elif operation == 2:
            result = num1 - num2
        elif operation == 3:
            result = num1 * num2
        elif operation == 4:
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Simple Calculator with Radio Buttons")

num1 = ttk.Label(root, text="Enter first number:")
num1.pack(pady=5)
entry_num1 = ttk.Entry(root)
entry_num1.pack(pady=5)


num2 = ttk.Label(root, text="Enter second number:")
num2.pack(pady=5)
entry_num2 = ttk.Entry(root)
entry_num2.pack(padx=10,pady=5)

operation_variable = tk.IntVar()
operation_variable.set(1)

label_operation = ttk.Label(root, text="Select operation:")
label_operation.pack(padx=10,pady=10)

add = ttk.Radiobutton(root, text="+", variable=operation_variable, value=1)
add.pack()
subtract = ttk.Radiobutton(root, text="-", variable=operation_variable, value=2)
subtract.pack()
multiply = ttk.Radiobutton(root, text="*", variable=operation_variable, value=3)
multiply.pack()
divide = ttk.Radiobutton(root, text="/", variable=operation_variable, value=4)
divide.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

result_label = ttk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()
