
import tkinter
import meal_planner
import timed_recipe
import search_recipe
import helpers
import start_app
from datetime import datetime
import session

class WelcomeScreen:
    def __init__(self, session):
        self.session = session
        self.main_win = session.main_win
        self.my_db = session.my_db
        self.create_widgets()

    def create_widgets(self):
        self.frame = tkinter.Frame(self.main_win.root, width=1000, height=1000, bg='#F9EBEA')

        CookNCart = tkinter.Button(
            self.frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25))
        Meal_planner_label = tkinter.Button(
            self.frame, text="Meal Planner", bg='#D2B4DE', font=("Georgia", 12), command=self.meal_planner_button_clicked)
        Search_recipe_label = tkinter.Button(
            self.frame, text="Search Recipe", bg='#D2B4DE', font=("Georgia", 12), command=self.search_recipe_button_clicked)
        Timed_recipe_label = tkinter.Button(
            self.frame, text="Timed Recipe", bg='#D2B4DE', font=("Georgia", 12), command=self.timed_recipe_button_clicked)
        log_off_button = tkinter.Button(
            self.frame, text="Log Off", bg='#F5B7B1', font=("Georgia", 11), command=self.log_off_button_clicked)
        profile_button = tkinter.Button(
            self.frame, text="Profile", bg='#F5B7B1', font=("Georgia", 11), command=helpers.profile_button_clicked)

        CookNCart.grid(row=0, column=2, columnspan=3, sticky="ne", padx=20, pady=20)
        Meal_planner_label.grid(row=1, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        Search_recipe_label.grid(row=2, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        Timed_recipe_label.grid(row=3, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        log_off_button.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
        profile_button.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True, side='top')

    def meal_planner_button_clicked(self):
       self.frame.destroy()
       meal_planner.MealPlanner(self.session)

    def log_off_button_clicked(self):
        self.clear_widgets()
        start_app.StartApp(self.session)

    def timed_recipe_button_clicked(self):
        now = datetime.now()
        current_time = now.time()   
        if current_time <= datetime.strptime('10:30', '%H:%M').time():
            time_of_day = "breakfast"
            timed_recipe.TimedRecipe(self.session)
        elif current_time <= datetime.strptime('14:30', '%H:%M').time():
            time_of_day = "Lunch"
            timed_recipe.TimedRecipe(self.session)
        else:
            time_of_day = "Dinner"            
            timed_recipe.TimedRecipe(self.session)                  
        self.frame.destroy()

    def search_recipe_button_clicked(self):    
        self.frame.destroy()
        search_recipe.SearchRecipe(self.session)
    
    def back_btn_clicked(self):
        self.frame.destroy()
        start_app.StartApp(self.session)

    # def profile_button_clicked(self):
    #     """Display the saved user profile."""
    #     cook_module.clear_widgets()
    #     display_profile.DisplayProfile(self.main_win, self.created_user_obj)
        
