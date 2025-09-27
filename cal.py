# GUI Calculator using Tkinter

import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the entry box
def press(num):
    global expression
    expression += str(num)
    entry_text.set(expression)

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    entry_text.set("")

# Function to calculate the result
def equal():
    global expression
    try:
        result = str(eval(expression))
        entry_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        entry_text.set("")

# Main GUI window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0, 0)

expression = ""
entry_text = tk.StringVar()

# Entry widget for display
entry = tk.Entry(root, textvariable=entry_text, font=('Arial', 20), bd=10, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame for buttons
btns_frame = tk.Frame(root)
btns_frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

# Create buttons dynamically
for r, row in enumerate(buttons):
    for c, btn in enumerate(row):
        if btn == '=':
            tk.Button(btns_frame, text=btn, width=5, height=2, font=('Arial', 18),
                      command=equal).grid(row=r, column=c, padx=5, pady=5)
        elif btn == 'C':
            tk.Button(btns_frame, text=btn, width=32, height=2, font=('Arial', 18),
                      command=clear).grid(row=r, column=0, columnspan=4, padx=5, pady=5)
        else:
            tk.Button(btns_frame, text=btn, width=5, height=2, font=('Arial', 18),
                      command=lambda x=btn: press(x)).grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
