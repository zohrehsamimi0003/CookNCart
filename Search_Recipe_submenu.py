import tkinter
import mysql.connector
from tkinter import messagebox
from Main_window import Main_window

root = tkinter.Tk()
Back_ground = Main_window(root)

frame = tkinter.Frame(root,bg='#F9EBEA')

def Log_off():
    pass
def profile():
    pass

cookNcart = tkinter.Button(
    frame, text="CookNCart",bg='#D2B4DE', font=("Comic Sans MS", 25),borderwidth=1,relief='solid' )
No_of_people =  tkinter.Label(
    frame,text="No.of People             ",bg='#D2B4DE',font= ("Georgia",12))
No_of_people_entry= tkinter.Entry(
    frame,bg='#D2B4DE' ,font=("Georgia", 12))
Recipe_name =  tkinter.Label(
    frame,text="Recipe Name            ",bg='#D2B4DE',font= ("Georgia",12))
Recipe_name_entry= tkinter.Entry(
    frame,bg='#D2B4DE' ,font=("Georgia", 12))
List_of_ingredients=  tkinter.Label(
    frame,text=" List_of_ingredients",bg='#D2B4DE',font= ("Georgia",12))
List_of_ingredients_entry=tkinter.Entry(
    frame,bg='#D2B4DE' ,font=("Georgia", 12))
log_off = tkinter.Button( frame, text="Log_off",bg='#F5B7B1', font=("Georgia", 11), command=Log_off)
Profile = tkinter.Button( frame, text="Profile",bg='#F5B7B1', font=("Georgia", 11), command=profile)


cookNcart.grid(row=0, column=0, sticky="nw") 
No_of_people.grid(row=1, column=0, sticky="e", ipadx=10, ipady=10,padx=10,pady=10)
No_of_people_entry.grid(row=1,column=1,pady=20,ipadx=100,ipady=10)
Recipe_name.grid(row=2, column=0, sticky="e",ipadx=10, ipady=10,padx=10,pady=10)
Recipe_name_entry.grid(row=2,column=1,pady=20,ipadx=100,ipady=10)
List_of_ingredients.grid(row=3, column=0,sticky="e", ipadx=10, ipady=10,padx=10,pady=10)
List_of_ingredients_entry.grid(row=3,column=1,pady=20,ipadx=100,ipady=10)
log_off.grid(row=0, column=1, sticky="ne", padx=10, pady=20)
Profile.grid(row=0, column=2, sticky="ne", padx=10, pady=(20,10))

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.pack(fill=tkinter.BOTH, expand=True)

frame.pack()

root.mainloop()