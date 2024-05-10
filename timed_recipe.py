import tkinter as tkinter
import main_window
import helpers
import database
import start_app
from PIL import Image, ImageTk


class TimedRecipe:
    
    def __init__(self, session, recipe_id):        
        self.session = session
        self.main_win = session.main_win
        self.my_db = session.my_db
        self.recipe_id = recipe_id
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










    '''def create_widgets(self):
        self.frame = tk.Frame(self.main_win.root, bg='#F9EBEA')

        cook_n_cart = tk.Button(self.frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25), borderwidth=1, relief='solid')
        log_off_button = tk.Button(self.frame, text="Log_off", bg='#F5B7B1', font=("Georgia", 11), command=self.log_off_button_clicked)
        profile_button = tk.Button(self.frame, text="Profile", bg='#F5B7B1', font=("Georgia", 11), command=self.profile_button_clicked)

        canvas = tk.Canvas(self.frame, bg="white", bd=2, relief="solid")


        # ChatGPT
        image = Image.open("Images/SampleImage.jpg")
        tk_image = ImageTk.PhotoImage(image)
        #image = image.resize((200, 200), Image.ANTIALIAS)
        image_widget = canvas.create_image(0, 0, anchor="nw", image=tk_image)

        canvas.image = tk_image
        #label_window = canvas.create_window(50, 50, anchor="nw", window=label)
        #ChatGPT

        recipe_label = tk.Label(canvas, text=f"Recipe ID: {self.recipe_id}", bg='#F5B7B1', font=("Georgia", 12), padx=20, pady=20)
        recipe_label_window = canvas.create_window(50, 50, anchor="nw", window=recipe_label)

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

        # Add entry to canvas
        entry = tk.Entry(canvas, width=50,bg='#D2B4DE')  # Adjust width to add padding
        entry_window = canvas.create_window(200, 50, anchor="nw", window=entry)
        canvas.itemconfig(entry_window, width=250, height=60)
        canvas.bind('<Button-1>', lambda event: canvas.coords(entry_window, event.x, event.y))
            
    def profile_button_clicked(self):
        helpers.profile_btn_screen_change(self.frame, self.session)

    def log_off_button_clicked(self):
        helpers.log_off_btn_screen_change(self.frame, self.session)

    def send_button_clicked(self):
        pass'''
