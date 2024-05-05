
import tkinter
import user
import database
import meal_planner

class WelcomeScreen:
    my_db = database.Database()
    
    def __init__(self,main_win):
        self.main_win = main_win
        self.create_widgets()


    def create_widgets(self):
        self.frame = tkinter.Frame(self.main_win.root, width=1000, height=1000,bg='#F9EBEA')
        CookNCart = tkinter.Button(
            self.frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25))
        Meal_planner_label = tkinter.Button(
            self.frame, text="Meal Planner", bg='#D2B4DE', font=("Georgia", 12))#, command=Meal_planner)
        Search_recipe_label = tkinter.Button(
            self.frame, text="Search Recipe", bg='#D2B4DE', font=("Georgia", 12))#, command=Search_recipe)
        Timed_recipe_label = tkinter.Button(
            self.frame, text="Timed Recipe", bg='#D2B4DE', font=("Georgia", 12))#, command=Timed_recipe)
        log_off_button = tkinter.Button(
            self.frame, text="Log Off", bg='#F5B7B1', font=("Georgia", 11), command=self.log_off)
        profile_button = tkinter.Button(
            self.frame, text="Profile", bg='#F5B7B1', font=("Georgia", 11))#, command=Profile)

        CookNCart.grid(row=0, column=2, columnspan=3, sticky="ne", padx=20, pady=20)
        Meal_planner_label.grid(row=1, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        Search_recipe_label.grid(row=2, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        Timed_recipe_label.grid(row=3, column=0, columnspan=3, pady=20, ipadx=50, ipady=20)
        log_off_button.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
        profile_button.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True, side='top')
        
    def log_off(self):
        """Exits the application if user opt to log off."""
        self.main_win.destroy()


    def Meal_planner():
        
       pass
    # def profile_button_clicked(self):
    #     """Functionality for log in button"""
    #     naem = user.User
    #     mail = self.email_entry.get()
    #     pwd = self.password_entry.get()
    #     user1 = self.my_db.login_validation(mail, pwd)
    #     return user1
    
   

    def handle_login(self, user1_tuple):
        """Handles the login success. Creat user object"""
        if user1_tuple is None:
            tkinter.messagebox.showerror("Error", "Invalid email or password")
        elif user1_tuple is False:
            tkinter.messagebox.showerror("Database Connection Error.")
        else:
            tkinter.messagebox.showinfo("Success", "Login successful!")
            user_details = user.User(user1_tuple) 

    
    def clear_widgets(self):
        """Clear widgets from main window and switch screen."""
        for widget in self.frame.winfo_children():
            widget.destroy()
        
    def switch_meal_planner_screen(self):
        meal_planner.MealPlanner(self.main_win)
  
        
    # def S
    # earch_recipe():
    #     pass

    # def Timed_recipe():
    #     pass

    # def log_off():
    #     pass

    # def Profile():
    #     pass

