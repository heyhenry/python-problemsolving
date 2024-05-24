import tkinter as tk

window = tk.Tk()
window.title("Calculator App")

data = tk.StringVar()
btn_params = {'font':('sans-serif',16), 'relief': 'groove'}

# input display
data_entry = tk.Entry(window, textvariable=data, borderwidth=5, width=25, font=('sans-serif', 22)).grid(columnspan=3, padx=5, pady=5)

# operators
add_btn = tk.Button(window, btn_params, text='+').grid(row=1, column=0,sticky='nswe')
sub_btn = tk.Button(window, btn_params, text='-').grid(row=1, column=1, sticky='nswe')
times_btn = tk.Button(window, btn_params, text='*').grid(row=1, column=2, sticky='nswe')

# numpad
numpad_one = tk.Button(window, btn_params, text='1').grid(row=2, column=0, sticky='nswe')
numpad_two = tk.Button(window, btn_params, text='2').grid(row=2, column=1, sticky='nswe')
numpad_three = tk.Button(window, btn_params, text='3').grid(row=2, column=2, sticky='nswe')
numpad_four = tk.Button(window, btn_params, text='4').grid(row=3, column=0, sticky='nswe')
numpad_five = tk.Button(window, btn_params, text='5').grid(row=3, column=1, sticky='nswe')
numpad_six = tk.Button(window, btn_params, text='6').grid(row=3, column=2, sticky='nswe')
numpad_seven = tk.Button(window, btn_params, text='7').grid(row=4, column=0, sticky='nswe')
numpad_eight = tk.Button(window, btn_params, text='8').grid(row=4, column=1, sticky='nswe')
numpad_nine = tk.Button(window, btn_params, text='9').grid(row=4, column=2, sticky='nswe')
numpad_ten = tk.Button(window, btn_params, text='0').grid(row=5, column=1, sticky='nswe')

# del / equal
del_btn = tk.Button(window, btn_params, text='DEL').grid(row=5,column=0, sticky='nswe')
equal_btn = tk.Button(window, btn_params, text='=').grid(row=5, column=2, sticky='nswe')





window.mainloop()


# [         ]
# [+] [-] [*]
# [1] [2] [3]
# [4] [5] [6]
# [7] [8] [9]
# [d] [0] [=]