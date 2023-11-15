import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0


for button in buttons:
    if button == 'C':
        tk.Button(window, text=button, width=5, height=2, command=clear).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(window, text=button, width=5, height=2, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


window.mainloop()
