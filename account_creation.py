
import tkinter
import user
import database
import welcome_screen
import start_app

# import mysql.connector
# from tkinter import messagebox
# import main_window

class AccountCreation:
    my_db = database.Database()
# root = tkinter.Tk()
    # Back_ground = main_window.MainWindow(root)

    def __init__(self,main_win):
        self.main_win = main_win
        self.create_widgets()
    
    def create_widgets(self):    
        self.frame = tkinter.Frame(self.main_win.root,width=1000, height=1000, bg='#F9EBEA')

        CookNCart = tkinter.Button(
            self.frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid', command = self.cook_n_cart_button)
        name_label = tkinter.Label(
            self.frame, text="Name                 ", bg='#AED6F1', font=("Georgia", 12))
        self.name_entry = tkinter.Entry(
            self.frame,bg='#D2B4DE' ,font=("Georgia", 12))
        Email = tkinter.Label(
            self.frame, text="Email_ID            ", bg='#AED6F1', font=("Georgia", 12))
        self.Email_entry = tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12))
        Password_label = tkinter.Label(
            self.frame, text="Password           ", bg='#AED6F1', font=("Georgia", 12))
        self.Password_entry= tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12))
        Meal_Preference = tkinter.Label(
            self.frame, text="Meal Preference", bg='#AED6F1', font=("Georgia", 12))
        self.Meal_preference_entry= tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12))
        create_account_button = tkinter.Button(
            self.frame, text="Create",bg='#F5B7B1', font=("Georgia", 12), 
                              command = lambda: self.handle_user_creation(self.create_button_clicked()))



        # Place widgets on screen
        CookNCart.grid(row=0, column=2, columnspan=3, sticky="ne", padx=20, pady=20)
        name_label.grid(row=1, column=0, pady=30, padx=20, sticky="e")  # Adjusted padx and sticky
        self.name_entry.grid(row=1, column=1, pady=30, padx=20, sticky="w")  # Adjusted padx and sticky
        Email.grid(row=2, column=0, pady=30, padx=20, sticky="e")  # Adjusted padx and sticky
        self.Email_entry.grid(row=2, column=1, pady=30, padx=20, sticky="w")  # Adjusted padx and sticky
        Password_label.grid(row=3, column=0, pady=30, padx=20, sticky="e")  # Adjusted padx and sticky
        self.Password_entry.grid(row=3, column=1, pady=30, padx=20, sticky="w")  # Adjusted padx and sticky
        Meal_Preference.grid(row=0, column=0, pady=30, padx=20, sticky="e")  # Adjusted padx and sticky
        self.Meal_preference_entry.grid(row=0, column=1, pady=30, padx=20, sticky="w")  # Adjusted padx and sticky
        create_account_button.grid(row=0, column=2, padx=20, pady=(10,5), sticky="se")  # Place the button in the bottom-right corner

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True, side = 'top')
        
   
        
        
    def create_button_clicked(self):
        """Check for duplicate user based on email."""
        name = self.name_entry.get()
        mail = self.Email_entry.get()
        pwd = self.Password_entry.get()
        meal = self.Meal_preference_entry.get()
        user1 = self.my_db.check_if_user_exists(mail) #duplicacy check based on email. currently we are doing
        return user1
        
    def handle_user_creation(self, user1):
        if user1 is None:
            name = self.name_entry.get()
            mail = self.Email_entry
            pwd = self.Password_entry
            meal = self.Password_entry
            rowcount = self.my_db.insert_user(name, mail, pwd, meal)
            if rowcount == 1:
                tkinter.messagebox.showinfo("Account Created", "Account Successfully Created.")
                user1_tuple = self.login_validation (mail, pwd )
                create_user_obj = user.User(user1_tuple)
                self.clear_and_add_widgets()
                welcome_screen.WelcomeScreen(self.main_win, create_user_obj)             
    
            else:
                tkinter.messagebox.showerror("Error", "Failed to create account.")    
        elif user1 is False:
            tkinter.messagebox.showerror("Error", "Database Connection Error.")
        else:                
            tkinter.messagebox.showerror("Error","User already exist.")

    
    def clear_and_add_widgets(self):
        # Clear widgets from main window
        for widget in self.frame.winfo_children():
            widget.destroy()
        
    def cook_n_cart_button(self):
        # Clear widgets from main window
        self.clear_and_add_widgets()
        start_app.StartApplication(self.main_win)
