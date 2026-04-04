import tkinter as tk

window = tk.Tk()
window.title("Event Driven Demo")
window.geometry("200x200")

label = tk.Label(window, text="Number1")
label.grid(row=0, column=1, padx=10, pady=5)

entry = tk.Entry(window)
entry.grid(row=0, column=2, padx=10, pady=5)

label1 = tk.Label(window, text="Number2")
label1.grid(row=1, column=1, padx=10, pady=5)

entry1 = tk.Entry(window)
entry1.grid(row=1, column=2, padx=10, pady=5)


label2 = tk.Label(window, text="")
label2.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

def add():
    number1 = float(entry.get())
    number2 = float(entry1.get())
    result = number1 + number2
    label2.config(text=result)


button = tk.Button(window, text="Add", command=add)
button.place(x=70, y=100)

window.mainloop()