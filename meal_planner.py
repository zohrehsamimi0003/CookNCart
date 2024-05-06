import tkinter
from tkinter import messagebox
import main_window
from meal_planner_table import Table
import helpers
import welcome_screen
import display_profile
class MealPlanner:
    
    def __init__(self, main_win,my_db):
        self.main_win = main_win
        #self.created_user_obj = created_user_obj
        self.my_db = my_db
        self.create_widgets()


    def create_widgets(self):
        frame = tkinter.Frame(self.main_win.root, bg='#F9EBEA')



        CookNCart = tkinter.Button(
            frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid', command = self.cook_n_cart_btn_clicked)
        Log_off = tkinter.Button( frame, text="Log_off",bg='#F5B7B1', font=("Georgia", 11), command = self.log_off_btn_clicked)
        Profile = tkinter.Button( frame, text="Profile",bg='#F5B7B1', font=("Georgia", 11), command= self.profile_btn_clicked)
        Send=tkinter.Button(frame, text="Send",bg='#F5B7B1', font=("Georgia", 11), command=self.send)
        table = Table(frame)

        CookNCart.grid(row=0, column=0, columnspan=3, sticky="nw",padx=20, pady=20) 
        Log_off.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
        Profile.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))
        Send.grid(row=8, column=2, padx=20, pady=(10,5), sticky="se")  # Place the button in the bottom-right corner

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.pack(fill=tkinter.BOTH, expand=True)


        # Use grid() for the table widget
        table.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    
    def cook_n_cart_btn_clicked(self):
         welcome_screen.WelcomeScreen(self.main_win, self.created_user_obj)

    def log_off_btn_clicked(self):
         """Exits the application if user opt to log off."""
         self.main_win.destroy()

    def profile_btn_clicked(self):
         """Display the saved user profile."""
         self.clear_widgets()
         display_profile.DisplayProfile(self.main_win, self.created_user_obj)

    def send(self): #ZASKIA HANDLE THIS
        pass
