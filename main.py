import tkinter
import mysql.connector
from tkinter import messagebox
from Database import Database

window = tkinter.Tk()
window.title("Login form")
window.geometry('500x500')
window.configure(bg='#FFFFFF')

frame = tkinter.Frame(bg='#FFFFFF')

#This Must stay in main or whatever file you start on.
# It instanstiates the database
db = Database()

#Wherever you wanto to use methods thataccess the database (here or elsewhere)
#You use it like in the login method below.

def login():
    email_id = email_entry.get()
    password = password_entry.get()
    user = db.login_validation(email_id, password)
    if user:
        #Returns the user
        print(user)
        messagebox.showinfo(title="Successfully logged in", message="You are logged in!")
    else:
        messagebox.showinfo(title="Login Error", message="Invalid email or password!")
    
def recipe_test():
    random_recipe = db.random_recipe()
    print(random_recipe)

# Create widgets
login_label = tkinter.Label(
    frame, text="Login",bg='#FFFFFF', font=("Arial", 30) )
email_label = tkinter.Label(
    frame, text="E-Mail ID", bg='#FFFFFF', font=("Arial", 16))
email_entry = tkinter.Entry(
    frame, font=("Arial", 16))
password_entry = tkinter.Entry(
    frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#FFFFFF', font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg='#B0C4DE', font=("Arial", 16), command=login)
forgot_pw_button = tkinter.Button(
    frame, text="Forgot Password", bg='#B0C4DE', font=("Arial", 16), command=recipe_test)

# Place widgets on screen
login_label.grid(row=0, column=0, columnspan=3, sticky="news", pady=40) 
email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=2, pady=20)
password_label.grid(row=2, column=0)  
password_entry.grid(row=2, column=2, pady=20)  
login_button.grid(row=4, column=0, columnspan=2, pady=30)
forgot_pw_button.grid(row=4, column=2, columnspan=2, pady=30)

frame.pack()


window.mainloop()
