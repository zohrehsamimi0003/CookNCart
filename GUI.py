import tkinter as tk
from LoginVisuals import LoginVisuals

class GUI(tk.Tk):
    def __init__(self, login_handler):
        super().__init__()
        self.title("Login form")
        self.geometry('500x500')
        self.configure(bg='#FFFFFF')

        self.frame = tk.Frame(self, bg='#FFFFFF')
        self.login_visuals = LoginVisuals(self.frame, login_handler=login_handler)  # Pass the login handler to LoginVisuals
        self.login_visuals.pack()  # Packing LoginVisuals into the frame
        self.frame.pack()