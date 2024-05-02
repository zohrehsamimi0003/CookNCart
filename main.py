import tkinter
import mysql.connector
from tkinter import messagebox
from Database import Database
from datetime import datetime, time
from User import User
#This Must stay in main or whatever file you start on.
# It instanstiates the database
db = Database()

#Wherever you wanto to use methods thataccess the database (here or elsewhere)
#You use it like in the login method below.

def login(email_entry, password_entry):
    user = db.login_validation(email_entry, password_entry)
    if user:
        #Returns the user
        print(user)
        messagebox.showinfo(title="Successfully logged in", message="You are logged in!")
    else:
        messagebox.showinfo(title="Login Error", message="Invalid email or password!")
    
def recipe_test():
    current_time = datetime.now().time()
    breakfast_end = time(10,30)
    lunch_end = time(14,30)

    if current_time < breakfast_end:
        meal_time = "Breakfast"
    elif current_time > breakfast_end and current_time < lunch_end:
        meal_time = "Lunch"
    else:
        meal_time = "Dinner"
    time_of_day_recipe = db.time_of_day_recipe(meal_time)
    print(time_of_day_recipe)

    

def main():

        #login:
    '''email_entry = input("email: ")
    password_entry = input("password: ")

    login(email_entry, password_entry)'''

    #create user:
    username_entry = input("username: ")
    email_entry = input("email: ")
    password_entry = input("password: ")
    diet_type = input("diet type: ")

    db.insert_user(username_entry, email_entry, password_entry, diet_type)

    
    user = User(username_entry, email_entry, password_entry, diet_type)

    #db.insert_user("test_user", "test_user@gmail.com", "testpw", "Vegan")'''

    #delete user:
    '''email_entry = input("email: ")
    db.delete_user(email_entry)'''
    #db.delete_user(test_user

    #update password:
    '''email_entry = input("email: ")
    password_entry = input("password: ")
    db.update_password(email_entry, password_entry)'''


if __name__ == "__main__":
    main()