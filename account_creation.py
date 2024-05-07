import tkinter
from user import User
import database
import welcome_screen
import start_app
import helpers

class AccountCreation:

    def __init__(self, session):
        self.session = session
        self.main_win = session.main_win
        self.my_db = session.my_db
        self.create_widgets()
    
    def create_widgets(self):    

        self.frame = tkinter.Frame(self.main_win.root,bg='#F9EBEA', width=500,height=500)
        cook_n_cart = tkinter.Button(
            self.frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid')
        name_label = tkinter.Label(
            self.frame, text="Name", bg='#AED6F1', font=("Georgia", 12), width=20, anchor="w")
        self.name_entry = tkinter.Entry(
            self.frame,bg='#D2B4DE' ,font=("Georgia", 12))
        email = tkinter.Label(
            self.frame, text="Email_ID", bg='#AED6F1', font=("Georgia", 12), width=20, anchor="w")
        self.email_entry = tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12))
        password_label = tkinter.Label(
            self.frame, text="Password", bg='#AED6F1', font=("Georgia", 12), width=20, anchor="w")
        self.password_entry= tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12))
        meal_preference = tkinter.Label(
            self.frame, text="Meal Preference", bg='#AED6F1', font=("Georgia", 12), width=20, anchor="w")
        self.meal_preference_entry= tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12), width=20)
        create_account_button = tkinter.Button(
            self.frame, text="Create",bg='#F5B7B1', font=("Georgia", 12), command=self.create_button_clicked)


        # Place widgets on screen
        cook_n_cart.grid(row=0, column=0, columnspan=3, sticky="nw",padx=40, pady=40) 
        name_label.grid(row=1,column=0,padx=(200,0),pady=30,ipadx=20,ipady=10)
        self.name_entry.grid(row=1,column=1,padx=(0,200),pady=20,ipadx=20,ipady=10)
        email.grid(row=2,column=0,pady=30,padx=(200,0),ipadx=20,ipady=10)
        self.email_entry.grid(row=2,column=1,pady=20,padx=(0,200),ipadx=20,ipady=10)
        password_label.grid(row=3,column=0,pady=30,padx=(200,0),ipadx=20,ipady=10)  
        self.password_entry.grid(row=3,column=1,padx=(0,200),pady=20,ipadx=20,ipady=10)  
        meal_preference.grid(row=4,column=0,pady=30,padx=(200,0),ipadx=20,ipady=10)
        self.meal_preference_entry.grid(row=4,column=1,padx=(0,200),pady=20,ipadx=20,ipady=10)
        create_account_button.grid(row=5, column=2, padx=20, pady=(10,5), sticky="se")  # Place the button in the bottom-right corner


        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True)
        
        
    def create_button_clicked(self):
        """Check for duplicate user based on email."""
        mail = self.email_entry.get()
        found_user = self.my_db.check_if_user_exists(mail) #duplicacy check based on email. currently we are doing
        self.handle_user_creation(found_user, mail)
        
    def handle_user_creation(self, found_user, mail):
        """Handles user creation, creation of user object
           and take the user to welcom screen."""
        if found_user is None:
            name = self.name_entry.get()
            pwd = self.password_entry.get()
            meal = self.meal_preference_entry.get()
            rowcount = self.my_db.insert_user(name, mail, pwd, meal)
            if rowcount == 1:
                tkinter.messagebox.showinfo("Account Created", "Account Successfully Created.")
                self.session.user = User(name, mail, pwd, meal)
                helpers.clear_widgets(self.frame)
                welcome_screen.WelcomeScreen(self.session)

    
            else:
                tkinter.messagebox.showerror("Error", "Failed to create account.")    
        elif found_user is False:
            tkinter.messagebox.showerror("Error", "Database Connection Error.")
        else:                
            tkinter.messagebox.showerror("Error","User already exist.")

    
    #def cook_n_cart_button(self):
        #"""Clear widgets from main window & switches screen"""
        #helpers.clear_widgets()
        #start_app.StartApp(self.session)

    def clear_and_add_widgets(self):
        """Clear widgets from main window and switch screen."""
        self.frame.destroy()

    def back_btn_clicked(self):
        helpers.clear_widgets(self.frame)
        start_app.StartApp(self.session)
