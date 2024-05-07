import display_profile
import welcome_screen
import start_app
import timed_recipe

"""This module deals with clear widget, exit the application 
    & switches the screen."""
    
def clear_widgets(frame):
    """Clear widgets from main window and switch screen."""
    frame.destroy()


def log_off_btn_screen_change(frame, session):
    """Logs user out of application and returns to log in page (start_app)"""
    clear_widgets(frame)
    session.user = None
    start_app.StartApp(session)
        
        
def profile_btn_screen_change(frame, session):
    """Display the saved user profile."""
    clear_widgets(frame)
    display_profile.DisplayProfile(session)
              
def cook_n_cart_clicked(self, created_user_obj):
    """Clear widgets and take user to welcome screen."""
    self.clear.widgets()
    welcome_screen.WelcomeScreen(self.main_win, created_user_obj)
