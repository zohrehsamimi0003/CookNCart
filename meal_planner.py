import tkinter
from tkinter import messagebox
import main_window
from meal_planner_table import Table
import helpers
import welcome_screen
import display_profile
class MealPlanner:
    
    def __init__(self, session):
        self.session = session
        self.main_win = session.main_win
        self.my_db = session.my_db
        self.create_widgets()


    def create_widgets(self):
        frame = tkinter.Frame(self.main_win.root, bg='#F9EBEA')



        CookNCart = tkinter.Button(
            frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid')
        Log_off = tkinter.Button( frame, text="Log_off",bg='#F5B7B1', font=("Georgia", 11), command = self.log_off_btn_clicked)
        Profile = tkinter.Button( frame, text="Profile",bg='#F5B7B1', font=("Georgia", 11), command= self.profile_btn_clicked)
        Send=tkinter.Button(frame, text="Send",bg='#F5B7B1', font=("Georgia", 11), command=self.send)
        table = Table( self.session, frame)

        CookNCart.grid(row=0, column=0, columnspan=3, sticky="nw",padx=20, pady=20) 
        Log_off.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
        Profile.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))
        Send.grid(row=8, column=2, padx=20, pady=(10,5), sticky="se")  # Place the button in the bottom-right corner

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.pack(fill=tkinter.BOTH, expand=True)


        # Use grid() for the table widget
        table.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def profile_btn_clicked(self):
        helpers.profile_btn_screen_change(self.frame, self.session)

    def log_off_btn_clicked(self):
        helpers.log_off_btn_screen_change(self.frame, self.session)

    def send(self): #ZASKIA HANDLE THIS
        pass
