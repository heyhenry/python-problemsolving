import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter!")
greeting.pack()
wassup = tk.Label(
    text = "Wassup bro?",
    foreground='pink',
    background='yellow'
)
wassup.pack()

window.mainloop()