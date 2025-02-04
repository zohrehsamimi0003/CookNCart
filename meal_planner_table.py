import tkinter as tk
import database
import random_recipe
from PIL import Image, ImageTk

class Table(tk.Frame):

    def __init__(self, session, parent, rows=7, columns=4, is_new_meal_plan = False):
        self.session = session
        self.breafast_recipes =[]
        self.lunch_recipes = []
        self.dinner_recipes = []
        self.is_new_meal_plan = is_new_meal_plan

        # Check whether to use meal plan from database 
        # or generate a new temporary meal plan
        self.set_recipe_meal_groups()
        # Create one list of recipe_ids. Used in meal_planner class.
        self.recipe_ids = self.get_recipe_ids(self.breakfast_recipes, self.lunch_recipes, self.dinner_recipes)


        tk.Frame.__init__(self, parent)        

        # Column headings
        headings = ["", "Breakfast", "Lunch", "Dinner"]
        for j, heading in enumerate(headings):
            label = tk.Label(self, text=heading, borderwidth=0, background= self.session.main_win.bg, relief="solid",font=("Comic Sans MS", 18))
            label.grid(row=0, column=j, sticky="nsew",ipadx=10,ipady=10)

        # Row headings and empty cells
        row_headings = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7"]
        self.cells = []
        for i, heading in enumerate(row_headings):
            row = []
            for j in range(columns):
                if j == 0:
                    label = tk.Label(self, text=heading, background= self.session.main_win.bg, borderwidth= 0, relief="solid",font=("Comic Sans MS", 18))
                elif j== 1:
                    self.recipe_id = self.breakfast_recipes[i][0]
                    details_url = self.breakfast_recipes[i][3]
                    label = tk.Button(self, text=self.breakfast_recipes[i][1], background= self.session.main_win.bg, borderwidth= 0, command=lambda url=details_url: self.recipe_btn_clicked(url), relief="solid", font=("Georgia", 12))
                elif j == 2:
                    self.recipe_id = self.lunch_recipes[i][0]
                    details_url = self.lunch_recipes[i][3]
                    label = tk.Button(self, text=self.lunch_recipes[i][1], background= self.session.main_win.bg, borderwidth= 0, command=lambda url=details_url: self.recipe_btn_clicked(url), relief="solid",font= ("Georgia",12))
                elif j == 3:
                    self.recipe_id = self.dinner_recipes[i][0]
                    details_url = self.dinner_recipes[i][3]
                    label = tk.Button(self, text=self.dinner_recipes[i][1], background= self.session.main_win.bg, borderwidth= 0, command=lambda url=details_url: self.recipe_btn_clicked(url), relief="solid",font= ("Georgia",12))
                else:
                    label = tk.Label(self, text="some recipe", relief="solid",font= ("Georgia",12))
                label.grid(row=i+1, column=j, sticky="nsew",ipadx=10,ipady=10)
                row.append(label)
            self.cells.append(row)

        # Configure row and column weights to make the grid resizable
        for i in range(rows + 1):
            self.grid_rowconfigure(i, weight=1)
        for j in range(columns):
            self.grid_columnconfigure(j, weight=1)

    def set_recipe_meal_groups(self):
        '''Get the recipes to display.'''

        # If user has no meal plan saved in database or clicked on a new plan
        if len(self.session.user.meal_plan.breakfast_recipes) == 0 or self.is_new_meal_plan == True:
            print(self.session.user.diet_type)
            self.breakfast_recipes = self.session.my_db.get_random_recipes("Breakfast", self.session.user.diet_type, 7)
            self.lunch_recipes = self.session.my_db.get_random_recipes("Lunch", self.session.user.diet_type, 7)
            self.dinner_recipes = self.session.my_db.get_random_recipes("Dinner", self.session.user.diet_type, 7)

        # If user has a meal plan saved in database
        elif self.is_new_meal_plan == False or len(self.session.user.meal_plan.breakfast_recipes) != 0:
            self.breakfast_recipes = self.session.user.meal_plan.breakfast_recipes
            self.lunch_recipes = self.session.user.meal_plan.lunch_recipes
            self.dinner_recipes = self.session.user.meal_plan.dinner_recipes
            
    def get_recipe_ids(self, breakfast_list, lunch_list, dinner_list):
        '''Get first element from several lists of tuples.'''
        first_elements = [t[0] for sublist in [breakfast_list, lunch_list, dinner_list] for t in sublist]
        return first_elements
        
    def recipe_btn_clicked(self, recipe_details_url):
        '''Open recipe detail image as pop up screen.'''
        recipe_window = tk.Toplevel(self.session.main_win.root)
        recipe_window.title("Recipe Image")
        image = Image.open(recipe_details_url)
        photo = ImageTk.PhotoImage(image)

        # Display the image in a label
        label = tk.Label(recipe_window, image=photo)
        # This line keeps a reference to the image, preventing it from being garbage collected
        label.image = photo
        label.pack()
        recipe_window.mainloop()        


