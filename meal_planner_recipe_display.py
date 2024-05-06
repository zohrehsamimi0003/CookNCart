import tkinter as tk
import main_window
import helpers

def log_off():
    pass

def profile():
    pass

def shopping_list():
    pass

def back():
    pass

def checkout():
    pass

root = tk.Tk()
Back_ground = main_window.MainWindow(root)

frame = tk.Frame(root, bg='#F9EBEA')

cook_n_cart = tk.Button(
    frame, text="CookNCart", bg='#D2B4DE', font=("Comic Sans MS", 25), borderwidth=1, relief='solid' )
log_off_button = tk.Button(frame, text="Log_off", bg='#F5B7B1', font=("Georgia", 11), command=helpers.log_off_button_clicked)
profile_button = tk.Button(frame, text="Profile", bg='#F5B7B1', font=("Georgia", 11), command=helpers.profile_button_clicked)
shopping_list_button = tk.Button(frame, text="Shopping List", bg='#F5B7B1', font=("Georgia", 11), command=shopping_list)

canvas = tk.Canvas(frame, bg="white", bd=2, relief="solid")

back_button = tk.Button(frame, text="Back", bg='#F5B7B1', font=("Georgia", 11), command=back)
checkout_button = tk.Button(frame, text="Checkout", bg='#F5B7B1', font=("Georgia", 11), command=checkout)

cook_n_cart.grid(row=0, column=0, sticky="nw") 
profile_button.grid(row=0, column=3, sticky="ne",padx=(0,25),pady=10,ipadx=10,ipady=5)
shopping_list_button.grid(row=0, column=4,padx=(0,150), sticky="ne",pady=10,ipadx=5,ipady=5)
log_off_button.grid(row=0, column=4, sticky="ne",padx=(0,50),pady=10,ipadx=5,ipady=5)

canvas.grid(row=1, column=0, columnspan=4, padx=10, pady=10,ipady=(90), sticky="nsew")

back_button.grid(row=2, column=4, sticky="se", padx=(0,175), pady=(20, 10),ipadx=10,ipady=5)
checkout_button.grid(row=2, column=4, sticky="se", padx=(0,50), pady=(20, 10),ipadx=5,ipady=5)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

frame.pack(fill=tk.BOTH, expand=True)




root.mainloop()