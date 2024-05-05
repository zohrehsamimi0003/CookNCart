import tkinter
import mysql.connector
from tkinter import messagebox
import main_window
import database
import cook_module

class DisplyProfile:
    my_db = database.Database()    
    def __init__(self, main_win, created_user_obj):
        self.main_win = main_win
        self.created_user_obj = created_user_obj
        self.create_widgets()
    
    def create_widgets(self):    
        frame = tkinter.Frame(self.main_win.root,bg='#F9EBEA')

        CookNCart = tkinter.Button(
            frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25),borderwidth=1,relief='solid',anchor=tkinter.CENTER, command = cook_module.cook_n_cart_clicked )
        name_label = tkinter.Label(
            frame, text="Name                 ", bg='#AED6F1', font=("Georgia", 12))
        name_var = tkinter.StringVar(value=self.created_user_obj.name)
        name_entry = tkinter.Entry(frame,bg='#D2B4DE' ,font=("Georgia", 12), textvariable=name_var)

        Email = tkinter.Label(
            frame, text="Email_ID            ", bg='#AED6F1', font=("Georgia", 12))
        email_var = tkinter.StringVar(value=self.created_user_obj.email)
        Email_entry = tkinter.Entry(
            frame,bg='#D2B4DE' , font=("Georgia", 12), textvariable=email_var, state="readonly")
        Password_label = tkinter.Label(
            frame, text="Password           ", bg='#AED6F1', font=("Georgia", 12))
        password_var = tkinter.StringVar(value=self.created_user_obj.password)
        Password_entry= tkinter.Entry(
            frame,bg='#D2B4DE' , font=("Georgia", 12),textvariable=password_var)
        Meal_Preference = tkinter.Label(    
            frame, text="Meal Preference", bg='#AED6F1', font=("Georgia", 12))
        meal_pre_var = tkinter.StringVar(value=self.self.created_user_obj.diet_type)
        Meal_preference_entry= tkinter.Entry(
            frame,bg='#D2B4DE' , font=("Georgia", 12), textvariable = meal_pre_var)
        update_account_button = tkinter.Button(
            frame, text="Update",bg='#F5B7B1', font=("Georgia", 11), command=self.update_button_clicked)



        # Place widgets on screen
        CookNCart.grid(row=0, column=0, columnspan=3, sticky="nw",padx=40, pady=40) 
        name_label.grid(row=1,column=0,pady=30,ipadx=20,ipady=10)
        name_entry.grid(row=1,column=1,pady=20,ipadx=100,ipady=10)
        Email.grid(row=2, column=0,pady=30,ipadx=20,ipady=10)
        Email_entry.grid(row=2, column=1, pady=20,ipadx=100,ipady=10)
        Password_label.grid(row=3, column=0,pady=30,ipadx=20,ipady=10)  
        Password_entry.grid(row=3, column=1, pady=20,ipadx=100,ipady=10)  
        Meal_Preference.grid(row=4, column=0, pady=30,ipadx=20,ipady=10)
        Meal_preference_entry.grid(row=4, column=1,columnspan=3,pady=10,ipadx=100,ipady=10)
        update_account_button.grid(row=5, column=1, padx=50, pady=10,ipadx=20,ipady=10, sticky="se")  # Place the button in the bottom-right corner

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.pack(fill=tkinter.BOTH, expand=True)

    def update_button_clicked(self):
        """Get updated values from entry boxes."""
        new_name = self.name_var.get()
        new_password = self.password_var.get()
        new_diet_type = self.meal_pre_var.get()
        mail = self.email_var.get()

        # Update database and user object with new values. 
        rowcount = self.my_db.change_user_info(mail, new_name, new_password, new_diet_type)
        if rowcount == 1:
            self.created_user_obj.update_user_data(new_name, new_password, new_diet_type)
            tkinter.messagebox.showinfo("Update", "Data updated successfully!")
            cook_module.cook_n_cart_clicked(self.main_win, self.created_user_obj)
        else:
            tkinter.messagebox.showerror("Database Connection Error. Please try later.")

        
         