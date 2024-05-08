import main_window

"""User class to save the user details retrieved from database based on user input."""
class User:
    """Initialize the user class."""
    def __init__(self, name, password,  email, diet_type = None):        
        self.name = name
        self.email = email
        self.password = password
        self.diet_type = diet_type
    
    def update_user_data(self, new_name, new_password, new_diet_type):
        """Updates the user information if user want to update."""
        self.name = new_name
        self.password = new_password
        self.diet_type = new_diet_type
        
