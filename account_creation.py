import tkinter
# import mysql.connector
# from tkinter import messagebox
# import main_window

class AccountCreation:
# root = tkinter.Tk()
    # Back_ground = main_window.MainWindow(root)

    def __init__(self,main_win):
        self.main_win = main_win
        self.create_widgets()
    
    def create_widgets(self):    
        self.frame = tkinter.Frame(self.main_win.root,bg='#F9EBEA')

        CookNCart = tkinter.Button(
            self.frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid')
        name_label = tkinter.Label(
            self.frame, text="Name                 ", bg='#AED6F1', font=("Georgia", 12))
        name_entry = tkinter.Entry(
            self.frame,bg='#D2B4DE' ,font=("Georgia", 12))
        Email = tkinter.Label(
            self.frame, text="Email_ID            ", bg='#AED6F1', font=("Georgia", 12))
        Email_entry = tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12))
        Password_label = tkinter.Label(
            self.frame, text="Password           ", bg='#AED6F1', font=("Georgia", 12))
        Password_entry= tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12))
        Meal_Preference = tkinter.Label(
            self.frame, text="Meal Preference", bg='#AED6F1', font=("Georgia", 12))
        Meal_preference_entry= tkinter.Entry(
            self.frame,bg='#D2B4DE' , font=("Georgia", 12))
        create_account_button = tkinter.Button(
            self.frame, text="Create",bg='#F5B7B1', font=("Georgia", 12))



        # Place widgets on screen
        CookNCart.grid(row=0, column=0, columnspan=3, sticky="nw",padx=40, pady=40) 
        name_label.grid(row=1,column=0,pady=30,ipadx=20,ipady=10)
        name_entry.grid(row=1,column=1,pady=20,ipadx=20,ipady=10)
        Email.grid(row=2,column=0,pady=30,ipadx=20,ipady=10)
        Email_entry.grid(row=2,column=1,pady=20,ipadx=20,ipady=10)
        Password_label.grid(row=3,column=0,pady=30,ipadx=20,ipady=10)  
        Password_entry.grid(row=3,column=1,pady=20,ipadx=20,ipady=10)  
        Meal_Preference.grid(row=4,column=0,pady=30,ipadx=20,ipady=10)
        Meal_preference_entry.grid(row=4,column=1,pady=20,ipadx=20,ipady=10)
        create_account_button.grid(row=5, column=2, padx=20, pady=(10,5), sticky="se")  # Place the button in the bottom-right corner

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True)

        self.frame.pack()


        # root.mainloop()