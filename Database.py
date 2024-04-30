import mysql.connector
from tkinter import messagebox

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="zaskia",
            password="publicpw",
            database="cookncart"
        )
    
    def login_validation(self, email, password):
        try:
            my_cursor = self.db.cursor()
            query = "SELECT * FROM users WHERE Email = %s AND UserPassword = %s"
            my_cursor.execute(query, (email, password))
            user = my_cursor.fetchone()
            return user is not None
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False

    def login_handler(self, email, password):
        if self.login_validation(email, password):
            messagebox.showinfo(title="Successfully logged in", message="You are logged in!")
        else:
            messagebox.showinfo(title="Login Error", message="Invalid email or password!")
