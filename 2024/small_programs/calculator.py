import tkinter as tk

window = tk.Tk()
window.title("Calculator App")
window.geometry("320x500")

add_frame = tk.Frame(window)
subtract_frame = tk.Frame(window)

add_num1_var = tk.IntVar(add_frame, '')
add_num2_var = tk.IntVar(add_frame, '')

subtract_num1_var = tk.IntVar(subtract_frame, '')
subtract_num2_var = tk.IntVar(subtract_frame, '')

def add():

    num1 = add_num1_var.get()
    num2 = add_num2_var.get()

    result = num1 + num2

    print("(Addition) The result is: " + str(result))

def subtract():

    num1 = subtract_num1_var.get()
    num2 = subtract_num2_var.get()

    result = num1 - num2
    
    print("(Subtraction) The result is: " + str(result))


# add frame

add_label = tk.Label(add_frame, text="Addition")
add_first_num = tk.Label(add_frame, text="First Num: ")
add_num1_entry = tk.Entry(add_frame, textvariable=add_num1_var)
add_second_num = tk.Label(add_frame, text="Second Num: ")
add_num2_entry = tk.Entry(add_frame, textvariable=add_num2_var)
add_btn = tk.Button(add_frame, text = "Calculate", command=add)

# subtract frame

subtract_label = tk.Label(subtract_frame, text="Subtraction")
subtract_first_num = tk.Label(subtract_frame, text="First Num: ")
subtract_num1_entry = tk.Entry(subtract_frame, textvariable=subtract_num1_var)
subtract_second_num = tk.Label(subtract_frame, text="Second Num: ")
subtract_num2_entry = tk.Entry(subtract_frame, textvariable=subtract_num2_var)
subtract_btn = tk.Button(subtract_frame, text="Calcuate", command=subtract)

# add layout
add_frame.pack()
add_label.grid(row=0, column=1)
add_first_num.grid(row=1, column=0)
add_num1_entry.grid(row=1, column=1)
add_second_num.grid(row=2,column=0)
add_num2_entry.grid(row=2,column=1)
add_btn.grid(row=3,column=1)

# subtract layout
subtract_frame.pack()
subtract_label.grid(row=0,column=1)
subtract_first_num.grid(row=1, column=0)
subtract_num1_entry.grid(row=1, column=1)
subtract_second_num.grid(row=2,column=0)
subtract_num2_entry.grid(row=2,column=1)
subtract_btn.grid(row=3,column=1)

window.mainloop()