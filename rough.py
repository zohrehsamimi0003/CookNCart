import tkinter

class MainWindow:
    """Creates the main window for all screens that appear throughout the application"""
    def __init__(self, root):
        self.root = root
        root.title("CookNCart")
        root.geometry('1000x1000')
        root.configure(bg='#F9EBEA')

class WidgetCreator:
    """Creates widgets on the main window"""
    def __init__(self, main_window):
        self.main_window = main_window
        self.frame1 = None
        self.frame2 = None

    def create_widgets(self):
        # Create frames
        self.frame1 = tkinter.Frame(self.main_window.root, width=500, height=500, bg='#F9EBEA')
        self.frame1.pack(side='top')
        self.frame2 = tkinter.Frame(self.main_window.root, width=500, height=500, bg='#F9EBEA')
        self.frame2.pack(side='top')

        # Create widgets
        label = tkinter.Label(self.frame1, text="Hello, World!")
        button = tkinter.Button(self.frame2, text="Click Me", command=self.clear_and_add_widgets)

        # Place widgets on frames
        label.pack(pady=20)
        button.pack(pady=20)

    def clear_and_add_widgets(self):
        # Clear widgets from main window
        for widget in self.frame1.winfo_children():
            widget.destroy()
        for widget in self.frame2.winfo_children():
            widget.destroy()

        # Create additional widgets using AdditionalWidgetCreator
        additional_widget_creator = AdditionalWidgetCreator(self.main_window)
        # additional_widget_creator.create_additional_widgets()

class AdditionalWidgetCreator:
    """Creates additional widgets on the main window"""
    def __init__(self, main_window):
        self.main_window = main_window
        self.create_additional_widgets()
    def create_additional_widgets(self):
        # Create more widgets
        entry = tkinter.Entry(self.main_window.root)
        entry.pack(pady=20)

def main():
    root = tkinter.Tk()
    main_window = MainWindow(root)
    
    # Create widgets using WidgetCreator
    widget_creator = WidgetCreator(main_window)
    widget_creator.create_widgets()
    
    root.mainloop()

if __name__ == "__main__":
    main()
