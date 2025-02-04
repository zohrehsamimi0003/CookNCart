
import tkinter 
import meal_planner
import random_recipe
import search_recipe
import helpers
import start_app
from datetime import datetime
import session
from main_window import MainWindow

class WelcomeScreen:
    def __init__(self, session):
        self.session = session
        self.main_win = session.main_win
        self.my_db = session.my_db
        self.create_widgets()
    
    def meal_planner_button_clicked(self):
       '''Go to meal planner page.'''
       helpers.clear_widgets(self.frame)
       meal_planner.MealPlanner(self.session)

    def random_recipe_button_clicked(self):
        '''Go to random recipe page.'''
        '''now = datetime.now()
        current_time = now.time()   
        if current_time <= datetime.strptime('10:30', '%H:%M').time():
            period_of_day = "breakfast"
        elif current_time <= datetime.strptime('14:30', '%H:%M').time():
            period_of_day = "Lunch"
        else:
            period_of_day = "Dinner"
         period_of_day)'''                  
        helpers.clear_widgets(self.frame)
        random_recipe.RandomRecipe(self.session)

    def search_recipe_button_clicked(self):
        '''Go to search recipe page.'''
        helpers.clear_widgets(self.frame)
        search_recipe.SearchRecipe(self.session)

    def profile_button_clicked(self):
        '''Go to profile page.'''
        helpers.profile_btn_screen_change(self.frame, self.session)

    def log_off_button_clicked(self):
        '''Log off acount and go to login page.'''
        helpers.log_off_btn_screen_change(self.frame, self.session)
    
    def create_widgets(self):
        
        self.frame = tkinter.Frame(self.main_win.root, width=1280, height=720, bg=self.main_win.bg)
        self.frame.place(x=0, y=0)
        button_style = {
            'font': ("Algerian", 16),
            'bg': 'tan4',
            'fg': 'black',
            'padx': 40,
            'pady': 10,
            'width': 15,
            'relief': tkinter.RAISED,
            'borderwidth': 2
        }


        Meal_planner_label = tkinter.Button(
            self.frame, text="Meal Planner", **button_style, command=self.meal_planner_button_clicked)
        Search_recipe_label = tkinter.Button(
            self.frame, text="Search Recipe", **button_style, command=self.search_recipe_button_clicked)
        Random_recipe_label = tkinter.Button(
            self.frame, text="Random Recipe", **button_style, command=self.random_recipe_button_clicked)
        log_off_button = tkinter.Button(
            self.frame, text="Log Off", bg='#8b5a2b',fg='white', font=("Georgia", 11), borderwidth=1,command=self.log_off_button_clicked)
        profile_button = tkinter.Button(
            self.frame, text="Profile", bg='#8b5a2b',fg='white', font=("Georgia", 11), borderwidth=1, command=self.profile_button_clicked)

        # Position the buttons and labels
        Meal_planner_label.grid(row=2, column=0, pady=(100,20), padx=35, ipadx=50, ipady=20, sticky='w')
        Search_recipe_label.grid(row=3, column=0, pady=20, padx=35, ipadx=50, ipady=20, sticky='w')
        Random_recipe_label.grid(row=4, column=0, pady=20, padx=35, ipadx=50, ipady=20, sticky='w')
        # Create descriptive labels next to each button
        description_label_mp = tkinter.Label(self.frame, text="Plan your meals for the week here.", bg=self.main_win.bg, font=("Verdana", 12), justify='left', width=40)
        description_label_sr = tkinter.Label(self.frame, text="Best match for your ingredients.", bg=self.main_win.bg, font=("Verdana", 12), justify='left', width=40)
        description_label_tr = tkinter.Label(self.frame, text="Let's cook for Lunch/Dinner?", bg=self.main_win.bg, font=("Verdana", 12), justify='left', width=40)

        
        log_off_button.grid(row=0, column=1, sticky="ne", padx=10, pady=(0,20), ipadx=20,ipady=10)
        profile_button.grid(row=0, column=2, sticky="ne", padx=10, pady=(0,20), ipadx=20, ipady=10)
        description_label_mp.grid(row=2, column=1, padx=10, pady=(10,20), sticky='w')
        description_label_sr.grid(row=3, column=1, padx=10, pady=20, sticky='w')
        description_label_tr.grid(row=4, column=1, padx=10, pady=20, sticky='w')


        self.frame.pack(fill=tkinter.BOTH, expand=True, side='top')

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        # Pack the frame
        self.main_win.logo_label.lift()

    
        # Pack the frame
        self.frame.pack(fill=tkinter.BOTH, expand=True, anchor='n', padx=0, pady=0)

        self.main_win.root.mainloop()
