import tkinter
from user import User
from database import Database
import welcome_screen
import start_app
import helpers
from main_window import MainWindow
from session import Session


class SearchRecipe:

    def __init__(self, session):
        self.session = session
        self.create_widgets()
    
    def profile_button_clicked(self):
        '''Go to profile page.'''
        helpers.profile_btn_screen_change(self.frame, self.session)

    def log_off_button_clicked(self):
        '''Log off acount and go to login page.'''
        helpers.log_off_btn_screen_change(self.frame, self.session)

    def back_button_clicked(self):
        '''Go to welcome page'''
        helpers.back_to_welcome_screen(self.frame, self.session)

    def search_button_clicked(self):
        pass

    def create_widgets(self):    

        self.frame = tkinter.Frame(self.session.main_win.root,bg='#F9EBEA', width=500,height=500)
        ingredients = tkinter.Label(
            self.frame, text="  Ingredients :", bg='#AED6F1', font=("Georgia", 12), anchor="w")
        ingredients_entry= tkinter.Entry(
            self.frame,bg='#AED6F1', font=("Georgia", 12))
        results = tkinter.Label(
            self.frame, text="Results found :" , bg='#F9EBEA', font=("Georgia", 12), anchor="w")
        Log_off_button = tkinter.Button(
            self.frame, text="Log_off",bg='#8b5a2b', font=("Georgia", 12), command=self.log_off_button_clicked)
        Profile_button = tkinter.Button(
            self.frame, text = "Profile",bg='#8b5a2b', font=("Georgia", 12), command=self.profile_button_clicked)
        back_button = tkinter.Button(self.frame, text="Back", bg='#8b5a2b',font=("Georgia", 12), command=self.back_button_clicked,  borderwidth=1)
        search_button = tkinter.Button(self.frame, text="Search", bg='#8b5a2b',font=("Georgia", 12), command=self.search_button_clicked)

        canvas =tkinter.Canvas(
            self.frame,width=500, height=350, bg="white"
        )

        # Place widgets on screen
        ingredients.grid(row=1,column=0,padx=(50,0),pady=(150,30),ipadx=10,ipady=13,sticky="w")
        ingredients_entry.grid(row=1, column=0,padx=(10,20),pady=(150,30),ipadx=50,ipady=13)
        search_button.grid(row=1,column=0, pady=(150,30),padx= (400,20) ,ipadx=20, ipady=8)

        Log_off_button.grid(row=1,column=1, sticky="ne",padx=(10,50), pady=(10,5), ipadx=20, ipady=10)
        Profile_button.grid(row=1,column=1, sticky="ne",padx=(0,175), pady=(10,5), ipadx=20, ipady=10)
        back_button.grid(row=3, column=1, sticky="se", padx=(10,50),pady=(0,150), ipadx=20, ipady=10)
        canvas.grid(row=3,column=0,padx=(150,0),pady=(0,150))
        results.grid(row=2,column=0,padx=(50,100),sticky="w")


        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        
        
        # Pack the frame
        self.session.main_win.logo_label.lift()

    
        # Pack the frame
        self.frame.pack(fill=tkinter.BOTH, expand=True, anchor='n', padx=0, pady=0)

        self.session.main_win.root.mainloop()