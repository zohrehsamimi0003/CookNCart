import tkinter
# import database
import account_creation
import start_app
import main_window
# import screen_manager

def main():
    
    root = tkinter.Tk()
    cnc_win = main_window.MainWindow(root)
    
    start  = start_app.StartApp(cnc_win)
    
    
    
    
    root.mainloop()

    # # g = mygui.MyGUI(root)
    # g.frame1_button()
    
if __name__ == "__main__":
    main()
