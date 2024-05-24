import tkinter as tk

window = tk.Tk()
window.title("Calculator App")

# variables
calculations = ''
data = tk.StringVar()

# params
btn_params = {'font':('sans-serif',16), 'relief': 'groove'}

def on_click(char):
    global calculations
    calculations += char
    data.set(calculations)

def del_data():
    global calculations
    calculations = ''
    data.set(calculations)
    
def equal_data():
    global calculations
    result = eval(calculations)
    data.set(result)
    calculations = str(result)

# def add_clicked(char):
#     global calculations
#     calculations += char
#     data.set(calculations)

# def sub_clicked(char):
#     global calculations
#     calculations += char
#     data.set(calculations)

# def times_clicked(char):
#     global calculations
#     calculations += char
#     data.set(calculations)

# input display
data_entry = tk.Entry(window, textvariable=data, borderwidth=5, width=25, font=('sans-serif', 22)).grid(columnspan=3, padx=5, pady=5)

# operators
add_btn = tk.Button(window, btn_params, text='+', command=lambda: on_click('+')).grid(row=1, column=0,sticky='nswe')
sub_btn = tk.Button(window, btn_params, text='-', command=lambda: on_click('-')).grid(row=1, column=1, sticky='nswe')
times_btn = tk.Button(window, btn_params, text='*', command=lambda: on_click('*')).grid(row=1, column=2, sticky='nswe')

# numpad
numpad_one = tk.Button(window, btn_params, text='1', command=lambda: on_click('1')).grid(row=2, column=0, sticky='nswe')
numpad_two = tk.Button(window, btn_params, text='2', command=lambda: on_click('2')).grid(row=2, column=1, sticky='nswe')
numpad_three = tk.Button(window, btn_params, text='3', command=lambda: on_click('3')).grid(row=2, column=2, sticky='nswe')
numpad_four = tk.Button(window, btn_params, text='4', command=lambda: on_click('4')).grid(row=3, column=0, sticky='nswe')
numpad_five = tk.Button(window, btn_params, text='5', command=lambda: on_click('5')).grid(row=3, column=1, sticky='nswe')
numpad_six = tk.Button(window, btn_params, text='6', command=lambda: on_click('6')).grid(row=3, column=2, sticky='nswe')
numpad_seven = tk.Button(window, btn_params, text='7', command=lambda: on_click('7')).grid(row=4, column=0, sticky='nswe')
numpad_eight = tk.Button(window, btn_params, text='8', command=lambda: on_click('8')).grid(row=4, column=1, sticky='nswe')
numpad_nine = tk.Button(window, btn_params, text='9', command=lambda: on_click('9')).grid(row=4, column=2, sticky='nswe')
numpad_ten = tk.Button(window, btn_params, text='0', command=lambda: on_click('0')).grid(row=5, column=1, sticky='nswe')

# del / equal
del_btn = tk.Button(window, btn_params, text='DEL', command=del_data).grid(row=5,column=0, sticky='nswe')
equal_btn = tk.Button(window, btn_params, text='=', command=equal_data).grid(row=5, column=2, sticky='nswe')

window.mainloop()


# [         ]
# [+] [-] [*]
# [1] [2] [3]
# [4] [5] [6]
# [7] [8] [9]
# [d] [0] [=]