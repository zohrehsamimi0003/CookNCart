import tkinter as tk
import database
import timed_recipe
from PIL import Image, ImageTk

class Table(tk.Frame):

    
    def __init__(self, session, parent, rows=7, columns=4):
        self.my_db = session.my_db
        self.session = session
        self.recipe_ids = []
        tk.Frame.__init__(self, parent)
        
        breakfast_recipes = self.my_db.get_random_recipes("Breakfast", 7)
        lunch_recipes = self.my_db.get_random_recipes("Lunch", 7)
        dinner_recipes = self.my_db.get_random_recipes("Dinner", 7)

        self.recipe_ids = self.get_recipe_ids(breakfast_recipes, lunch_recipes, dinner_recipes)

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
                    details_url = breakfast_recipes[i][2]
                    label = tk.Button(self, text=breakfast_recipes[i][1], command=lambda url=details_url: self.recipe_btn_clicked(url), relief="solid", font=("Georgia", 12))
                elif j == 2:
                    self.recipe_id = lunch_recipes[i][0]
                    details_url = lunch_recipes[i][2]
                    label = tk.Button(self, text=lunch_recipes[i][1], command=lambda url=details_url: self.recipe_btn_clicked(url), relief="solid",font= ("Georgia",12))
                elif j == 3:
                    self.recipe_id = dinner_recipes[i][0]
                    details_url = dinner_recipes[i][0]
                    label = tk.Button(self, text=dinner_recipes[i][1], command=lambda url=self.recipe_id: self.recipe_btn_clicked(url), relief="solid",font= ("Georgia",12))
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
        
    def recipe_btn_clicked(self, recipe_details_url):
        #recipe_window = tk.Toplevel(self.session.main_win.root)
        #timed_recipe.TimedRecipe(self.session, recipe_window, self.recipe_id)
        # Create a new Toplevel window
        print(recipe_details_url)
        recipe_window = tk.Toplevel(self.session.main_win.root)
        recipe_window.title("Recipe Image")
        # Load the image
        image = Image.open(recipe_details_url)

        # Create a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Display the image in a label
        label = tk.Label(recipe_window, image=photo)
        label.image = photo  # This line keeps a reference to the image, preventing it from being garbage collected
        label.pack()

        # Start the tkinter event loop for the new window
        recipe_window.mainloop()        


    def get_recipe_ids(self, breakfast_list, lunch_list, dinner_list):
        first_elements = [t[0] for sublist in [breakfast_list, lunch_list, dinner_list] for t in sublist]
        return first_elements
