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

def add():

    result_var.set(num1_var.get() + num2_var.get())
    
    # testing
    # result = result_var.get()
    # print(result)

# display frame
num1_input = tk.Entry(display_frame, textvariable=num1_var)
num2_input = tk.Entry(display_frame, textvariable=num2_var)
add_btn = tk.Button(input_frame, text="Pookie", command=add)

# packing
display_frame.pack()
input_frame.pack()
num1_input.pack()
num2_input.pack()
add_btn.pack()

# the run
window.mainloop()