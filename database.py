import mysql.connector
from tkinter import messagebox
from datetime import datetime, time

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="meenu",
            password="1234",
            database="cookncart"
        )
    
    
    def login_validation(self, mail, pwd):
        try:
            my_cursor = self.db.cursor()
            query = "SELECT * FROM users WHERE Email = %s AND UserPassword = %s"
            my_cursor.execute(query, (mail, pwd))
            user = my_cursor.fetchone()
            print(user) #checking
            return user
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False

    def random_recipe(self): #This should return a tuple or something like it
        current_time = datetime.now().time()
        breakfast_end = time(10,30)
        lunch_end = time(14,30)

        if current_time < breakfast_end:
            meal_time = "Breakfast"
        elif current_time > breakfast_end and current_time < lunch_end:
            meal_time = "Lunch"
        else:
            meal_time = "Dinner"

        try:
            my_cursor = self.db.cursor()
            query = '''SELECT RecipeTitle, Instructions, CookTime, ImageURL, MealTime, diet_types.DietType, Portions FROM recipes
                    INNER JOIN meal_times
                    ON recipes.MealTimeId = meal_times.MealTimeId
                    INNER JOIN diet_types
                    ON recipes.DietType = diet_types.DietTypeId
                    WHERE meal_times.MealTime = %s
                    ORDER BY RAND()
                    LIMIT 1;'''
            
            
            my_cursor.execute(query, (meal_time,))
            random_recipe = my_cursor.fetchone()
            return random_recipe 
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False