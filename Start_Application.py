import tkinter
import mysql.connector
from tkinter import messagebox
from Main_window import Main_window

root = tkinter.Tk()
Back_ground = Main_window(root)

frame = tkinter.Frame(root,bg='#F9EBEA')

def login():
    
    try:
        
        db = mysql.connector.connect(
            host="localhost",
            user="Anitta",
            password="Anitta#110405",
            database="cookncart"
        )
        my_cursor = db.cursor()
        email_id = email_entry.get()
        password = password_entry.get()
        query = "SELECT * FROM users WHERE Email = %s AND UserPassword = %s"
        my_cursor.execute(query, (email_id, password))
        user = my_cursor.fetchone()

        if user:
            messagebox.showinfo(title="Successfully logged in", message="You are logged in!")
        else:
            messagebox.showinfo(title="Login Error", message="Invalid email or password!")

    except mysql.connector.Error as e:
        messagebox.showerror(title="Database Error", message=f"Error: {e}")
def create_account():
    pass
    

# Create widgets
login_label = tkinter.Label(
    frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25),borderwidth=1,relief='solid' )
email_label = tkinter.Label(
    frame, text="E-Mail ID", bg='#AED6F1', font=("Georgia", 12))
email_entry = tkinter.Entry(
    frame,bg='#D2B4DE' ,font=("Georgia", 12))
password_entry = tkinter.Entry(
    frame, show="*",bg='#D2B4DE' , font=("Georgia", 12))
password_label = tkinter.Label(
    frame, text="Password", bg='#AED6F1', font=("Georgia", 12))
login_button = tkinter.Button(
    frame, text="Login", bg='#F5B7B1', font=("Georgia", 12), command=login)
forgot_pw_button = tkinter.Button(
    frame, text="Forgot Password", bg='#F5B7B1', font=("Georgia", 12))
create_account_button = tkinter.Button(
    frame, text="Create Account",bg='#F5B7B1', font=("Georgia", 11), command = create_account)


# Place widgets on screen
login_label.grid(row=0, column=0, columnspan=3, pady=50,ipadx=100,ipady=50) 
email_label.grid(row=1, column=0 ,ipadx=10,ipady=10,sticky="e")
email_entry.grid(row=1, column=1,ipadx=100,ipady=10, pady=20,sticky="e")
password_label.grid(row=2, column=0,ipadx=10,ipady=10,sticky="e")  
password_entry.grid(row=2, column=1,pady=20,ipadx=100,ipady=10,sticky="e")  
login_button.grid(row=4,column=0 ,columnspan=2, padx=10,pady=30,ipadx=10,ipady=10)
forgot_pw_button.grid(row=4,column=1, columnspan=2, pady=30,ipadx=10,ipady=10)
create_account_button.grid(row=0,column=2, sticky="ne",padx=10,pady=10,ipadx=10,ipady=10)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.pack(fill=tkinter.BOTH, expand=True)

frame.pack()


root.mainloop()
