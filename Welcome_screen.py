import tkinter
import mysql.connector
from tkinter import messagebox
from Main_window import Main_window

root = tkinter.Tk()
Back_ground = Main_window(root)

frame = tkinter.Frame(root, bg='#F9EBEA')

def Meal_planner():
    pass

def Search_recipe():
    pass

def Timed_recipe():
    pass

def log_off():
    pass

def Profile():
    pass

CookNCart = tkinter.Button(
    frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25))
Meal_planner_label = tkinter.Button(
    frame, text="Meal Planner", bg='#D2B4DE', font=("Georgia", 12), command=Meal_planner)
Search_recipe_label = tkinter.Button(
    frame, text="Search Recipe", bg='#D2B4DE', font=("Georgia", 12), command=Search_recipe)
Timed_recipe_label = tkinter.Button(
    frame, text="Timed Recipe", bg='#D2B4DE', font=("Georgia", 12), command=Timed_recipe)
log_off_button = tkinter.Button(
    frame, text="Log Off", bg='#F5B7B1', font=("Georgia", 11), command=log_off)
profile_button = tkinter.Button(
    frame, text="Profile", bg='#F5B7B1', font=("Georgia", 11), command=Profile)

CookNCart.grid(row=0, column=0, columnspan=3, sticky="nw", padx=40, pady=40)
Meal_planner_label.grid(row=1, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
Search_recipe_label.grid(row=2, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
Timed_recipe_label.grid(row=3, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
log_off_button.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
profile_button.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.pack(fill=tkinter.BOTH, expand=True)

root.mainloop()
