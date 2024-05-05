import tkinter as tk
import database

class Table(tk.Frame):
    my_db = database.Database()
    self.Breakfast = Breakfast
    def __init__(self, parent, rows=7, columns=4):
        tk.Frame.__init__(self, parent)
        

        # Column headings
        headings = ["", "Breakfast", "Lunch", "Dinner"]
        for j, heading in enumerate(headings):
            label = tk.Label(self, text=heading, borderwidth=1, relief="solid",font=("Comic Sans MS", 18))
            label.grid(row=0, column=j, sticky="nsew",ipadx=10,ipady=10)

        # Row headings and empty cells
        row_headings = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7"]
        self.cells = []
        for i, heading in enumerate(row_headings):
            row = []
            for j in range(columns):
                if j == 0:
                    label = tk.Label(self, text=heading, relief="solid",font=("Comic Sans MS", 18))
                else:
                    label = tk.Label(self, text="random recipe", relief="solid",font= ("Georgia",12))
                label.grid(row=i+1, column=j, sticky="nsew",ipadx=10,ipady=10)
                row.append(label)
            self.cells.append(row)

        # Configure row and column weights to make the grid resizable
        for i in range(rows + 1):
            self.grid_rowconfigure(i, weight=1)
        for j in range(columns):
            self.grid_columnconfigure(j, weight=1)
            
        self.update_table()
        
    def update_table(self):
        # Fetch data from the database
        data = self.my_db.get_random_recipes(Breakfast, 7)
        data = self.database.fetch_table_data()  # Implement this method in your Database class

        # Update table cells with fetched data
        for i, row_data in enumerate(data):
            for j, cell_data in enumerate(row_data):
                self.cells[i][j].configure(text=cell_data)        