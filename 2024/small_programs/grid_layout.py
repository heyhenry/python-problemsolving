# Training Materials: http://tkdocs.com/tutorial/grid.html

# Following training material but without ttk insertion
import tkinter as tk

window = tk.Tk()

content = tk.Frame(window, bg='red')
frame = tk.Frame(content, borderwidth=5, relief='ridge', width=200, height=100)
namelbl = tk.Label(content, text="Name")
name = tk.Entry(content)

onevar = tk.BooleanVar(value=True)
twovar = tk.BooleanVar(value=False)
threevar = tk.BooleanVar(value=True)

one = tk.Checkbutton(content, text='One', variable=onevar, onvalue=True)
two = tk.Checkbutton(content, text='two', variable=twovar, onvalue=True)
three = tk.Checkbutton(content, text='three', variable=threevar, onvalue=True)
ok = tk.Button(content, text='Okay')
cancel = tk.Button(content, text='Cancel')

content.grid(row=0, column=0)
frame.grid(row=0, column=0, columnspan=3, rowspan=2)
namelbl.grid(row=0, column=3, columnspan=2)
name.grid(row=1, column=3, columnspan=2)

one.grid(row=2, column=0)
two.grid(row=2, column=1)
three.grid(row=2, column=2)
ok.grid(row=2, column=3)
cancel.grid(row=2, column=4)

window.mainloop()

# Following training material as per ttk insertion
# from tkinter import *
# from tkinter import ttk

# window = Tk()

# content = ttk.Frame(window)
# frame = ttk.Frame(content, borderwidth=5, relief='ridge', width=200, height=100)
# namelbl = ttk.Label(content, text='Name')
# name = ttk.Entry(content)

# onevar = BooleanVar(value=True)
# twovar = BooleanVar(value=False)
# threevar = BooleanVar(value=True)

# one = ttk.Checkbutton(content, text='One', variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text='Two', variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text='Three', variable=threevar, onvalue=True)
# ok = ttk.Button(content, text='Okay')
# cancel = ttk.Button(content, text="Cancel")

# content.grid(row=0, column=0)
# frame.grid(row=0, column=0, columnspan=3, rowspan=2)
# namelbl.grid(row=0, column=3, columnspan=2)
# name.grid(row=1, column=3, columnspan=2)
# one.grid(row=2, column=0)
# two.grid(row=2, column=1)
# three.grid(row=2, column=2)
# ok.grid(row=2, column=3)
# cancel.grid(row=2, column=4)

# window.mainloop()