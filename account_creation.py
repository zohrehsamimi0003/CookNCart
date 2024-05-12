import tkinter
from user import User
import database
import welcome_screen
import start_app
import helpers

class AccountCreation:

    def __init__(self, session):
        self.session = session
        self.diet_types = self.session.my_db.get_diet_types()
        self.create_widgets()
    
    def create_widgets(self):

        self.frame = tkinter.Frame(self.session.main_win.root,bg='#F9EBEA', width=500,height=500)
        cook_n_cart = tkinter.Button(
            self.frame, text="CookNCart", command= self.back_btn_clicked, bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid')
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
        
        # Create drop down list and set the default selected
        self.selected_diet_type = tkinter.StringVar(self.frame)
        self.selected_diet_type.set(self.diet_types[0])
        diet_type = tkinter.Label(
            self.frame, text="Diet Type", bg='#AED6F1', font=("Georgia", 12), width=20, anchor="w")
        self.diet_type_option= tkinter.OptionMenu(
            self.frame, self.selected_diet_type, *self.diet_types)
        self.diet_type_option.config(bg='#D2B4DE', font=("Georgia", 12), width=15)
        

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
        diet_type.grid(row=4,column=0,pady=30,padx=(200,0),ipadx=20,ipady=10)
        self.diet_type_option.grid(row=4,column=1,padx=(0,200),pady=20,ipadx=20,ipady=10)
        create_account_button.grid(row=5, column=2, padx=20, pady=(10,5), sticky="se")  # Place the button in the bottom-right corner


        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True)
        
        
    def create_button_clicked(self):
        """Check if user exists and call method to create user."""
        mail = self.email_entry.get()
        found_user = self.session.my_db.check_if_user_exists(mail)
        self.handle_user_creation(found_user, mail)
        
    def handle_user_creation(self, found_user, mail):
        """Handle user creation, creation of user object
           and take user to welcome screen."""
        if found_user is None:
            name = self.name_entry.get()
            pwd = self.password_entry.get()
            meal = self.selected_diet_type.get().strip("(),'")
            # try to insert user and return user_id as int
            user_id = self.session.my_db.insert_user(name, mail, pwd, meal)
            if user_id is not None:
                self.session.user = User(user_id, name, pwd, mail, meal)
                helpers.clear_widgets(self.frame)
                welcome_screen.WelcomeScreen(self.session)    
            else:
                tkinter.messagebox.showerror("Error", "Failed to create account.")    
        elif found_user is False:
            tkinter.messagebox.showerror("Error", "Database Connection Error.")
        else:                
            tkinter.messagebox.showerror("Error","User already exist.")

    def back_btn_clicked(self):
        '''Back to the login page.'''
        helpers.clear_widgets(self.frame)
        start_app.StartApp(self.session)
