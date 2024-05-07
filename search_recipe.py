import tkinter
import start_app

class SearchRecipe:
    def __init__(self, session):
        self.session = session
        self.main_win = session.main_win
        self.my_db = session.my_db    
        self.create_widgets()

    def create_widgets(self):
        self.frame = tkinter.Frame(self.main_win.root, bg='#F9EBEA')

        cookNcart = tkinter.Button(
            self.frame, text="CookNCart", bg='#F5B7B1', font=("Comic Sans MS", 25), borderwidth=1, relief='solid')
        No_of_people = tkinter.Label(
            self.frame, text="No.of People             ", bg='#F5B7B1', font=("Georgia", 12))
        self.No_of_people_entry = tkinter.Entry(
            self.frame, bg='#D2B4DE', font=("Georgia", 12))
        Recipe_name = tkinter.Label(
            self.frame, text="Recipe Name            ", bg='#F5B7B1', font=("Georgia", 12))
        self.Recipe_name_entry = tkinter.Entry(
            self.frame, bg='#D2B4DE', font=("Georgia", 12))
        List_of_ingredients = tkinter.Label(
            self.frame, text=" List_of_ingredients", bg='#F5B7B1', font=("Georgia", 12))
        self.List_of_ingredients_entry = tkinter.Entry(
            self.frame, bg='#D2B4DE', font=("Georgia", 12))
        log_off = tkinter.Button(self.frame, text="Log_off", bg='#F5B7B1',
                                font=("Georgia", 11), command=self.log_off_button_clicked)
        Profile = tkinter.Button(self.frame, text="Profile", bg='#F5B7B1',
                                font=("Georgia", 11), command=self.profile)

        cookNcart.grid(row=0, column=0, sticky="nw")
        No_of_people.grid(row=1, column=0, sticky="e",
                        ipadx=10, ipady=10, padx=10, pady=10)
        self.No_of_people_entry.grid(
            row=1, column=1, pady=20, ipadx=100, ipady=10)
        Recipe_name.grid(row=2, column=0, sticky="e",
                        ipadx=10, ipady=10, padx=10, pady=10)
        self.Recipe_name_entry.grid(
            row=2, column=1, pady=20, ipadx=100, ipady=10)
        List_of_ingredients.grid(row=3, column=0, sticky="e",
                                ipadx=10, ipady=10, padx=10, pady=10)
        self.List_of_ingredients_entry.grid(
            row=3, column=1, pady=20, ipadx=100, ipady=10)
        log_off.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
        Profile.grid(row=0, column=2, sticky="ne", padx=10, pady=(20, 10))

        self.frame.pack(fill=tkinter.BOTH, expand=True)

    def profile():
        pass
    def log_off_button_clicked(self):  
        self.frame.destroy()
        start_app.StartApp(self.session)