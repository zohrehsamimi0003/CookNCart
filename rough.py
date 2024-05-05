import cook_module
import user
u = ['2', 'max', '30', 'sfdfsd', 'erer']

us = user.User(u)
print (us.name)
us.name ='Ram'
print(us.name)

cook_module.cook_n_cart_clicked(us)





# import tkinter as tk
# import mysql.connector
# from tkinter import messagebox

# class Database:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host="localhost",
#             user="username",
#             password="password",
#             database="your_database"
#         )
#         self.cursor = self.conn.cursor()

#     def login_user(self, email, password):
#         query = "SELECT * FROM users WHERE email = %s AND password = %s"
#         self.cursor.execute(query, (email, password))
#         user_data = self.cursor.fetchone()
#         if user_data:
#             user = User(*user_data[1:])
#             return user
#         else:
#             return None

#     def create_user(self, name, email, password, meal_type):
#         query = "INSERT INTO users (name, email, password, meal_type) VALUES (%s, %s, %s, %s)"
#         self.cursor.execute(query, (name, email, password, meal_type))
#         self.conn.commit()
#         return self.cursor.rowcount

#     def log_off_user(self):
#         self.conn.close()

# class User:
#     def __init__(self, name, email, meal_type):
#         self.name = name
#         self.email = email
#         self.meal_type = meal_type

# class LoginScreen:
#     def __init__(self, root, db):
#         self.root = root
#         self.db = db
#         self.email_var = tk.StringVar()
#         self.password_var = tk.StringVar()

#         self.email_label = tk.Label(root, text="Email:")
#         self.email_entry = tk.Entry(root, textvariable=self.email_var)
#         self.password_label = tk.Label(root, text="Password:")
#         self.password_entry = tk.Entry(root, textvariable=self.password_var, show="*")
#         self.login_button = tk.Button(root, text="Login", command=self.login)

#         self.email_label.pack()
#         self.email_entry.pack()
#         self.password_label.pack()
#         self.password_entry.pack()
#         self.login_button.pack()

#     def login(self):
#         email = self.email_var.get()
#         password = self.password_var.get()
#         user = self.db.login_user(email, password)
#         if user:
#             messagebox.showinfo("Success", f"Login successful! Welcome, {user.name}!")
#             self.root.destroy()
#             MainApplication(user)
#         else:
#             messagebox.showerror("Error", "Invalid email or password.")

# class CreateAccountScreen:
#     def __init__(self, root, db):
#         self.root = root
#         self.db = db
#         self.name_var = tk.StringVar()
#         self.email_var = tk.StringVar()
#         self.password_var = tk.StringVar()
#         self.meal_type_var = tk.StringVar()

#         self.name_label = tk.Label(root, text="Name:")
#         self.name_entry = tk.Entry(root, textvariable=self.name_var)
#         self.email_label = tk.Label(root, text="Email:")
#         self.email_entry = tk.Entry(root, textvariable=self.email_var)
#         self.password_label = tk.Label(root, text="Password:")
#         self.password_entry = tk.Entry(root, textvariable=self.password_var, show="*")
#         self.meal_type_label = tk.Label(root, text="Meal Type:")
#         self.meal_type_entry = tk.Entry(root, textvariable=self.meal_type_var)
#         self.create_button = tk.Button(root, text="Create Account", command=self.create_account)

#         self.name_label.pack()
#         self.name_entry.pack()
#         self.email_label.pack()
#         self.email_entry.pack()
#         self.password_label.pack()
#         self.password_entry.pack()
#         self.meal_type_label.pack()
#         self.meal_type_entry.pack()
#         self.create_button.pack()

#     def create_account(self):
#         name = self.name_var.get()
#         email = self.email_var.get()
#         password = self.password_var.get()
#         meal_type = self.meal_type_var.get()
#         rowcount = self.db.create_user(name, email, password, meal_type)
#         if rowcount:
#             messagebox.showinfo("Success", "Account created successfully!")
#             self.root.destroy()
#             MainApplication(User(name, email, meal_type))
#         else:
#             messagebox.showerror("Error", "Failed to create account.")

# class MainApplication:
#     def __init__(self, user):
#         self.user = user
#         # Here you can use self.user to access user data
#         print(f"Welcome, {self.user.name}! Your email is: {self.user.email}")

# if __name__ == "__main__":
#     db = Database()
#     root = tk.Tk()
#     LoginScreen(root, db)
#     root.mainloop()



# # import tkinter

# # class MainWindow:
# #     """Creates the main window for all screens that appear throughout the application"""
# #     def __init__(self, root):
# #         self.root = root
# #         root.title("CookNCart")
# #         root.geometry('1000x1000')
# #         root.configure(bg='#F9EBEA')

# # class WidgetCreator:
# #     """Creates widgets on the main window"""
# #     def __init__(self, main_window):
# #         self.main_window = main_window
# #         self.frame1 = None
# #         self.frame2 = None

# #     def create_widgets(self):
# #         # Create frames
# #         self.frame1 = tkinter.Frame(self.main_window.root, width=500, height=500, bg='#F9EBEA')
# #         self.frame1.pack(side='top')
# #         self.frame2 = tkinter.Frame(self.main_window.root, width=500, height=500, bg='#F9EBEA')
# #         self.frame2.pack(side='top')

# #         # Create widgets
# #         label = tkinter.Label(self.frame1, text="Hello, World!")
# #         button = tkinter.Button(self.frame2, text="Click Me", command=self.clear_and_add_widgets)

# #         # Place widgets on frames
# #         label.pack(pady=20)
# #         button.pack(pady=20)

# #     def clear_and_add_widgets(self):
# #         # Clear widgets from main window
# #         for widget in self.frame1.winfo_children():
# #             widget.destroy()
# #         for widget in self.frame2.winfo_children():
# #             widget.destroy()

# #         # Create additional widgets using AdditionalWidgetCreator
# #         additional_widget_creator = AdditionalWidgetCreator(self.main_window)
# #         # additional_widget_creator.create_additional_widgets()

# # class AdditionalWidgetCreator:
# #     """Creates additional widgets on the main window"""
# #     def __init__(self, main_window):
# #         self.main_window = main_window
# #         self.create_additional_widgets()
# #     def create_additional_widgets(self):
# #         # Create more widgets
# #         entry = tkinter.Entry(self.main_window.root)
# #         entry.pack(pady=20)

# # def main():
# #     root = tkinter.Tk()
# #     main_window = MainWindow(root)
    
# #     # Create widgets using WidgetCreator
# #     widget_creator = WidgetCreator(main_window)
# #     widget_creator.create_widgets()
    
# #     root.mainloop()

# # if __name__ == "__main__":
# #     main()




