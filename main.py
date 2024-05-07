import tkinter
from start_app import StartApp
from main_window import MainWindow
from database import Database
from session import Session

def main():
    """Starts the application."""  
    
    my_db = Database() 
    
    root = tkinter.Tk()
    main_win = MainWindow(root)
    session = Session(main_win, my_db)
    
    StartApp(session)  
    root.mainloop()

if __name__ == "__main__":
    main()
