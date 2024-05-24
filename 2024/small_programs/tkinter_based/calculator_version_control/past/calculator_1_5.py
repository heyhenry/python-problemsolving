import tkinter as tk

class CalcApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_start()
        self.create_widgets()
        self.overall_num = 0

    def create_start(self):
        self.title("Calc App Ver.1.5")
        self.geometry("320x500")

    def create_widgets(self):
        self.display_frame = tk.Frame(self, bg='red', borderwidth=5, relief='ridge', width=300, height=500)
        self.input_frame = tk.Frame(self, bg='blue', borderwidth=5, relief='solid', width=300, height=500)

        self.result_var = tk.IntVar(self.display_frame)
        self.output = tk.Label(self.display_frame, textvariable=self.result_var)
        add_flag = tk.BooleanVar(value=False)
        subtract_flag = tk.BooleanVar(value=False)

        if add_flag:
            numpad_one = tk.Button(self.input_frame, text='1', command=lambda: self.add_num(1))
            numpad_two = tk.Button(self.input_frame, text='2', command=lambda: self.add_num(2))
            numpad_three = tk.Button(self.input_frame, text='3', command=lambda: self.add_num(3))

        elif subtract_flag:
            numpad_one = tk.Button(self.input_frame, text='1', command=lambda: self.sub_num(1))
            numpad_two = tk.Button(self.input_frame, text='2', command=lambda: self.sub_num(2))
            numpad_three = tk.Button(self.input_frame, text='3', command=lambda: self.sub_num(3))

        add_btn = tk.Checkbutton(self.input_frame, text='Add', variable=add_flag, onvalue=True)
        subtract_btn = tk.Checkbutton(self.input_frame, text="Subtract", variable=subtract_flag, onvalue=True)

        self.display_frame.grid(columnspan=3)
        self.input_frame.grid(columnspan=3)
        self.output.grid(row=0, column=0)
        numpad_one.grid(row=1, column=0)
        numpad_two.grid(row=1, column=1)
        numpad_three.grid(row=1, column=2)
        add_btn.grid(row=2, column=0)
        subtract_btn.grid(row=2, column=1)

    def add_num(self, num):
        self.overall_num += num
        self.result_var.set(self.overall_num)

    def sub_num(self, num):
        self.overall_num -= num
        self.result_var.set(self.overall_num)

if __name__ == "__main__":
    app = CalcApp()
    app.mainloop()
