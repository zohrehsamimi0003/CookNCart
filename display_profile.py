import tkinter
from tkinter import messagebox
import database
import helpers

class DisplayProfile:
    
    def __init__(self, session):
        self.session = session
        self.main_win = session.main_win
        self.user = session.user
        self.my_db = session.my_db
        self.create_widgets()
    
    def create_widgets(self):    
        self.frame = tkinter.Frame(self.main_win.root,bg='#F9EBEA')

        cook_n_cart = tkinter.Button(
            self.frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25),borderwidth=1,relief='solid',anchor=tkinter.CENTER, command = helpers.cook_n_cart_clicked )
        name_label = tkinter.Label(
            self.frame, text="Name", bg='#AED6F1', font=("Georgia", 12), width=20, anchor="w")
        self.name_var = tkinter.StringVar(value=self.user.name)
        self.name_entry = tkinter.Entry(self.frame,bg='#D2B4DE' ,font=("Georgia", 12), textvariable=self.name_var)

        email = tkinter.Label(
            self.frame, text="Email_ID", bg='#AED6F1', font=("Georgia", 12), width=20, anchor="w")
        email_var = tkinter.StringVar(value=self.user.email)
        self.email_entry = tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12), textvariable=email_var, state="readonly")
        password_label = tkinter.Label(
            self.frame, text="Password", bg='#AED6F1', font=("Georgia", 12), width=20, anchor="w")
        self.password_var = tkinter.StringVar(value=self.user.password)
        self.password_entry= tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12),textvariable=self.password_var)
        meal_preference = tkinter.Label(    
            self.frame, text="Meal Preference", bg='#AED6F1', font=("Georgia", 12),  width=20, anchor="w")
        self.meal_pre_var = tkinter.StringVar(value=self.user.diet_type)
        self.meal_preference_entry= tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12), textvariable = self.meal_pre_var)
        update_account_button = tkinter.Button(
            self.frame, text="Update",bg='#F5B7B1', font=("Georgia", 11), command=self.update_button_clicked)


        # Place widgets on screen
        cook_n_cart.grid(row=0, column=0, columnspan=3, sticky="nw",padx=40, pady=40) 
        name_label.grid(row=1,column=0,pady=30,ipadx=20,ipady=10)
        self.name_entry.grid(row=1,column=1,pady=20,ipadx=100,ipady=10)
        email.grid(row=2, column=0,pady=30,ipadx=20,ipady=10)
        self.email_entry.grid(row=2, column=1, pady=20,ipadx=100,ipady=10)
        password_label.grid(row=3, column=0,pady=30,ipadx=20,ipady=10)  
        self.password_entry.grid(row=3, column=1, pady=20,ipadx=100,ipady=10)  
        meal_preference.grid(row=4, column=0, pady=30,ipadx=20,ipady=10)
        self.meal_preference_entry.grid(row=4, column=1,columnspan=3,pady=10,ipadx=100,ipady=10)
        update_account_button.grid(row=5, column=1, padx=50, pady=10,ipadx=20,ipady=10, sticky="se")  # Place the button in the bottom-right corner

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True)

    def update_button_clicked(self):
        """Get updated values from entry boxes."""
        new_name = self.name_var.get()
        new_password = self.password_var.get()
        new_diet_type = self.meal_pre_var.get()

        # Update database and user object with new values. 
        rowcount = self.my_db.update_user(self.user.email, new_name, new_password, new_diet_type)
        if rowcount == 1:
            self.user.update_user_data(new_name, new_password, new_diet_type)
            tkinter.messagebox.showinfo("Update", "Data updated successfully!")
            #helpers.cook_n_cart_clicked(self.session)
        else:
            tkinter.messagebox.showerror("Database Connection Error. Please try again.")


    def profile_button_clicked(self):
        helpers.profile_btn_screen_change(self.frame, self.session)

    def log_off_button_clicked(self):
        helpers.log_off_btn_screen_change(self.frame, self.session)

        
         