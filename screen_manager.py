"""Used to switch the screens during application run."""


class ScreenManager:
    
    def __init__(self, main_win):
        self.main_win = main_win
        
    def switch_screen (self, screen_obj):
        """Destroy or remove all widgets of the current screen & switch screens."""
        for widget in self.main_win.winfo_children():
            widget.destroy()
        screen_obj(self.main_win)

  