import tkinter as tk

window=tk.Tk()
window.title("tk")
window.geometry("300x150")

def hello():
    label.config(text='Hello')

label = tk.Label(window, text="")
label.pack()


    

button = tk.Button(window, text="Click me", command=hello)
button.pack(pady=50)




window.mainloop()