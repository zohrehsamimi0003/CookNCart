import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="zaskia",
            password="testpw",
            database="cookncart"
        )

    #CHECKS IF THE LOGIN DETAILS RETURNS A USER AND SO EXISTS    
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

    #INSERTS A USER BEING CREATED INTO THE DATABASE    
    def insert_user(self, username_entry, email_entry, password_entry, diet_type): 
        mycursor = self.db.cursor()
        query = '''SELECT DietTypeId INTO @DietTypeId FROM diet_types WHERE DietType = 'Vegetarian';
                INSERT INTO users (Username, UserPassword, Email, DietType)
                VALUES (%s, %s, %s, %s)'''
        
        parameters = (username_entry, password_entry, email_entry, diet_type)
        mycursor.execute(query, parameters)

        return mycursor.rowcount #will return 1 if properly inserted, maybe use that to check and instantiate user object?

    #DELETES AN EXISTING USER
    def delete_user(self, user):
        mycursor = self.db.cursor()
        query = '''DELETE FROM users WHERE Email = %s;'''
        mycursor.execute(query, (user.email,))

    #UPDATES THE PASSWORD OF AN EXISTING USER
    def update_password(self, user, new_password): #pass user object here and the new password from the entry box
        mycursor = self.db.cursor()
        query = '''UPDATE users SET UserPassword = % WHERE Email = %;'''
        parameters = (new_password, user.email)
        mycursor.execute(query, parameters)
        mycursor.rowcount

    #UPDATES THE DIET TYPE OF AN EXISTING USER
    def update_diet_type(self, user, new_diet_type): #pass user object here and the new password from the entry box
        mycursor = self.db.cursor()
        query = '''SELECT DietTypeId INTO @DietTypeId FROM diet_types WHERE DietType = %s;
        UPDATE users SET DietTypeId = @DietTypeId WHERE Email = %s;'''
        parameters = (new_diet_type, user.email)
        mycursor.execute(query, parameters)
        mycursor.rowcount



    #SELECTS A RANDOM RECIPE BASED ON LUNCH TYPE (USED FOR TIME OF DAY RECIPE)
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
        
    

