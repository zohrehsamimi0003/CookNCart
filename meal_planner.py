import tkinter
from tkinter import messagebox
import main_window
from meal_planner_table import Table

root = tkinter.Tk()
Back_ground = main_window.MainWindow(root)

frame = tkinter.Frame(root,bg='#F9EBEA')

def log_off():
    pass
def profile():
    pass
def send():
    pass


CookNCart = tkinter.Button(
    frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25) ,borderwidth=1,relief='solid')
Log_off = tkinter.Button( frame, text="Log_off",bg='#F5B7B1', font=("Georgia", 11), command=log_off)
Profile = tkinter.Button( frame, text="Profile",bg='#F5B7B1', font=("Georgia", 11), command=profile)
Send=tkinter.Button(frame, text="Send",bg='#F5B7B1', font=("Georgia", 11), command=send)
table = Table(frame)

CookNCart.grid(row=0, column=0, columnspan=3, sticky="nw",padx=20, pady=20) 
Log_off.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
Profile.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))
Send.grid(row=8, column=2, padx=20, pady=(10,5), sticky="se")  # Place the button in the bottom-right corner

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.pack(fill=tkinter.BOTH, expand=True)


# Use grid() for the table widget
table.grid(row=1, column=0, columnspan=3, padx=10, pady=10)


root.mainloop()