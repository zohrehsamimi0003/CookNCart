
import tkinter
import meal_planner
import timed_recipe
import search_recipe
import cook_module

class WelcomeScreen:
    def __init__(self, main_win, my_db):
        self.main_win = main_win
        self.my_db = my_db
        #self.user = user
        self.create_widgets()

    def create_widgets(self):
        self.frame = tkinter.Frame(self.main_win.root, width=1000, height=1000, bg='#F9EBEA')

        CookNCart = tkinter.Button(
            self.frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25))
        Meal_planner_label = tkinter.Button(
            self.frame, text="Meal Planner", bg='#D2B4DE', font=("Georgia", 12), command=self.Meal_planner_button_clicked)
        Search_recipe_label = tkinter.Button(
            self.frame, text="Search Recipe", bg='#D2B4DE', font=("Georgia", 12), command=self.search_recipe_button_clicked)
        Timed_recipe_label = tkinter.Button(
            self.frame, text="Timed Recipe", bg='#D2B4DE', font=("Georgia", 12), command=self.timed_recipe_button_clicked)
        log_off_button = tkinter.Button(
            self.frame, text="Log Off", bg='#F5B7B1', font=("Georgia", 11), command=cook_module.log_off_button_clicked)
        profile_button = tkinter.Button(
            self.frame, text="Profile", bg='#F5B7B1', font=("Georgia", 11), command=cook_module.profile_button_clicked)

        CookNCart.grid(row=0, column=2, columnspan=3, sticky="ne", padx=20, pady=20)
        Meal_planner_label.grid(row=1, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        Search_recipe_label.grid(row=2, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        Timed_recipe_label.grid(row=3, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        log_off_button.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
        profile_button.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True, side='top')

    def Meal_planner_button_clicked(self):
       cook_module.clear_widgets()
       meal_planner.MealPlanner(self.main_win, self.user)

    def timed_recipe_button_clicked(self):
        cook_module.clear_widgets()
        # Fetch recipes from database based on time
        # timed_recipe.TimedRecipe(self.main_win, self.my_db, self.user)

    def search_recipe_button_clicked(self):    
        cook_module.clear_widgets()
        search_recipe.SearchRecipe(self.main_win)


#Used for testing . ZASKIA you can delete it.    
        
    def clear_widgets(self):
        """Clear widgets from main window and switch screen."""
        self.frame.destroy()
    
    

    # def profile_button_clicked(self):
    #     """Display the saved user profile."""
    #     cook_module.clear_widgets()
    #     display_profile.DisplayProfile(self.main_win, self.created_user_obj)
        
