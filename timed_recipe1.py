import tkinter
from user import User
from database import Database
import welcome_screen
import start_app
import helpers
from main_window import MainWindow
from session import Session


class Timed_recipe1:

    def __init__(self, session):
        my_db = Database() 
        root = tkinter.Tk()
        main_win = MainWindow(root)
        session = Session(main_win, my_db)
        self.session = session
        self.main_win = session.main_win
        self.my_db = session.my_db
        self.create_widgets()
    
    def log_off(self):
        pass
    def profile(self):
        pass


    def back_btn_clicked(self):
        helpers.clear_widgets(self.frame)
        start_app.StartApp(self.session)

    def recipe_details(self):
        pass

    def Send(self):
        pass

    def create_widgets(self):    

        self.frame = tkinter.Frame(self.main_win.root,bg='#F9EBEA', width=500,height=500)
        Recipe_title_label = tkinter.Label(
            self.frame, text="       Recipe Title", bg='#AED6F1', font=("Georgia", 12), anchor="w")
        recipe_details= tkinter.Button(
            self.frame, text="Recipe Details",bg='#8b5a2b', font=("Georgia", 12), command=self.recipe_details)
        send = tkinter.Button(
            self.frame, text="send",bg='#8b5a2b', font=("Georgia", 12), command=self.Send)
        canvas =tkinter.Canvas(
            self.frame,width=500, height=400, bg="white"
        )

        Log_off_button = tkinter.Button(
            self.frame, text="Log_off",bg='#8b5a2b', font=("Georgia", 12), command=self.log_off)
        Profile_button = tkinter.Button(
            self.frame, text = "Profile",bg='#8b5a2b', font=("Georgia", 12), command=self.profile)
        back_button = tkinter.Button(self.frame, text="Back", bg='#8b5a2b',font=("Georgia", 12), command=self.back_btn_clicked,  borderwidth=1)
        

        # Place widgets on screen
        Recipe_title_label.grid(row=1,column=0,padx=(50,350),pady=(150,30),ipadx=10,ipady=10)
        recipe_details.grid(row=2,column=2,pady=(0,150),ipadx=10,ipady=12)
        send.grid(row=2,column=2,padx=20,ipadx=42,ipady=10)
        canvas.grid(row=2,column=0,padx=(50,100),pady=(0,100))

        Log_off_button.grid(row=1,column=3, sticky="ne",padx=(10,50), pady=(10,5), ipadx=20, ipady=10)
        Profile_button.grid(row=1,column=3, sticky="ne",padx=(0,175), pady=(10,5), ipadx=20, ipady=10)
        back_button.grid(row=2, column=3, sticky="se", padx=(10,50),pady=(0,100),  ipadx=20, ipady=10)
        


        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        
        
        # Pack the frame
        self.main_win.logo_label.lift()

    
        # Pack the frame
        self.frame.pack(fill=tkinter.BOTH, expand=True, anchor='n', padx=0, pady=0)

        self.main_win.root.mainloop()
    

# Create an instance of Timed_recipe1 and let its __init__ method create widgets
timed_recipe_instance = Timed_recipe1(Session)
