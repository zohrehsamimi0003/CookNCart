import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Main_Window_Update import MainWindow

# Create widgets
root = tk.Tk()
Back_ground = MainWindow(root)

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

# Maximum window size (width, height)
root.maxsize(1000, 800)

# Define a style dictionary for buttons
button_style = {
    'font': ("Algerian", 16),
    'bg': 'tan4',
    'fg': 'black',
    'padx': 40,
    'pady': 10,
    'width': 15,
    'relief': tk.RAISED,
    'borderwidth': 6
}

# Create frame and buttons
frame = tk.Frame(root, bg='#F9EBEA')
CookNCart = tk.Button(frame, text="CookNCart", bg='#D2B4DE', font=("Verdana", 24), width=1, relief=tk.RAISED, borderwidth=0)
Meal_planner_label = tk.Button(frame, text="Meal Planner", **button_style, command=Meal_planner)
Search_recipe_label = tk.Button(frame, text="Search Recipe", **button_style, command=Search_recipe)
Timed_recipe_label = tk.Button(frame, text="Timed Recipe", **button_style, command=Timed_recipe)
log_off_button = tk.Button(frame, text="Log Off", bg='#db7070', fg='white', command=log_off, width=30, borderwidth=1)
profile_button = tk.Button(frame, text="Profile", bg='#db7070', fg='white', command=Profile, width=30, borderwidth=1)

# Create descriptive labels next to each button
description_label_mp = tk.Label(frame, text="Plan your meals for the week here.", bg='#F9EBEA', font=("Verdana", 12), justify='left', width=40)
description_label_sr = tk.Label(frame, text="Best match for your ingredients.", bg='#F9EBEA', font=("Verdana", 12), justify='left', width=40)
description_label_tr = tk.Label(frame, text="Let's cook for Lunch/Dinner?", bg='#F9EBEA', font=("Verdana", 12), justify='left', width=40)

# Position the buttons and labels
Meal_planner_label.grid(row=2, column=0, pady=20, padx=35, ipadx=50, ipady=20, sticky='w')
Search_recipe_label.grid(row=3, column=0, pady=20, padx=35, ipadx=50, ipady=20, sticky='w')
Timed_recipe_label.grid(row=4, column=0, pady=20, padx=35, ipadx=50, ipady=20, sticky='w')

description_label_mp.grid(row=2, column=1, padx=10, pady=20, sticky='w')
description_label_sr.grid(row=3, column=1, padx=10, pady=20, sticky='w')
description_label_tr.grid(row=4, column=1, padx=10, pady=20, sticky='w')

log_off_button.grid(row=0, column=1, sticky="ne", padx=10, pady=(0, 0), ipadx=10, ipady=10)
profile_button.grid(row=0, column=2, sticky="ne", padx=10, pady=(0, 0), ipadx=10, ipady=10)

# Configure columns
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Pack the frame
frame.pack(fill=tk.BOTH, expand=True, anchor='n', padx=0, pady=0)

root.mainloop()
