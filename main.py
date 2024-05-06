import tkinter
from start_app import StartApp
from main_window import MainWindow
from database import Database
from session import Session

def main():
    """Starts the application."""  
    my_db = Database() 
    
    root = tkinter.Tk()
    cnc_win = MainWindow(root)
    
    StartApp(cnc_win, my_db)  
    root.mainloop()

if __name__ == "__main__":
    main()
