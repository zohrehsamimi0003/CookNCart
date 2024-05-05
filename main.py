import tkinter
import start_app
import main_window

def main():
    """Starts the application."""    
    root = tkinter.Tk()
    cnc_win = main_window.MainWindow(root)
    
    start_app.StartApp(cnc_win)  
    root.mainloop()

if __name__ == "__main__":
    main()
