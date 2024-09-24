import tkinter as tk

window = tk.Tk()
window.title("Layouts ver.1.0")

content = tk.Frame(window, bg='red')
frame_one = tk.Frame(content, bg='blue')

title_lbl = tk.Label(frame_one, text='Wakata')

content.grid(row=0, column=0)
frame_one.grid(row=0, column=0)
title_lbl.grid(row=0, column=0)

window.mainloop()


