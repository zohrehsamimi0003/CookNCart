import display_profile
import welcome_screen
import start_app
import random_recipe

"""Helper functions."""
    
def clear_widgets(frame):
    """Clear widgets from main window and switch screen."""
    frame.destroy()


def log_off_btn_screen_change(frame, session):
    """Log user out of application and returns to log in page (start_app)"""
    clear_widgets(frame)
    session.user = None
    start_app.StartApp(session)
        
        
def profile_btn_screen_change(frame, session):
    """Display the saved user profile."""
    clear_widgets(frame)
    display_profile.DisplayProfile(session)
              
'''def cook_n_cart_clicked(self, created_user_obj):
    """Clear widgets and take user to welcome screen."""
    self.clear.widgets()
    welcome_screen.WelcomeScreen(self.main_win, created_user_obj)'''

def back_to_welcome_screen(frame, session):
    '''Change screen to welcome screen.'''
    clear_widgets(frame)
    welcome_screen.WelcomeScreen(session)

def create_shop_list(recipe_ingredients):
    '''Add ingredients to create a list with unique ingredient, quantity.'''
    shopping_list = {} 
    # Pair Ingredient, Unit to add the same type of ingredient to each other
    for Ingredient, Quantity, Unit in recipe_ingredients:
        key = (Ingredient, Unit)
        if key in shopping_list:
            shopping_list[key] += Quantity
        else:
            shopping_list[key] = Quantity

    return shopping_list

def create_shop_list_file(shopping_list, file_name): 
    '''Generate a text file and display shopping list.'''
    with open(file_name, 'w') as file:
        file.write("Shopping List\n\n")
        file.write("Quantity".ljust(10) + "Ingredient\n\n")
        
        # Write each quantity, unit and ingredient on a new line
        for (ingredient, unit), quantity in shopping_list.items():
            amount = f"{quantity}{unit}"
            if unit is None:
                unit = ""
                file.write(f"{quantity:<10}{ingredient}\n")
            else:
                file.write(f"{amount:<10}{ingredient}\n")
