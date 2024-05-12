import tkinter
from tkinter import messagebox
from user import User
import database
import account_creation
import welcome_screen
from session import Session
import helpers


class StartApp:
    
    def __init__(self, session):
        self.session = session
        self.create_widgets()
        
  
    def login_button_clicked(self):
        """Functionality for log in button"""
        mail = self.email_entry.get()
        pwd = self.password_entry.get()
        user_found = self.session.my_db.login_validation(mail, pwd)
        self.handle_login(user_found)
    
    def handle_login(self, user_found):
        """Handles the login success. Create user object"""
        if user_found is None:
            tkinter.messagebox.showerror("Error", "Invalid email or password")
        elif user_found is False:
            tkinter.messagebox.showerror("Database Connection Error.")
        else:
            tkinter.messagebox.showinfo("Success", "Login successful!")
            self.session.user = User(user_found[0], user_found[1], user_found[2], user_found[3], user_found[4])
            self.set_meal_plans()
            helpers.clear_widgets(self.frame)
            welcome_screen.WelcomeScreen(self.session)  
                       
    def create_button_clicked(self):
        """Clear widgets and switch screen."""
        helpers.clear_widgets(self.frame)     
        account_creation.AccountCreation(self.session)
    


    def set_meal_plans(self):
        meal_plan = self.session.my_db.get_meal_plan_id(self.session.user.user_id)
        if meal_plan is not None:
            meal_plan_id = meal_plan[0]
            self.session.user.meal_plan.breakfast_recipes = self.session.my_db.get_meal_plan_recipe_ids(meal_plan_id, "breakfast")
            self.session.user.meal_plan.lunch_recipes = self.session.my_db.get_meal_plan_recipe_ids(meal_plan_id, "lunch")
            self.session.user.meal_plan.dinner_recipes = self.session.my_db.get_meal_plan_recipe_ids(meal_plan_id, "dinner")


    def create_widgets(self):
        # Create frame
        self.frame = tkinter.Frame(self.session.main_win.root, width=1000, height=500, bg=self.session.main_win.bg)
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
        create_account_button = tkinter.Button(
            self.frame, text="Create Account", bg='#F5B7B1', font=("Georgia", 12),
            command=self.create_button_clicked)

        # Place widgets on screen
        login_label.grid(row=0, column=0, columnspan=3, sticky="news", pady=40) 
        email_label.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=2, pady=20)
        password_label.grid(row=2, column=0)  
        self.password_entry.grid(row=2, column=2, pady=20)  
        login_button.grid(row=4, column=0, columnspan=2, pady=30)
        create_account_button.grid(row=4, column=1, columnspan=2, pady=30)
