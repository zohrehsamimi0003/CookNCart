import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="zaskia",
            password="testpw",
            database="cookncart"
        )
        
    def login_validation(self, email, password):
        try:
            my_cursor = self.db.cursor()
            query = "SELECT * FROM users WHERE Email = %s AND UserPassword = %s"
            my_cursor.execute(query, (email, password))
            user = my_cursor.fetchone()
            return user  # Returns the user object if found, otherwise None
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False  # Return False only if there's an error
        
    def insert_user(self, user): #pass a user object here ()
        pass

    def delete_user(self, email):
        pass

    def update_user(self, user): #pass user object
        pass



    #based on time of day
    def get_random_recipe(self, meal_time): 
        #implement a function in your code that decides if 
        #its time for a random lunch/breankfast/dinner recipe
        #pass strings lunch or dinner or breakfast (see main.py on my branch for logic i tested with)

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
        
    

