import tkinter as tk

def click(value):
    """Handles button clicks"""
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear():
    """Clears the entry field"""
    entry_var.set("")

def calculate(event=None):  # event=None allows both button and Enter key to work
    """Evaluates the expression safely"""
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except ZeroDivisionError:
        entry_var.set("Error")
    except:
        entry_var.set("Invalid")

def backspace():
    """Removes last character"""
    current = entry_var.get()
    entry_var.set(current[:-1])

def key_press(event):
    """Handles keyboard input"""
    key = event.keysym

    if key in "0123456789":  # Numbers
        click(key)
    elif key in ["plus", "KP_Add"]:
        click("+")
    elif key in ["minus", "KP_Subtract"]:
        click("-")
    elif key in ["asterisk", "KP_Multiply"]:
        click("*")
    elif key in ["slash", "KP_Divide"]:
        click("/")
    elif key in ["period", "KP_Decimal"]:
        click(".")
    elif key == "Return":  # Enter key
        calculate()
    elif key == "BackSpace":
        backspace()
    elif key == "Escape":  # Esc key clears everything
        clear()

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#222")

entry_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10, padx=10)

# Button style function for consistency
def make_button(text, row, col, cmd=None, color="#333", fg="white"):
    return tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), bg=color, fg=fg,
                     command=cmd if cmd else lambda: click(text)).grid(row=row, column=col, padx=5, pady=5)

# Button layout (matrix style)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create number and operator buttons
for (text, row, col) in buttons:
    if text == "=":
        make_button(text, row, col, cmd=calculate, color="#0A9396")
    else:
        make_button(text, row, col)

# Backspace button
tk.Button(root, text="⌫", width=5, height=2, font=("Arial", 16), bg="#666", fg="white",
          command=backspace).grid(row=5, column=0, padx=5, pady=5)

# Clear button (spans 3 columns)
tk.Button(root, text="CLEAR", width=17, height=2, font=("Arial", 16), bg="#BB3E03", fg="white",
          command=clear).grid(row=5, column=1, columnspan=3, padx=5, pady=5)

# Bind keyboard keys
root.bind("<Key>", key_press)

root.mainloop()
