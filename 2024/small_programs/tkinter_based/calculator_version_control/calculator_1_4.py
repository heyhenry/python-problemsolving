import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_calc()
        self.overall_num = 0

    def create_calc(self):

        self.title("Calculator App Ver.1.4")
        self.geometry("320x500")

        self.display_frame = tk.Frame(self)
        self.display_frame.pack()

        self.input_frame = tk.Frame(self)
        self.input_frame.pack()

        self.result_var = tk.IntVar(self.display_frame)
        self.output = tk.Label(self.display_frame, textvariable=self.result_var)
        self.output.pack()

        numpad_one = tk.Button(self.input_frame, text='1', command=lambda: self.add_num(1))
        numpad_two = tk.Button(self.input_frame, text='2', command=lambda: self.add_num(2))
        numpad_three = tk.Button(self.input_frame, text='3', command=lambda: self.add_num(3))
        calculate_btn = tk.Button(self.input_frame, text='Calculate', command=self.calculate)

        numpad_one.grid(row=0, column=0)
        numpad_two.grid(row=0, column=1)
        numpad_three.grid(row=0, column=2)
        calculate_btn.grid(row=1, columnspan=3)
        

    def add_num(self, num):
        self.overall_num += num

        # update the result_var in realtime
        self.result_var.set(self.overall_num)

    def calculate(self):
        self.result_var.set(self.overall_num)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
