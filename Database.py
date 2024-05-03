import mysql.connector
from tkinter import messagebox
from datetime import datetime, time

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="zaskia",
            password="testpw",
            database="cookncart"
        )
    
    
    def login_validation(self, mail, pwd):
        try:
            my_cursor = self.conn.cursor()
            query = "SELECT * FROM users WHERE Email = %s AND UserPassword = %s"
            my_cursor.execute(query, (mail, pwd))
            user = my_cursor.fetchone()
            return user
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False
        
        
    #CHECKS IF AN EMAIL EXISTS. RETURNS A USER IF IT EXISTS OTHERWISE NONE (TRUE OR FALSE)
    def check_if_user_exists(self, email):
        try:
            my_cursor = self.conn.cursor()
            query = "SELECT * FROM users WHERE Email = %s"
            my_cursor.execute(query, (email,))
            user = my_cursor.fetchone()
            return user #You can do: if user: blah else: call the insert method
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        
    #INSERTS A USER BEING CREATED INTO THE DATABASE    
    def insert_user(self, username_entry, email_entry, password_entry, diet_type_entry): 
        try:
            my_cursor = self.conn.cursor()

            # First, execute the SELECT statement
            select_query = "SELECT DietTypeId FROM diet_types WHERE DietType = %s"
            my_cursor.execute(select_query, (diet_type_entry,))
            diet_type_result = my_cursor.fetchone()
            
            # Then, insert the user with the obtained DietTypeId
            insert_query = '''INSERT INTO users (UserName, UserPassword, Email, DietTypeId)
                            VALUES (%s, %s, %s, %s)'''
            parameters = (username_entry, password_entry, email_entry, diet_type_result[0])
            my_cursor.execute(insert_query, parameters)

            # Finally, commit the transaction
            self.conn.commit()
            rowcount = my_cursor.rowcount

            my_cursor.close()

            return rowcount #you get 1 if it inserted it successfully 
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return 0
            

        
    #DELETES AN EXISTING USER
    def delete_user(self, user):
        try:
            my_cursor = self.conn.cursor()
            query = '''DELETE FROM users WHERE Email = %s;'''
            my_cursor.execute(query, (user.email,))
            # Finally, commit the transaction
            self.conn.commit()
            rowcount = my_cursor.rowcount

            my_cursor.close()
            return rowcount
        except mysql.connector.Error as e: 
            print(f"Database Error: {e}")
            return 0

    #UPDATES THE PASSWORD OF AN EXISTING USER
    def update_password(self, user, new_password): #pass user object here and the new password from the entry box
        try:
            my_cursor = self.conn.cursor()
            query = '''UPDATE users SET UserPassword = %s WHERE Email = %s;'''
            parameters = (new_password, user.email)
            my_cursor.execute(query, parameters)
            self.conn.commit()
            rowcount = my_cursor.rowcount

            my_cursor.close()
            return rowcount
        except mysql.connector.Error as e: 
            print(f"Database Error: {e}")
            return 0

    #UPDATES THE DIET TYPE OF AN EXISTING USER
    def update_diet_type(self, user, new_diet_type): #pass user object here and the new password from the entry box
        try:
            my_cursor = self.conn.cursor()
            select_query = "SELECT DietTypeId FROM diet_types WHERE DietType = %s"
            my_cursor.execute(select_query, (new_diet_type,))
            diet_type_result = my_cursor.fetchone()
            query = '''SELECT DietTypeId INTO @DietTypeId FROM diet_types WHERE DietType = %s;
            UPDATE users SET DietTypeId = @DietTypeId WHERE Email = %s;'''
            parameters = (diet_type_result, user.email)
            my_cursor.execute(query, parameters)
            # Finally, commit the transaction
            self.conn.commit()
            rowcount = my_cursor.rowcount

            my_cursor.close()
            return rowcount
        except mysql.connector.Error as e: 
            print(f"Database Error: {e}")
            return 0



    #SELECTS 1 OR MORE RANDOM RECIPE BASED ON LUNCH TYPE (USED FOR TIME OF DAY RECIPE)
    def get_random_recipes(self, meal_time, number_of_recipes): 
        #implement a function in your code that decides if 
        #its time for a random lunch/breankfast/dinner recipe
        #pass strings lunch or dinner or breakfast (see main.py on my branch for logic i tested with)

        try:
            my_cursor = self.conn.cursor()
            query = '''SELECT RecipeTitle, Instructions, CookTime, ImageURL, MealTime, diet_types.DietType, Portions FROM recipes
                    INNER JOIN meal_times
                    ON recipes.MealTimeId = meal_times.MealTimeId
                    INNER JOIN diet_types
                    ON recipes.DietType = diet_types.DietTypeId
                    WHERE meal_times.MealTime = %s
                    ORDER BY RAND()
                    LIMIT %;'''            
            
            my_cursor.execute(query, (meal_time, number_of_recipes))
            random_recipe = my_cursor.fetchone()
            return random_recipe 
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False


    
    
