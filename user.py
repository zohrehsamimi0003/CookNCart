import account_creation_screen


class User:
    def __init__(self):
        self.name = account_creation_screen.name_entry()
        self.email_id
        self.password
        self.diet_type
        
    #when user clicked create_account then a_c_screen will appear)    
    def create_account(self, account_creation_screen):
        return account_creation_screen
    
        # self.name = name_entry.get()
        # self.email_id = email_entry.get()
        # self.password = password_entry.get()
        # self.diet_type = 
   def log_in(self, self.email_id, self.password):
        
            
    def create_user (name, email, pwd, diet_type):
        email_id = email_entry.get()
        password = password_entry.get()
        try:
            my_cursor = self.db.cursor()
            query = "SELECT * FROM users WHERE Email = %s AND UserPassword = %s"
            my_cursor.execute(query, (email, password))
            user = my_cursor.fetchone()
            return user is not None
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False    
        

