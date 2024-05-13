import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="zaskia",
            password="testpw",
            database="cookncart"
        )
    
    
    def login_validation(self, mail, pwd):
        '''Return user information as tuple.'''
        try:
            my_cursor = self.conn.cursor()
            query = '''SELECT UserId, UserName, UserPassword, EMail, DietType FROM users
             JOIN diet_types ON users.DietTypeId = diet_types.DietTypeId WHERE Email = %s AND UserPassword = %s'''
            my_cursor.execute(query, (mail, pwd))
            user = my_cursor.fetchone()
            return user
        except mysql.connector.Error as e:
            print(f"Database Error in login_validation: {e}")
            return False
        
        
    #CHECKS IF AN EMAIL EXISTS. RETURNS A USER IF IT EXISTS OTHERWISE NONE (TRUE OR FALSE)
    def check_if_user_exists(self, email):
        '''Check if a user exists based on unique email.'''
        try:
            my_cursor = self.conn.cursor()
            query = '''SELECT UserId, UserName, UserPassword, EMail, DietType FROM users
             JOIN diet_types ON users.DietTypeId = diet_types.DietTypeId WHERE Email = %s'''
            my_cursor.execute(query, (email,))
            user = my_cursor.fetchone()
            return user #You can do: if user: blah else: call the insert method
        except mysql.connector.Error as e:
            print(f"Database Error in check_if_user_exists: {e}")
        
    #INSERTS A USER BEING CREATED INTO THE DATABASE    
    def insert_user(self, username_entry, email_entry, password_entry, diet_type_entry): 
        '''Get DietTypeId, insert user, return user.'''
        try:
            my_cursor = self.conn.cursor()

            # Get the DietTypeId
            select_query = "SELECT DietTypeId FROM diet_types WHERE DietType = %s"
            my_cursor.execute(select_query, (diet_type_entry,))
            diet_type_result = my_cursor.fetchone()
            
            # Insert the user with the obtained DietTypeId
            insert_query = '''INSERT INTO users (UserName, UserPassword, Email, DietTypeId)
                            VALUES (%s, %s, %s, %s)'''
            parameters = (username_entry, password_entry, email_entry, diet_type_result[0])
            my_cursor.execute(insert_query, parameters)
            user_id = my_cursor.lastrowid
            # Commit to database and return user
            self.conn.commit()
            my_cursor.close()
            return user_id
        except mysql.connector.Error as e:
            print(f"Database Error in insert_user: {e}")

            
            
    def update_user(self, mail, new_name, new_password, new_diet_type):       
        '''Get DietTypeId, update all user fields except email, return rowcount.'''
        try:
            my_cursor = self.conn.cursor()

            # Get DietTypeId
            select_query = "SELECT DietTypeId FROM diet_types WHERE DietType = %s"
            my_cursor.execute(select_query, (new_diet_type,))
            diet_type_result = my_cursor.fetchone()

            query = '''UPDATE users SET Username = %s, UserPassword = %s, DietTypeId = %s WHERE Email = %s;'''
            parameters = (new_name, new_password, diet_type_result[0], mail)
            my_cursor.execute(query, parameters)

            self.conn.commit()
            rowcount = my_cursor.rowcount
            my_cursor.close()
            return rowcount
        except mysql.connector.Error as e: 
            print(f"Database Error in update_user: {e}")


    def get_random_recipes(self, meal_time, diet_type, number_of_recipes):
        '''Select 1 or more random recipes based on lunch type.'''
        parameters = [meal_time]
        query = '''SELECT RecipeId, RecipeTitle, ImageURL, DetailsURL, MealTime, diet_types.DietType, Portions FROM recipes
                INNER JOIN meal_times
                ON recipes.MealTimeId = meal_times.MealTimeId
                INNER JOIN diet_types
                ON recipes.DietType = diet_types.DietTypeId
                WHERE meal_times.MealTime = %s'''  
        
        if diet_type != "no preference":
            query += "AND diet_types.DietType = %s"
            parameters.append(diet_type)
        
        query += '''ORDER BY RAND()
                 LIMIT %s;'''
        parameters.append(number_of_recipes)
        
        try:
            my_cursor = self.conn.cursor()         
            
            my_cursor.execute(query, parameters)
            random_recipe = my_cursor.fetchall()
            return random_recipe 
        except mysql.connector.Error as e:
            print(f"Database Error in get_random_recipes: {e}")
            return False
        

    def get_random_recipe(self, diet_type):
        ''' Select a random recipe.'''
        parameter = []
        query = '''SELECT RecipeId, RecipeTitle, ImageURL, DetailsURL, diet_types.DietType FROM recipes '''
        if diet_type != "no preference":            
            query += ''' INNER JOIN diet_types
            ON recipes.DietType = diet_types.DietTypeId 
            WHERE diet_types.DietType = %s '''
            parameter.append(diet_type)
        query += ''' ORDER BY RAND()
                    LIMIT 1;'''       
        try:
            my_cursor = self.conn.cursor()           
            my_cursor.execute(query, parameter)
            random_recipe = my_cursor.fetchall() #might change this if I have time, should be fetchone()
            return random_recipe 
        except mysql.connector.Error as e:
            print(f"Database Error in get_random_recipe: {e}")
            return False
        
    def get_diet_types(self):
        '''Return a list available diet types.'''
        try:
            my_cursor = self.conn.cursor()
            query = '''SELECT DietType FROM diet_types;'''  
            my_cursor.execute(query)
            return my_cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Database Error in get_diet_types: {e}")
            return False


    def get_recipe_ingredients(self, recipe_id):
        '''Return the list of ingredients for a specific recipe.'''
        try:
            my_cursor = self.conn.cursor()
            query = '''SELECT Ingredient, Quantity, Unit  FROM recipe_ingredients 
                    JOIN ingredients ON recipe_ingredients.IngredientId = ingredients.IngredientId
                    WHERE RecipeId = %s '''
            my_cursor.execute(query, (recipe_id,))
            ingredients = my_cursor.fetchall()
            return ingredients
        except mysql.connector.Error as e:
            print(f"Database Error in get_recipe_ingredients: {e}")
            return False      
          
    def get_recipe_details_url(self, recipe_id):
        '''Return the recipe details url of a specific recipe.'''
        try:
            my_cursor = self.conn.cursor()
            query = '''SELECT DetailsURL FROM recipes WHERE RecipeId = %s '''            
            
            my_cursor.execute(query, (recipe_id,))
            recipe_details_url = my_cursor.fetchall()
            return recipe_details_url 
        except mysql.connector.Error as e:
            print(f"Database Error in get_recipe_details_url: {e}")
            return False

    
    def insert_meal_plan(self, user_id, recipe_ids): 
        '''Insert user's new meal plan and its recipes into database.'''
        try:
            my_cursor = self.conn.cursor()
            
            # Create a meal plan for the user
            insert_query = '''INSERT INTO user_meal_plans (UserId, DateCreated) VALUES(%s , NOW());'''
            my_cursor.execute(insert_query, (user_id,))
            self.conn.commit()
            
            # Get the id of the newly created meal plan
            select_query = "SELECT LAST_INSERT_ID();"
            my_cursor.execute(select_query)
            meal_plan_id = my_cursor.fetchone()[0]

            # Insert each meal plan's recipes
            for recipe_id in recipe_ids:
                select_query="INSERT INTO meal_plan_recipes (MealPlanID, RecipeId) VALUES(%s, %s)"
                my_cursor.execute(select_query, (meal_plan_id, recipe_id))
                self.conn.commit()

            my_cursor.close()
        except mysql.connector.Error as e:
            print(f"Database Error in insert_meal_plan: {e}")

    

    def get_meal_plan_id(self, user_id):
        '''Get the last inserted meal plan.'''
        try:
            my_cursor = self.conn.cursor()
            query = '''SELECT MealPlanId FROM user_meal_plans 
            WHERE UserId = %s ORDER BY DateCreated DESC
            LIMIT 1;'''
            my_cursor.execute(query, (user_id,))
            meal_plan_id = my_cursor.fetchone()
            return meal_plan_id 
        except mysql.connector.Error as e:
            print(f"Database Error in get_meal_plan_id: {e}")
            return False
        
    def get_meal_plan_recipe_ids(self, meal_plan_id, meal_time):
        '''Get a list of all the recipes belonging to a meal plan.'''
        try:
            my_cursor = self.conn.cursor()
            query = '''SELECT meal_plan_recipes.RecipeId,  RecipeTitle, ImageURL, DetailsURL FROM meal_plan_recipes
                    JOIN recipes ON  meal_plan_recipes.RecipeId = recipes.RecipeId
                    JOIN meal_times ON meal_times.MealTimeId = recipes.MealTimeId 
                    WHERE MealTime = %s AND MealPlanId = %s
                    ORDER BY meal_plan_recipes.insertion_timestamp;'''           
            
            my_cursor.execute(query, (meal_time, meal_plan_id))
            random_recipe = my_cursor.fetchall()
            return random_recipe 
        except mysql.connector.Error as e:
            print(f"Database Error in get_meal_plan_recipe_ids: {e}")
            return False

            
    
    