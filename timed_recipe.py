import tkinter as tk
import main_window
import cook_module
import database


class TimedRecipe:
    my_db = database.Database()
    
    def __init__(self, main_win, my_db, created_user_obj):
        self.main_win = main_win
        self.created_user_obj = created_user_obj
        self.my_db = my_db
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.main_win.root, bg='#F9EBEA')

        cook_n_cart = tk.Button(
            frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25), borderwidth=1, relief='solid', command=cook_module.cook_n_cart_clicked(self.created_user_obj))
        log_off_button = tk.Button(frame, text="Log_off", bg='#F5B7B1', font=("Georgia", 11), command=cook_module.log_off_button_clicked)
        profile_button = tk.Button(frame, text="Profile", bg='#F5B7B1', font=("Georgia", 11), command=cook_module.profile_button_clicked(self.created_user_obj))

        canvas = tk.Canvas(frame, bg="white", bd=2, relief="solid")

        send_button = tk.Button(frame, text="Send", bg='#F5B7B1', font=("Georgia", 11), command=send_button)

        cook_n_cart.grid(row=0, column=0, sticky="nw") 
        profile_button.grid(row=0, column=4, sticky="ne",padx=(0,50),pady=10,ipadx=5,ipady=5)
        log_off_button.grid(row=0, column=4, sticky="ne",padx=(0,150),pady=10,ipadx=5,ipady=5)

        canvas.grid(row=1, column=0, columnspan=4, padx=10, pady=10,ipady=(90), sticky="nsew")

        send_button.grid(row=2, column=4, sticky="se", padx=(0,50), pady=(20, 10),ipadx=5,ipady=5)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)

        frame.pack(fill=tk.BOTH, expand=True)

        # Add label to canvas
        label = tk.Label(canvas, text="No.Of people", bg='#F5B7B1', font=("Georgia", 12),padx=20,pady=20)
        label_window = canvas.create_window(50, 50, anchor="nw", window=label)

        # Add entry to canvas
        entry = tk.Entry(canvas, width=50,bg='#D2B4DE')  # Adjust width to add padding
        entry_window = canvas.create_window(200, 50, anchor="nw", window=entry)
        canvas.itemconfig(entry_window, width=250, height=60)
        canvas.bind('b1', lambda event: canvas.coords(entry_window, event.x, event.y))

