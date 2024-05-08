import tkinter
from PIL import Image, ImageTk

class MainWindow:
    """Creates the main window for all screens that appear throughout the application"""

    def __init__(self, root):
        # root = tkinter.Tk()
        self.root = root
        root.title("CookNCart")
        root.geometry('1000x1000')
        root.configure(bg='#F9EBEA')

        # Create the primary frame with the same background color
        self.frame1 = tkinter.Frame(self.root, width=50, height=50, bg='#F9EBEA')
        self.frame1.pack(anchor='nw')

        # Load and resize the logo image
        self.logo = Image.open("C:\\Kritianstad university\\Agile Development method\\New folder\\Zohreh\\logo.png")  # Update to your logo file path
        self.logo = ImageTk.PhotoImage(self.logo.resize((300, 100)))

        # Create the button with a matching background color and slight border
        self.button = tkinter.Button(self.frame1, image=self.logo, width=300, height=100, bg='#F9EBEA', borderwidth=1, relief=tkinter.FLAT)
        self.button.grid(row=0, column=0, padx=40, pady=10)

        # Ensure the reference to the image is maintained to prevent garbage collection
        self.button.image = self.logo


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MainWindow(root)
    root.mainloop()
