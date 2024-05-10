import tkinter as tk
import database
import timed_recipe

class Table(tk.Frame):

    
    def __init__(self, session, parent, rows=7, columns=4):
        self.my_db = session.my_db
        self.session = session
        tk.Frame.__init__(self, parent)
        
        breakfast_recipes = self.my_db.get_random_recipes("Breakfast", 7)
        lunch_recipes = self.my_db.get_random_recipes("Lunch", 7)
        dinner_recipes = self.my_db.get_random_recipes("Dinner", 7)

        recipe_ids = self.get_recipe_ids(breakfast_recipes, lunch_recipes, dinner_recipes)

        # Column headings
        headings = ["", "Breakfast", "Lunch", "Dinner"]
        for j, heading in enumerate(headings):
            label = tk.Label(self, text=heading, borderwidth=1, relief="solid",font=("Comic Sans MS", 18))
            label.grid(row=0, column=j, sticky="nsew",ipadx=10,ipady=10)

        # Row headings and empty cells
        row_headings = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7"]
        self.cells = []
        for i, heading in enumerate(row_headings):
            row = []
            for j in range(columns):
                if j == 0:
                    label = tk.Label(self, text=heading, relief="solid",font=("Comic Sans MS", 18))
                elif j== 1:
                    self.recipe_id = breakfast_recipes[i][0]
                    label = tk.Button(self, text=breakfast_recipes[i][1], command=self.recipe_btn_clicked, relief="solid", font=("Georgia", 12))
                elif j == 2:
                    self.recipe_id = breakfast_recipes[i][0]
                    label = tk.Button(self, text=lunch_recipes[i][1], command=self.recipe_btn_clicked, relief="solid",font= ("Georgia",12))
                elif j == 3:
                    self.recipe_id = breakfast_recipes[i][0]
                    label = tk.Button(self, text=dinner_recipes[i][1], command=self.recipe_btn_clicked, relief="solid",font= ("Georgia",12))
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
            
        self.update_table()
        
    def update_table(self):
        pass
        '''# Fetch data from the database
        #data = self.my_db.meal_planner_recipes()
         # Implemented this method in Zaskia Database class

        # Update table cells with fetched data
        for i, row_data in enumerate(data):
            for j, cell_data in enumerate(row_data):
                self.cells[i][j].configure(text=cell_data)    '''    
        
    def recipe_btn_clicked(self):
        recipe_window = tk.Toplevel(self.session.main_win.root)
        timed_recipe.TimedRecipe(self.session, recipe_window, self.recipe_id)


    def get_recipe_ids(self, breakfast_list, lunch_list, dinner_list):
        first_elements = [t[0] for sublist in [breakfast_list, lunch_list, dinner_list] for t in sublist]
        print(first_elements)        


    def add_or_update_recipe(self, recipe_ids):
        for recipe_id in recipe_ids:
            recipe_ingredients = self.my_db.get_recipe_ingredients(recipe_id)
            shop_ingredients = [{}] #I need this to be empty and populated in the conditional below.
            #
        if recipe_ingredients[0] in shop_ingredients:
            '''# If the ingredient already exists for this recipe, update quantity if unit matches
            if recipe_ingredients[2] == unit:
                recipe_data[key]["Quantity"] += quantity
            else:
                print(f"Warning: Unit mismatch for ingredient '{ingredient}' in Recipe_id {recipe_id}.")
        else:
            # If the ingredient does not exist for this recipe, add it
            recipe_data[key] = {"Quantity": quantity, "Unit": unit}'''