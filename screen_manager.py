
class ScreenManager:
    
    def __init__(self, root):
        self.root = root
        
    def clear_widgets(self):
            # Destroy or remove all widgets of the current screen
            for widget in self.root.winfo_children():
                widget.destroy()
                
    def switch_to_new_screen(self):
        self.clear_widgets()
        # new_screen.create_widgets()