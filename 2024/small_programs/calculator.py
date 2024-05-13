import tkinter as tk

window = tk.Tk()
window.title("Fuck man")
window.geometry("320x500")

num1_var = tk.IntVar(window, '')
num2_var = tk.IntVar(window, '')

def calculate():

    num1 = num1_var.get()
    num2 = num2_var.get()

    result = num1 + num2

    print("The sum is: " + str(result))

first_num = tk.Label(window, text="First Num: ")
num1_entry = tk.Entry(window, textvariable=num1_var)
second_num = tk.Label(window, text="second Num: ")
num2_entry = tk.Entry(window, textvariable=num2_var)
calc_btn = tk.Button(window, text = "Calculate", command=calculate)

first_num.pack()
num1_entry.pack()
second_num.pack()
num2_entry.pack()
calc_btn.pack()

window.mainloop()