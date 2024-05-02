
class ScreenManager:
    
    def __init__(self, main_win):
        self.main_win = main_win
        
    def clear_widgets(self):
            # Destroy or remove all widgets of the current screen
            for widget in self.main_win.winfo_children():
                widget.destroy()
                
    def switch_to_new_screen(self, screen_obj):
        self.clear_widgets()
        # new_screen.create_widgets()