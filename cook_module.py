import display_profile
import welcome_screen



def clear_widgets(self):
    """Clear widgets from main window and switch screen."""
    for widget in self.frame.winfo_children():
        widget.destroy()

def log_off_button_clicked(self, main_win):
    """Exits the application if user opt to log off."""
    main_win.destroy()
        
        
def profile_button_clicked(self, created_user_obj):
    """Display the saved user profile."""
    self.clear_widgets()
    display_profile.DisplayProfile(self.main_win, created_user_obj)
              
def cook_n_cart_clicked(self, created_user_obj):
    welcome_screen.WelcomeScreen(self.main_win, created_user_obj)
    print(created_user_obj.name)
                