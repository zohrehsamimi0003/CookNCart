import tkinter as tk

class LoginVisuals(tk.Frame):
    def __init__(self, parent, login_handler):
        super().__init__(parent, bg='#FFFFFF')  # Set background color of the frame
        self.login_handler = login_handler
        
        self.create_widgets()

    def create_widgets(self):
        self.login_label = tk.Label(self, text="Login",bg='#FFFFFF', font=("Arial", 30))
        self.email_label = tk.Label(self, text="E-Mail ID",bg='#FFFFFF', font=("Arial", 16))
        self.email_entry = tk.Entry(self, font=("Arial", 16))
        self.password_label = tk.Label(self, text="Password",bg='#FFFFFF', font=("Arial", 16))
        self.password_entry = tk.Entry(self, show="*",bg='#FFFFFF', font=("Arial", 16))
        self.login_button = tk.Button(self, text="Login", font=("Arial", 16), command=self.login)

        self.login_label.grid(row=0, column=0, columnspan=2, pady=20)
        self.email_label.grid(row=1, column=0, sticky="e", padx=10)
        self.email_entry.grid(row=1, column=1, padx=10)
        self.password_label.grid(row=2, column=0, sticky="e", padx=10)
        self.password_entry.grid(row=2, column=1, padx=10)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.login_handler(email, password)
