import tkinter
import start_app
import main_window
import database

def main():
    """Starts the application."""    
    my_db = database.Database()
    root = tkinter.Tk()
    cnc_win = main_window.MainWindow(root)
    
    start_app.StartApp(cnc_win, my_db)  
    root.mainloop()

if __name__ == "__main__":
    main()
