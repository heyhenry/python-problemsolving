import tkinter as tk

# the CalculatorApp takes in the 'tk.Tk' argument as a means to inherit the tkinter library
class CalculatorApp(tk.Tk):
    # initialise the tkinter calc app
    def __init__(self):
        # super() calls the constructor of the superclass/parentclass (i.e. tk.Tk)
        # .__init__() is to initialise it straight up
        super().__init__()
        self.title("Calculator App Ver.1.3")
        self.geometry("320x500")
        # create_widgets can be called even though the actual function was written afterwards,
        # because python doesn't execute functions immediately after they've been written. 
        # Python executes functions when they are called and you can have your functions in any order inside a class.
        self.create_widgets()
        self.overall_num = 0

    def create_widgets(self):
        # attributes/variables with the self. attached to the beginning, have said self. attached
        # because they are components that will be accessed outside the function call and potentially
        # be modified.
        self.display_frame = tk.Frame(self)
        self.display_frame.pack()

        self.input_frame = tk.Frame(self)
        self.input_frame.pack()

        self.result_var = tk.IntVar(self.display_frame)
        self.output = tk.Label(self.display_frame, textvariable=self.result_var)
        self.output.pack()

        # other attributes/variables such as the numpad buttons are local and will not be accessed, altered
        # or modified outside the function call. 
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

    def calculate(self):
        # result_var can be accessed/utilised here because in Python, 
        # variables and attributes can be accessed within the scope where they are defined, 
        # as well as within any nested scopes.
        # So in this case, result_var can be accessed and modified because it is still within the CalculatorApp class,
        # even if it was created in another function (i.e. create_widgets())
        self.result_var.set(self.overall_num)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()

    