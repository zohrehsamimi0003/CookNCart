import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="zaskia",
            password="publicpw",
            database="cookncart")
    
    def login_validation(self, username, password):
        pass

    def create_user(self, username, password, email, diet_type):
        pass

    def forgot_password(self, email):
        pass

    