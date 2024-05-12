import tkinter as tkinter
import main_window
import helpers
import database
import start_app
from PIL import Image, ImageTk
from recipe import Recipe
import welcome_screen


class TimedRecipe:
    
    def __init__(self, session):        
        self.session = session
        self.main_win = session.main_win
        self.my_db = session.my_db
        self.recipe = None
        self.get_recipe()
        self.shopping_list = {}
        self.create_widgets()

    def profile_button_clicked(self):
        helpers.profile_btn_screen_change(self.frame, self.session)

    def log_off_button_clicked(self):
        helpers.log_off_btn_screen_change(self.frame, self.session)

    def back_btn_clicked(self):
        helpers.back_to_welcome_screen(self.frame, self.session)

    def get_recipe(self):
        random_recipe = self.session.my_db.get_random_recipe()[0]
        self.recipe = Recipe(random_recipe[0], random_recipe[1], random_recipe[2], random_recipe[3])

    def recipe_details(self):
        #recipe_window = tk.Toplevel(self.session.main_win.root)
        #timed_recipe.TimedRecipe(self.session, recipe_window, self.recipe_id)
        # Create a new Toplevel window
        recipe_window = tkinter.Toplevel(self.session.main_win.root)
        recipe_window.title("Recipe Image")

        # Load the image
        #image = Image.open(self.recipe.recipe_details_path)
        image = Image.open(self.recipe.recipe_details_path)

        # Create a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Display the image in a label
        label = tkinter.Label(recipe_window, image=photo)
        label.image = photo  # This line keeps a reference to the image, preventing it from being garbage collected
        label.pack()

        # Start the tkinter event loop for the new window
        recipe_window.mainloop()      

    def send_button_clicked(self):
        recipe_ingredients = self.session.my_db.get_recipe_ingredients(self.recipe.recipe_id)
        shopping_list = helpers.create_shop_list(recipe_ingredients)
        helpers.create_shop_list_file(shopping_list, "random_recipe_list.txt")

    


    def create_widgets(self):    

        self.frame = tkinter.Frame(self.session.main_win.root,bg='#F9EBEA', width=500,height=500)
        Recipe_title_label = tkinter.Label(
            self.frame, text=self.recipe.recipe_title, bg='#AED6F1', font=("Georgia", 12), anchor="w")
        recipe_details= tkinter.Button(
            self.frame, text="Recipe Details",bg='#8b5a2b', font=("Georgia", 12), command=self.recipe_details)
        send = tkinter.Button(
            self.frame, text="send",bg='#8b5a2b', font=("Georgia", 12), command=self.send_button_clicked)
        canvas =tkinter.Canvas(
            self.frame,width=500, height=400, bg="white"
        )

        Log_off_button = tkinter.Button(
            self.frame, text="Log_off",bg='#8b5a2b', font=("Georgia", 12), command=self.log_off_button_clicked)
        Profile_button = tkinter.Button(
            self.frame, text = "Profile",bg='#8b5a2b', font=("Georgia", 12), command=self.profile_button_clicked)
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

        #ChatGPTCODE

            # Load the image
        image = Image.open(self.recipe.recipe_img_path)  # Change path to your image file
        tk_image = ImageTk.PhotoImage(image)
        
        # Display the image on the canvas
        canvas.create_image(0, 0, anchor="nw", image=tk_image)

        # Keep a reference to the image to prevent it from being garbage collected
        canvas.image = tk_image

        #ChatGPTCODE
        
        
        # Pack the frame
        self.session.main_win.logo_label.lift()

    
        # Pack the frame
        self.frame.pack(fill=tkinter.BOTH, expand=True, anchor='n', padx=0, pady=0)

        self.session.main_win.root.mainloop()
