import tkinter
from PIL import Image, ImageTk

class MainWindow():
    """Creates the main window for all screens that appear throughout the application"""

    def __init__(self, root):
        self.root = root
        root.title("CookNCart")
        root.geometry('1000x1000')
        root.configure(bg='#F9EBEA')

        # Load and resize the logo image
        self.logo = Image.open("C:\Software development\Agile development\CookNCart\logo.png")  # Update to your logo file path
        self.logo = ImageTk.PhotoImage(self.logo.resize((300, 100)))

        # Create the button with a matching background color and slight border
        self.logo_label = tkinter.Label(root, image=self.logo, width=300, height=100, bg='#F9EBEA', borderwidth=1, relief=tkinter.FLAT)
        self.logo_label.place(x=0, y=0)



