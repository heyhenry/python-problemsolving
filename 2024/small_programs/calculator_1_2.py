import tkinter as tk

# global var
overall_num = 0
calculate = True

# initial window setup
window = tk.Tk()
window.title("Calculator App ver.1.2")
window.geometry("320x500")

# frames
display_frame = tk.Frame(window)
input_frame = tk.Frame(window)

# variables
num_var = tk.IntVar(display_frame)
result_var = tk.IntVar(display_frame)

# functions
def add_num(num):
    global overall_num
    overall_num += num

def calculating():
    result_var.set(overall_num)

# display_frame content
output = tk.Label(display_frame, textvariable=result_var)

# input_frame content
numpad_one = tk.Button(input_frame, text='1', command=lambda: add_num(1))
numpad_two = tk.Button(input_frame, text='2', command=lambda: add_num(2))
numpad_three = tk.Button(input_frame, text='3', command=lambda: add_num(3))
calculate_btn = tk.Button(input_frame, text="Calculate", command=calculating)

# packaging
display_frame.pack()
input_frame.pack()

output.pack()

numpad_one.grid(row=0, column=0)
numpad_two.grid(row=0, column=1)
numpad_three.grid(row=0, column=2)
calculate_btn.grid(row=1, columnspan=3)

# running
window.mainloop()