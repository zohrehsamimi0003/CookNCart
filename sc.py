import tkinter
from tkinter import *


class Screens:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('500x500')
        self.window.configure(bg='#FFFFFF')
        self.window.mainloop()

    def login_page(self):
        self.window.title("Login form")
        
a = Screens()
a.login_page()
        
        
#         frame = Frame(r1)
#         frame.pack()
        
#         self.printbutton = Button(frame, text="Click here", command = self.printmessage)
#         self.printbutton.pack()
        
        
#     def printmessage(self):
#         print("B-C")   

    
    
# r = Tk()
# a=Screens(r)
# r.mainloop()        
        
         

# window = tkinter.Tk()
# window.title("Login form")
# window.geometry('500x500')
# window.configure(bg='#FFFFFF')

# frame = tkinter.Frame(bg='#FFFFFF')

    