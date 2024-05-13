import tkinter as tk

# the window
window = tk.Tk()
window.title("Calculator App ver.1.1")
window.geometry("320x500")

# the frames
display_frame = tk.Frame(window)
input_frame = tk.Frame(window)

# the variables
num1_var = tk.IntVar(display_frame, '')
num2_var = tk.IntVar(display_frame, '')
result_var = tk.IntVar(display_frame)

# functions
def add():
    result_var.set(num1_var.get() + num2_var.get())

def subtract():
    result_var.set(num1_var.get() - num2_var.get())

def multiply():
    result_var.set(num1_var.get() * num2_var.get())

def divide():
    result_var.set(num1_var.get() / num2_var.get())

# display frame
output_label = tk.Label(display_frame, textvariable=result_var)
num1_input = tk.Entry(display_frame, textvariable=num1_var)
num2_input = tk.Entry(display_frame, textvariable=num2_var)
add_btn = tk.Button(input_frame, text="Add", command=add)
subtract_btn = tk.Button(input_frame, text="Subtract", command=subtract) 
multiply_btn = tk.Button(input_frame, text="Multiply", command=multiply)
divide_btn = tk.Button(input_frame, text="Divide", command=divide)

# packing
display_frame.pack()
input_frame.pack()

output_label.pack()

num1_input.pack()
num2_input.pack()

add_btn.pack()
subtract_btn.pack()
multiply_btn.pack()
divide_btn.pack()

# the run
window.mainloop()