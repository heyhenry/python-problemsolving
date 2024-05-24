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

# operators
add_btn = tk.Button(input_frame, text="Add", command=add)
subtract_btn = tk.Button(input_frame, text="Subtract", command=subtract) 
multiply_btn = tk.Button(input_frame, text="Multiply", command=multiply)
divide_btn = tk.Button(input_frame, text="Divide", command=divide)

# packing
display_frame.pack(padx=10, pady=10)
input_frame.pack()

output_label.grid(row=0, column=0, columnspan=2)

num1_input.grid(row=1, column=0, padx=5)
num2_input.grid(row=1, column=1, padx=5)

add_btn.grid(row=0, column=0)
subtract_btn.grid(row=0, column=1)
multiply_btn.grid(row=0, column=2)
divide_btn.grid(row=0, column=3)

# the run
window.mainloop()


# What to do next time on

# 1.0 Change intvar to stringvar
# 2.0 Create validate input function to ensure its an accepted int/float
# 2.1 Ensure error message is given if input is invalid
# 3.0 Add additional design considerations to existing content


# future considerations/implementations
# force the usage of displayed number buttons in lieu of keyboard inputs
# provide continuious inputs (not limited to current 2 numbers)