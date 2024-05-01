from tkinter import *


class Screens:
    def __init__(self):
        frame = Frame()
        frame.pack()
        
        self.printbutton = Button(frame, text="Click here", command = self.printmessage)
        self.printbutton.pack()
        
        
    def printmessage(self):
        print("B-C")   

    
    
r = Tk()
a=Screens(r)
r.mainloop()        
        
         
