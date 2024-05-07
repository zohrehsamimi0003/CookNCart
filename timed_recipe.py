import tkinter as tk
import main_window
import helpers
import database
import start_app


class TimedRecipe:
    
    def __init__(self, session):        
        self.session = session
        self.main_win = session.main_win
        #self.user = user
        self.my_db = session.my_db
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.main_win.root, bg='#F9EBEA')

        cook_n_cart = tk.Button(self.frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25), borderwidth=1, relief='solid')
        log_off_button = tk.Button(self.frame, text="Log_off", bg='#F5B7B1', font=("Georgia", 11), command=self.log_off_button_clicked)
        profile_button = tk.Button(self.frame, text="Profile", bg='#F5B7B1', font=("Georgia", 11), command=self.profile_button_clicked)

        canvas = tk.Canvas(self.frame, bg="white", bd=2, relief="solid")

        send_button = tk.Button(self.frame, text="Send", bg='#F5B7B1', font=("Georgia", 11), command=self.send_button_clicked)

        cook_n_cart.grid(row=0, column=0, sticky="nw") 
        profile_button.grid(row=0, column=4, sticky="ne",padx=(0,50),pady=10,ipadx=5,ipady=5)
        log_off_button.grid(row=0, column=4, sticky="ne",padx=(0,150),pady=10,ipadx=5,ipady=5)

        canvas.grid(row=1, column=0, columnspan=4, padx=10, pady=10,ipady=(90), sticky="nsew")

        send_button.grid(row=2, column=4, sticky="se", padx=(0,50), pady=(20, 10),ipadx=5,ipady=5)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

        self.frame.pack(fill=tk.BOTH, expand=True)

        # Add label to canvas
        label = tk.Label(canvas, text="No.Of people", bg='#F5B7B1', font=("Georgia", 12),padx=20,pady=20)
        label_window = canvas.create_window(50, 50, anchor="nw", window=label)

        # Add entry to canvas
        entry = tk.Entry(canvas, width=50,bg='#D2B4DE')  # Adjust width to add padding
        entry_window = canvas.create_window(200, 50, anchor="nw", window=entry)
        canvas.itemconfig(entry_window, width=250, height=60)
        canvas.bind('<Button-1>', lambda event: canvas.coords(entry_window, event.x, event.y))
            
    def log_off_button_clicked(self):  
        self.frame.destroy()
        start_app.StartApp(self.session)

    def profile_button_clicked(self):
        self.clear_widgets()

    def send_button_clicked(self):
        pass
