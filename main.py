from GUI import GUI
from Database import Database

def main():
    db = Database()  # Create an instance of the database
    app = GUI(login_handler=db.login_handler)  # Pass the login handler from the database instance
    app.mainloop()

if __name__ == "__main__":
    main()

#boo