import customtkinter as ctk
from widgets import Navbar

class Windows(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Schedule 1 | Customers")
        self.geometry("600x600")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = ctk.CTkFrame(self)
        container.grid(row=0, column=0, sticky="nswe")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}

        page_classes = {
            "HomePage": HomePage,
            "EntryPage": EntryPage
        }

        for page_name, P in page_classes.items():
            page = P(container, self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nswe")

    def show_page(self, selected_page):
        page = self.pages[selected_page]

        page.tkraise()

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        navbar = Navbar(self, self.controller)
        content = ctk.CTkFrame(self)

        navbar.grid(row=0, column=0, sticky="nswe")
        content.grid(row=1, column=0, sticky="nswe")

        content.grid_rowconfigure(0, weight=1)
        content.grid_rowconfigure(2, weight=1)
        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)

        content_title = ctk.CTkLabel(content, text="Home Page", font=("", 32, "bold"))

        content_title.grid(row=0, column=0)
        
class EntryPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        navbar = Navbar(self, self.controller)
        content = ctk.CTkFrame(self)

        navbar.grid(row=0, column=0, sticky="nswe")
        content.grid(row=1, column=0, sticky="nswe")

        content.grid_rowconfigure(0, weight=1)
        content.grid_rowconfigure(2, weight=1)
        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)

        entry_title = ctk.CTkLabel(content, text="Enter Customer Info", font=("", 32, "bold"))

        entry_title.grid(row=0, column=0)

if __name__ == "__main__":
    app = Windows()
    app.mainloop()