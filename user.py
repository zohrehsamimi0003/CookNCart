import main_window

"""User class to save the user details retrieved from database based on user input."""
class User:
    """Initialize the user class."""
    def __init__(self, user_attributes):        
        self.name = user_attributes[0]
        self.email_id = user_attributes[1]
        self.password = user_attributes[2]
        self.diet_type = user_attributes[3]
    
    def update_user_data(self, new_name, new_password, new_diet_type):
        """Updates the user information if user want to update."""
        self.name = new_name
        self.password = new_password
        self.diet_type = new_diet_type
        
