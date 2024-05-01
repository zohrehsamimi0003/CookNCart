import tkinter
import mysql.connector
from tkinter import messagebox
from Main_window import Main_window

root = tkinter.Tk()
Back_ground = Main_window(root)

frame = tkinter.Frame(root,bg='#F9EBEA')

def create_account():
    pass

CookNCart = tkinter.Button(
    frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid')
name_label = tkinter.Label(
    frame, text="Name                 ", bg='#AED6F1', font=("Georgia", 12))
name_entry = tkinter.Entry(
    frame,bg='#D2B4DE' ,font=("Georgia", 12))
Email = tkinter.Label(
    frame, text="Email_ID            ", bg='#AED6F1', font=("Georgia", 12))
Email_entry = tkinter.Entry(
    frame,bg='#D2B4DE' , font=("Georgia", 12))
Password_label = tkinter.Label(
    frame, text="Password           ", bg='#AED6F1', font=("Georgia", 12))
Password_entry= tkinter.Entry(
    frame,bg='#D2B4DE' , font=("Georgia", 12))
Meal_Preference = tkinter.Label(
    frame, text="Meal Preference", bg='#AED6F1', font=("Georgia", 12))
Meal_preference_entry= tkinter.Entry(
    frame,bg='#D2B4DE' , font=("Georgia", 12))
create_account_button = tkinter.Button(
    frame, text="Create",bg='#F5B7B1', font=("Georgia", 14), command=create_account)



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

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.pack(fill=tkinter.BOTH, expand=True)

frame.pack()


root.mainloop()
