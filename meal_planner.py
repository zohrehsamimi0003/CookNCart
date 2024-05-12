import tkinter
from tkinter import messagebox
import main_window
from meal_planner_table import Table
import helpers
import welcome_screen
import display_profile
class MealPlanner:
    
    def __init__(self, session):
        self.session = session
        self.create_widgets()

    def create_widgets(self):
        self.frame = tkinter.Frame(self.session.main_win.root, bg='#F9EBEA')

        CookNCart = tkinter.Button(
            self.frame, text="CookNCart", command= self.new_meal_planner_btn_clicked, bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid')
        Log_off = tkinter.Button( self.frame, text="Log_off",bg='#F5B7B1', font=("Georgia", 11), command = self.log_off_btn_clicked)
        Profile = tkinter.Button( self.frame, text="Profile",bg='#F5B7B1', font=("Georgia", 11), command= self.profile_btn_clicked)
        Send=tkinter.Button(self.frame, text="Send",bg='#F5B7B1', font=("Georgia", 11), command=self.send_btn_clicked)
        self.table = Table( self.session, self.frame, is_new_meal_plan=False)

        CookNCart.grid(row=0, column=0, columnspan=3, sticky="nw",padx=20, pady=20) 
        Log_off.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
        Profile.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))
        Send.grid(row=8, column=2, padx=20, pady=(10,5), sticky="se")  # Place the button in the bottom-right corner

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True)


        # Use grid() for the table widget
        self.table.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def profile_btn_clicked(self):
        '''Go to profile page.'''
        helpers.profile_btn_screen_change(self.frame, self.session)

    def log_off_btn_clicked(self):
        '''Log off acount and go to login page.'''
        helpers.log_off_btn_screen_change(self.frame, self.session)
    
    def send_btn_clicked(self): 
        '''Save displayed meal plan to database. Create shopping list'''
        self.save_meal_plan()
        # Create one list of ingredients for the combined recipes
        recipe_ingredients = []
        for recipe_id in self.table.recipe_ids:
            recipe_ingredients += self.session.my_db.get_recipe_ingredients(recipe_id)
        # Creates the list that must be saved to the text file
        shopping_list = helpers.create_shop_list(recipe_ingredients)
        # Writes the text file
        helpers.create_shop_list_file(shopping_list, 'shopping_list.txt')

    def save_meal_plan(self):
        '''Save the displayed meal plan.'''

        # Saves to the session object
        self.session.user.meal_plan.breakfast_recipes = self.table.breakfast_recipes
        self.session.user.meal_plan.lunch_recipes = self.table.lunch_recipes
        self.session.user.meal_plan.dinner_recipes = self.table.dinner_recipes

        # Saves to the database
        self.session.my_db.insert_meal_plan(self.session.user.user_id, self.table.recipe_ids)
    
    def back_button_clicked(self):
        '''Go to welcome page.'''
        helpers.back_to_welcome_screen(self.frame, self.session)

    def new_meal_planner_btn_clicked(self):
        '''Create a new table with new recipes.'''
        self.table.destroy()
        self.table = Table(self.session, self.frame, is_new_meal_plan = True)   
        self.table.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

