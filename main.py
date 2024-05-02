import tkinter
import account_creation
import start_app
import main_window
import screen_manager

def main():
    # s = tkinter.Tk()
    root = tkinter.Tk()
    m = main_window.MainWindow(root)
    
    s = start_app.StartApp(root)
    s.create_widgets()
    a = account_creation.AccountCreation(root)
    # my_screen_manager = screen_manager.ScreenManager()
    
    
    
    root.mainloop()

    # g = mygui.MyGUI(root)
    # g.frame1_button()
    
if __name__ == "__main__":
    main()
