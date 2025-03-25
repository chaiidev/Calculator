import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.configure(bg="black")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), bd=5, relief=tk.SUNKEN, justify='right', bg="black", fg="white")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

frame = tk.Frame(root, bg="black")
frame.pack()

for row in buttons:
    button_row = tk.Frame(frame, bg="black")
    button_row.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for char in row:
        btn = tk.Button(button_row, text=char, font=("Arial", 18), relief=tk.RAISED, bd=3, width=5, height=2, bg="black", fg="white")
        btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        btn.bind("<Button-1>", on_click)

root.mainloop()
