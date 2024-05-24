import tkinter as tk

window = tk.Tk()
window.title("Calculator App")

data = tk.StringVar()

data_entry = tk.Entry(window, textvariable=data, borderwidth=5, width=25, font=('Arial', 22)).grid(columnspan=3, padx=5, pady=5)
add_btn = tk.Button(window, text='+', relief='groove').grid(row=1, column=0,sticky='nswe')
sub_btn = tk.Button(window, text='-', relief='groove').grid(row=1, column=1, sticky='nswe')
times_btn = tk.Button(window, text='*', relief='groove').grid(row=1, column=2, sticky='nswe')





window.mainloop()


# [         ]
# [+] [-] [*]
# [1] [2] [3]
# [4] [5] [6]
# [7] [8] [9]
# [d] [0] [=]