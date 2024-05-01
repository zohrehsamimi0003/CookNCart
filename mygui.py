import callbackhandler
import tkinter as tk

class MyGUI:
    def __init__(self, root1):
        self.root = root1
        self.frame1 = tk.Frame(root1, width=1000, height=500, bg="red")
        self.frame1.pack(side='right')
        # self.frame1.grid(row=100, column=500, padx=5, pady=5)
        self.callback_handler = callbackhandler.CallbackHandler(root1)

    def frame1_button(self):        
        self.button = tk.Button(self.frame1, text="Shopping List",
                                command=self.callback_handler.callback_method)
        self.button1 = tk.Button(self.frame1, text="Log Off",
                                command=self.callback_handler.callback_method)
        self.button.pack(side = 'left')
        self.button1.pack()

