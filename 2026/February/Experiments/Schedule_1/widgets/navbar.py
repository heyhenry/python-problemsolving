import customtkinter as ctk

class Navbar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        home_icon = ctk.CTkLabel(self, text="Home", font=("", 18))
        entry_icon = ctk.CTkLabel(self, text="Entry", font=("", 18))

        home_icon.grid(row=0, column=0, padx=10, pady=20)
        entry_icon.grid(row=0, column=1, padx=10, pady=20)

        home_icon.bind("<Button-1>", lambda event: self.controller.show_page("HomePage"))
        entry_icon.bind("<Button-1>", lambda event: self.controller.show_page("EntryPage"))
