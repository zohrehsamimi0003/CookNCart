import main_window
from meal_plan import MealPlan

"""User class to save the user details retrieved from database based on user input."""
class User:
    """Initialize the user class."""
    def __init__(self, user_id, name, password,  email, diet_type = None):        
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.diet_type = diet_type
        self.meal_plan = MealPlan()
    
    def update_user_data(self, new_name, new_password, new_diet_type):
        """Update the user information if user want to update."""
        self.name = new_name
        self.password = new_password
        self.diet_type = new_diet_type
        
