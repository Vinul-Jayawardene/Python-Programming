import tkinter as tk

window = tk.Tk()
window.title("Student Registration")
window.geometry("400x250")

label = tk.Label(window, text="Student Name")
label.grid(row=0, column=1, padx=10, pady=5)

entry = tk.Entry(window)
entry.grid(row=0, column=2, padx=10, pady=5)

label1 = tk.Label(window, text="Student ID")
label1.grid(row=1, column=1, padx=10, pady=5)

entry1 = tk.Entry(window)
entry1.grid(row=1, column=2, padx=10, pady=5)


label2 = tk.Label(window, text="")
label2.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

def register():
    label2.config(text="Registration Successful")

button = tk.Button(window, text="Register", command=register)
button.place(x=70, y=100)

window.mainloop()