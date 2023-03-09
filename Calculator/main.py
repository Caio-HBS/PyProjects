from operations import sum, subtraction, multiplication, division

import tkinter as tk
from tkinter import *
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        # The weight of a row or  column  determines  how much of the  available 
        # space it should occupy relative to other rows or columns.
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=2)
        # Configures the colour of the backgroud of the window.
        self.root.config(bg="#e4df9c")

        #----------------------------Screen Label-------------------------------
        display_string = "012345678901"
        display_image = tk.PhotoImage(file="rounded_display.png")
    

        display_label = Label(self.root, image=display_image, anchor="e")
        display_label.config(text=display_string, fg="#313638", font=("Digital-7", 42), compound=tk.TOP, anchor="center")
        display_label.grid(sticky="nsew",row=0, column=0, columnspan=4, rowspan=1, pady=(20, 40), padx=(10, 10))
        
        
        
        #-------------------------First line of buttons-------------------------

        clear_button = Button(self.root, text="C", bg="#a6c525",font=('Roboto Condensed', 36), width=2, height=1)
        clear_button.grid(sticky="n", row=1, column=0, pady=(2, 2), padx=(10, 10))

        division_button = Button(self.root, text="/", bg="#a6c525",font=('Roboto Condensed', 36), width=2, height=1)
        division_button.grid(sticky="n", row=1, column=1, pady=(2, 2), padx=(10, 10))

        multiplication_button = Button(self.root, text="*", bg="#a6c525",font=('Roboto Condensed', 36), width=2, height=1)
        multiplication_button.grid(sticky="n", row=1, column=2, pady=(2, 2), padx=(10, 10))

        minus_button = Button(self.root, text="-", bg="#f22b29",font=('Roboto Condensed', 36), width=2, height=1)
        minus_button.grid(sticky="n", row=1, column=3, pady=(2, 2), padx=(10, 10))


        #------------------------Second line of buttons-------------------------

        seven_button = Button(self.root, text="7", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        seven_button.grid(sticky="n", row=2, column=0, pady=(2, 2), padx=(10, 10))

        eight_button = Button(self.root, text="8", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        eight_button.grid(sticky="n", row=2, column=1, pady=(2, 2), padx=(10, 10))

        nine_button = Button(self.root, text="9", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        nine_button.grid(sticky="n", row=2, column=2, pady=(2, 2), padx=(10, 10))

        plus_button = Button(self.root, text="+", bg="#f22b29",font=('Roboto Condensed', 36), width=2, height=3)
        plus_button.grid(sticky="n", row=2, column=3, pady=(2, 2), rowspan=2, padx=(10, 10))


        #------------------------Third line of buttons--------------------------

        four_button = Button(self.root, text="4", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        four_button.grid(sticky="n", row=3, column=0, pady=(2, 2), padx=(10, 10))

        five_button = Button(self.root, text="5", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        five_button.grid(sticky="n", row=3, column=1, pady=(2, 2), padx=(10, 10))

        six_button = Button(self.root, text="6", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        six_button.grid(sticky="n", row=3, column=2, pady=(2, 2), padx=(10, 10))


        #------------------------Fourth line of buttons-------------------------

        one_button = Button(self.root, text="1", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        one_button.grid(sticky="n", row=4, column=0, pady=(2, 2), padx=(5, 5))

        two_button = Button(self.root, text="2", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        two_button.grid(sticky="n", row=4, column=1, pady=(2, 2), padx=(5, 5))

        three_button = Button(self.root, text="3", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        three_button.grid(sticky="n", row=4, column=2, pady=(2, 2), padx=(5, 5))

        equal_button = Button(self.root, text="=", bg="#f22b29",font=('Roboto Condensed', 36), width=2, height=2)
        equal_button.grid(sticky="n", row=4, column=3, rowspan=2, pady=(2, 2), padx=(5, 5))


        #------------------------Fifth line of buttons--------------------------

        zero_button = Button(self.root, text="0", bg="#2176ff",font=('Roboto Condensed', 42), width=5, height=1)
        zero_button.grid(sticky="n", row=5, column=0, columnspan=2, pady=(2, 2), padx=(10, 10))

        dot_button = Button(self.root, text=".", bg="#2176ff",font=('Roboto Condensed', 36), width=2, height=1)
        dot_button.grid(sticky="n", row=5, column=2, pady=(10, 2), padx=(10, 10))

        


if __name__ == '__main__':
    window = Tk()
    window.title("Calculator")
    #window.geometry("450x700")

    app = Calculator(window)

    # Mainloop is a infinite loop  function that keeps the program running until
    # we close it, that is why we have to put it at the end of the code.
    window.mainloop()
    