import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
press = tk.Button(text='please')
press.pack()
window.mainloop()