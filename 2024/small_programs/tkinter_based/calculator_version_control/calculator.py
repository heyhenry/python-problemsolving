import tkinter as tk

window = tk.Tk()
window.title("My Calculator")
window.geometry("320x500")

calc_operator = ""
user_input = tk.StringVar()
result_var = tk.StringVar()

def on_press(char):
    global calc_operator
    calc_operator += str(char)
    user_input.set(calc_operator)

def on_add(char):
    global calc_operator
    calc_operator += str(char)
    user_input.set(calc_operator)

def equal():
    print(calc_operator)
    temp = eval(calc_operator) 
    print(temp)
    

input_label = tk.Label(window, text='Input: ')
input_entry = tk.Entry(window, textvariable=user_input)
numpad_one = tk.Button(window, text='1', command=lambda:on_press('1'))
numpad_two = tk.Button(window, text='2', command=lambda:on_press('2'))
add_btn = tk.Button(window, text='+', command=lambda:on_add('+'))
equal_btn = tk.Button(window, text='=', command=equal)

input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
numpad_one.grid(row=1, column=0)
numpad_two.grid(row=1, column=1)
add_btn.grid(row=2, columnspan=2)
equal_btn.grid(row=3, columnspan=2)

window.mainloop()