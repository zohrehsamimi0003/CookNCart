import tkinter
from tkinter import messagebox
from user import User
import database
import account_creation
import welcome_screen


class StartApp:
    
    def __init__(self, main_win, my_db):
        self.main_win = main_win
        self.my_db = my_db
        self.create_widgets()
        
    def create_widgets(self):
        # Create frame
        self.frame = tkinter.Frame(self.main_win.root, width=1000, height=500, bg='#F9EBEA')
        self.frame.pack(side='top')
        
        # Create widgets
        login_label = tkinter.Label(
            self.frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25))
        email_label = tkinter.Label(
            self.frame, text="E-Mail ID", bg='#AED6F1', font=("Georgia", 12))
        self.email_entry = tkinter.Entry(
            self.frame, bg='#D2B4DE', font=("Georgia", 12))
        self.password_entry = tkinter.Entry(
            self.frame, show="*", bg='#D2B4DE', font=("Georgia", 12))
        password_label = tkinter.Label(
            self.frame, text="Password", bg='#AED6F1', font=("Georgia", 12))
        login_button = tkinter.Button(
            self.frame, text="Login", bg='#F5B7B1', font=("Georgia", 12), 
            command=self.login_button_clicked)
        forgot_pw_button = tkinter.Button(
            self.frame, text="Forgot Password", bg='#F5B7B1', font=("Georgia", 12))
        create_account_button = tkinter.Button(
            self.frame, text="Create Account", bg='#F5B7B1', font=("Georgia", 11),
            command=self.create_button_clicked)

        # Place widgets on screen
        login_label.grid(row=0, column=0, columnspan=3, sticky="news", pady=40) 
        email_label.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=2, pady=20)
        password_label.grid(row=2, column=0)  
        self.password_entry.grid(row=2, column=2, pady=20)  
        login_button.grid(row=4, column=0, columnspan=2, pady=30)
        forgot_pw_button.grid(row=4, column=1, columnspan=2, pady=30)
        create_account_button.grid(row=0, column=2, padx=10, pady=10, sticky="ne")
        
    def login_button_clicked(self):
        """Functionality for log in button"""
        mail = self.email_entry.get()
        pwd = self.password_entry.get()
        user_found = self.my_db.login_validation(mail, pwd)
        self.handle_login(user_found)
    
    def handle_login(self, user_found):
        """Handles the login success. Create user object"""
        if user_found is None:
            tkinter.messagebox.showerror("Error", "Invalid email or password")
        elif user_found is False:
            tkinter.messagebox.showerror("Database Connection Error.")
        else:
            tkinter.messagebox.showinfo("Success", "Login successful!")
            user = User(user_found)
            self.clear_and_add_widgets()       
            welcome_screen.WelcomeScreen(self.main_win, self.my_db)  
                
    
    def clear_and_add_widgets(self):
        """Clear widgets from main window and switch screen."""
        self.frame.destroy()
            
    def create_button_clicked(self):
        """Clear widgets and switch screen."""
        self.clear_and_add_widgets()         
        account_creation.AccountCreation(self.main_win, self.my_db)