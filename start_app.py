import tkinter
from tkinter import messagebox
import user
import database
import account_creation
import welcome_screen

class StartApp:
    my_db = database.Database()
    
    def __init__(self,main_win):
        self.main_win = main_win
        self.create_widgets()
        
    def create_widgets(self):
        # Create frames    
        self.frame1 = tkinter.Frame(self.main_win.root, width=1000, height=500,bg='#F9EBEA')
        self.frame1.pack(side='top')
        self.frame2 = tkinter.Frame(self.main_win.root, width=1000, height=500,bg='#F9EBEA')
        self.frame2.pack(side='top')
        self.frame3 = tkinter.Frame(self.main_win.root, width=1000, height=1000,bg='#F9EBEA')
        self.frame3.pack(side='left')
        self.frame4 = tkinter.Frame(self.main_win.root, width=1000, height=500,bg='#F9EBEA')
        self.frame4.pack(side='top')
        
        # Create widgets
        login_label = tkinter.Label(
            self.frame1, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25) )
        email_label = tkinter.Label(
            self.frame2, text="E-Mail ID", bg='#AED6F1', font=("Georgia", 12))
        self.email_entry = tkinter.Entry(
            self.frame2,bg='#D2B4DE' ,font=("Georgia", 12))
        self.password_entry = tkinter.Entry(
            self.frame2, show="*",bg='#D2B4DE' , font=("Georgia", 12))
        password_label = tkinter.Label(
            self.frame2, text="Password", bg='#AED6F1', font=("Georgia", 12))
        login_button = tkinter.Button(
            self.frame1, text="Login", bg='#F5B7B1', font=("Georgia", 12), 
            command=lambda: self.handle_login(self.login_button_clicked()))
        forgot_pw_button = tkinter.Button(
            self.frame3, text="Forgot Password", bg='#F5B7B1', font=("Georgia", 12))
        create_account_button = tkinter.Button(
            self.frame4, text="Create Account",bg='#F5B7B1', 
                               font=("Georgia", 11),
                                command = self.create_button_clicked)


        # Place widgets on screen
        login_label.grid(row=0, column=0, columnspan=3, sticky="news", pady=40) 
        email_label.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=2, pady=20)
        password_label.grid(row=2, column=0)  
        self.password_entry.grid(row=2, column=2, pady=20)  
        login_button.grid(row=4, column=0, columnspan=2, pady=30)
        forgot_pw_button.grid(row=4, column=1, columnspan=2, pady=30)
        create_account_button.grid(row=0,column=2,padx=10,pady=10, sticky="ne")
        
        
        
    def login_button_clicked(self):
        """Functionality for log in button"""
        mail = self.email_entry.get()
        pwd = self.password_entry.get()
        user1_tuple = self.my_db.login_validation(mail, pwd)
        return user1_tuple
    

    def handle_login(self, user1_tuple):
        """Handles the login success. Creat user object"""
        if user1_tuple is None:
            tkinter.messagebox.showerror("Error", "Invalid email or password")
        elif user1_tuple is False:
            tkinter.messagebox.showerror("Database Connection Error.")
        else:
            tkinter.messagebox.showinfo("Success", "Login successful!")
            create_user_obj = user.User(user1_tuple)
            self.clear_and_add_widgets()
            welcome_screen.WelcomeScreen(self.main_win, create_user_obj)             
    
    def clear_and_add_widgets(self):
        """Clear widgets from main window and switch screen."""
        for widget in self.frame1.winfo_children():
            widget.destroy()
        for widget in self.frame2.winfo_children():
            widget.destroy()
        for widget in self.frame3.winfo_children():
            widget.destroy()
        for widget in self.frame4.winfo_children():
            widget.destroy()
            
        
    def create_button_clicked(self):
        """Clear widgets and switch screen."""
        self.clear_and_add_widgets()         
        account_creation.AccountCreation(self.main_win)
        