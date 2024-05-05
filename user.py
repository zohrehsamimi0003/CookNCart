import main_window

"""User class to save the user details retrieved from database based on user input."""
class User:
    """Initialize the user class."""
    def __init__(self, user1_tuple):        
        self.name = user1_tuple[1]
        self.email_id = user1_tuple[2]
        self.password = user1_tuple[3]
        self.diet_type =user1_tuple[4]
    
    def update_user_data(self, new_name, new_password, new_diet_type):
        """Updates the user information if user want to update."""
        self.name = new_name
        self.password = new_password
        self.diet_type = new_diet_type
        
