# import database
# import start_app
# import tkinter as tk
import main_window

class User:
    def __init__(self, user1_tuple):        
        self.name = user1_tuple[1]
        self.email_id = user1_tuple[2]
        self.password = user1_tuple[3]
        self.diet_type =user1_tuple[4]
    
    

    #when user clicked create_account then a_c_screen will appear)    
    # def create_account(self, account_creation_screen):
    #     return account_creation_screen
        
        # self.name = name_entry.get()
        # self.email_id = email_entry.get()
        # self.password = password_entry.get()
        # self.diet_type = 
        
    # def log_in(self, mail, pwd): #--------- this metd should return the entry.get email id & password
    #     """Call the login_screen method to get email and password from the user"""
    #     """Validate login credentials"""
    #     # print("before db query")
    #     # print ("name" + self.name)
    #     # user = self.my_db.login_validation(mail, pwd)
    #     # print(" after running db query in user class")
    #     # print (user)
        
    #     if user is None:  # Use boolean value False instead of string 'False'
    #         return False
    #         # tk.messagebox.showinfo("Error", "Incorrect credentials") 
    #     else:
    #     # Unpack user tuple into individual variables
    #         user = self.name, self.email_id, self.password, self.diet_type
    #         print("when user found")
    #         print("what is name " + self.name)
    #         print (user) # tk.messagebox.showinfo(title="Successfully logged in", message="You are logged in!")
    #         return user
        
       
    # def log_off(self):
    #     ls.LoginScreen() #------------start application screen will appear
        
    # def display_profile(self):
    #     #dps........ child screen should appear
    #     acs.entry_name = tk.Entry(textvariable=self.name)  
    #     acs.email_id = tk.Entry(textvariable=self.email_id, state='readonly')
    #     acs.password = tk.Entry(textvariable="*") 
    #     acs.diet_type = tk.Entry(textvariable=self.diet_type) 
    #     pass # display screen display profile with E-mail entry box as frozen
    
    # def update_profile(self):
    #     #  runs database query basedon e-mail id and update all other information.   
    #     pass
    # def forgot_pwd(self): #VERSION" 2.0
    #     pass
                    
            
    # def create_user (name, email, pwd, diet_type):
    #     email_id = email_entry.get()
    #     password = password_entry.get()
    #     try:
    #         my_cursor = self.db.cursor()
    #         query = "SELECT * FROM users WHERE Email = %s AND UserPassword = %s"
    #         my_cursor.execute(query, (email, password))
    #         user = my_cursor.fetchone()
    #         return user is not None
    #     except mysql.connector.Error as e:
    #         print(f"Database Error: {e}")
    #         return False    
        

