import tkinter as tk

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

# display_frame content
output = tk.Label(display_frame, textvariable=result_var)

# input_frame content
numpad_one = tk.Button(input_frame, text='1')
numpad_two = tk.Button(input_frame, text='2')
numpad_three = tk.Button(input_frame, text='3')
calculate_btn = tk.Button(input_frame, text="Calculate")

# packaging
display_frame.pack()
input_frame.pack()

output.grid(row=0, column=0, )

numpad_one.grid(row=0, column=0)
numpad_two.grid(row=0, column=1)
numpad_three.grid(row=0, column=2)
calculate_btn.grid(row=1, columnspan=3)

# running
window.mainloop()