import tkinter as tk
from tkinter import *
from tkinter import ttk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.display_string = ""
        self.operator = ""
        self.button_queue = []
        self.root.config(bg="#e4df9c")

        self.display_image = tk.PhotoImage(file="assets/rounded_display.png")
        self.green_C_button = tk.PhotoImage(file="assets/buttons/green_C_button.png")
        self.green_division_button = tk.PhotoImage(
            file="assets/buttons/green_division_button.png"
        )
        self.green_times_button = tk.PhotoImage(
            file="assets/buttons/green_times_button.png"
        )
        self.red_minus_button = tk.PhotoImage(
            file="assets/buttons/red_minus_button.png"
        )
        self.blue_7_button = tk.PhotoImage(file="assets/buttons/blue_7_button.png")
        self.blue_8_button = tk.PhotoImage(file="assets/buttons/blue_8_button.png")
        self.blue_9_button = tk.PhotoImage(file="assets/buttons/blue_9_button.png")
        self.red_plus_button = tk.PhotoImage(file="assets/buttons/red_plus_button.png")
        self.blue_4_button = tk.PhotoImage(file="assets/buttons/blue_4_button.png")
        self.blue_5_button = tk.PhotoImage(file="assets/buttons/blue_5_button.png")
        self.blue_6_button = tk.PhotoImage(file="assets/buttons/blue_6_button.png")
        self.blue_1_button = tk.PhotoImage(file="assets/buttons/blue_1_button.png")
        self.blue_2_button = tk.PhotoImage(file="assets/buttons/blue_2_button.png")
        self.blue_3_button = tk.PhotoImage(file="assets/buttons/blue_3_button.png")
        self.red_equals_button = tk.PhotoImage(
            file="assets/buttons/red_equals_button.png"
        )
        self.blue_0_button = tk.PhotoImage(file="assets/buttons/blue_0_button.png")
        self.blue_dot_button = tk.PhotoImage(file="assets/buttons/blue_dot_button.png")

        # ----------------------------Display Label-----------------------------
        self.display_label = tk.Label(self.root, image=self.display_image, bg="#e4df9c")
        self.display_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.display_label.grid(
            sticky="nsew",
            row=0,
            column=0,
            columnspan=4,
            rowspan=1,
            pady=(20, 40),
            padx=(10, 10),
        )

        self.text_label_inside_display = tk.Label(
            self.display_label,
            text=self.display_string,
            font=("Digital-7", 41),
            fg="#313638",
            bg="#c4dce5",
        )
        self.text_label_inside_display.place(relx=0.99, rely=0.5, anchor="e")

        # -------------------------First line of buttons------------------------
        clear_button = tk.Button(
            self.root,
            image=self.green_C_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.clear_display(),
        )
        clear_button.grid(sticky="n", row=1, column=0, pady=(2, 2), padx=(10, 10))

        division_button = tk.Button(
            self.root,
            image=self.green_division_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display("/"),
        )
        division_button.grid(sticky="n", row=1, column=1, pady=(2, 2), padx=(10, 10))

        multiplication_button = tk.Button(
            self.root,
            image=self.green_times_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display("*"),
        )
        multiplication_button.grid(
            sticky="n", row=1, column=2, pady=(2, 2), padx=(10, 10)
        )

        minus_button = tk.Button(
            self.root,
            image=self.red_minus_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display("-"),
        )
        minus_button.grid(sticky="n", row=1, column=3, pady=(2, 2), padx=(10, 10))

        # ------------------------Second line of buttons------------------------
        seven_button = tk.Button(
            self.root,
            image=self.blue_7_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(7),
        )
        seven_button.grid(sticky="n", row=2, column=0, pady=(2, 2), padx=(10, 10))

        eight_button = tk.Button(
            self.root,
            image=self.blue_8_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(8),
        )
        eight_button.grid(sticky="n", row=2, column=1, pady=(2, 2), padx=(10, 10))

        nine_button = tk.Button(
            self.root,
            image=self.blue_9_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(9),
        )
        nine_button.grid(sticky="n", row=2, column=2, pady=(2, 2), padx=(10, 10))

        plus_button = tk.Button(
            self.root,
            image=self.red_plus_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display("+"),
        )
        plus_button.grid(
            sticky="n", row=2, column=3, pady=(2, 2), rowspan=2, padx=(10, 10)
        )

        # ------------------------Third line of buttons-------------------------
        four_button = tk.Button(
            self.root,
            image=self.blue_4_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(4),
        )
        four_button.grid(sticky="n", row=3, column=0, pady=(15, 2), padx=(10, 10))

        five_button = tk.Button(
            self.root,
            image=self.blue_5_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(5),
        )
        five_button.grid(sticky="n", row=3, column=1, pady=(15, 2), padx=(10, 10))

        six_button = tk.Button(
            self.root,
            image=self.blue_6_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(6),
        )
        six_button.grid(sticky="n", row=3, column=2, pady=(15, 2), padx=(10, 10))

        # ------------------------Fourth line of buttons------------------------
        one_button = tk.Button(
            self.root,
            image=self.blue_1_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(1),
        )
        one_button.grid(sticky="n", row=4, column=0, pady=(2, 2), padx=(10, 10))

        two_button = tk.Button(
            self.root,
            image=self.blue_2_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(2),
        )
        two_button.grid(sticky="n", row=4, column=1, pady=(2, 2), padx=(10, 10))

        three_button = tk.Button(
            self.root,
            image=self.blue_3_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(3),
        )
        three_button.grid(sticky="n", row=4, column=2, pady=(2, 2), padx=(10, 10))

        equal_button = tk.Button(
            self.root,
            image=self.red_equals_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.result(),
        )
        equal_button.grid(
            sticky="n", row=4, column=3, pady=(2, 2), rowspan=2, padx=(10, 10)
        )

        # ------------------------Fifth line of buttons-------------------------
        zero_button = tk.Button(
            self.root,
            image=self.blue_0_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display(0),
        )
        zero_button.grid(
            sticky="n", row=5, column=0, columnspan=2, pady=(15, 0), padx=(10, 10)
        )

        dot_button = tk.Button(
            self.root,
            image=self.blue_dot_button,
            bg="#e4df9c",
            borderwidth=0,
            highlightbackground="#e4df9c",
            activebackground="#e4df9c",
            command=lambda: self.update_display("."),
        )
        dot_button.grid(sticky="n", row=5, column=2, pady=(15, 0), padx=(10, 10))

    def update_display(self, digit: str):
        """
        Changes what is displayed on the virtual screen.

        Args:
            digit: the desired number/operators.
        """
        # Prevents the user from starting a number with ".".
        if self.display_string == "" and digit == ".":
            return

        # Prevents the user from doing any calculations after an error before
        # clearing the queue.
        if self.display_string == "ERROR":
            return

        valid_operators = ["+", "-", "/", "*"]
        if str(digit) in valid_operators:
            # Prevents the user from starting a calculation by the operator.
            if self.display_string == "":
                return

            # Limts the calculator to only do one calculation at a time.
            for character in self.display_string:
                if character in valid_operators:
                    return

        # Limits the lenght of the string.
        if len(self.display_string) < 11:
            self.display_string += str(digit)
            self.text_label_inside_display.config(text=self.display_string)
            self.button_queue.append(digit)
            if str(digit) in valid_operators:
                self.operator = str(digit)
        else:
            return

    def clear_display(self):
        """
        Clears whatever is on the display.
        """
        self.display_string = ""
        self.text_label_inside_display.config(text=self.display_string)
        self.button_queue.clear()

    def result(self):
        """
        Does the operation.
        """
        if self.display_string == "":
            return
        if self.operator == "":
            return
        elif self.operator in self.display_string:
            (num1, num2) = self.display_string.split(self.operator)
        elif (
            num1 == None
            or num1 == ""
            or num2 == None
            or num2 == ""
            or self.operator == ""
        ):
            return

        # Separates the interger from the floats.
        if "." in num1:
            num1 = float(num1)
        else:
            num1 = int(num1)

        if "." in num2:
            num2 = float(num2)
        else:
            num2 = int(num2)

        # Handles the calculation.
        if self.operator == "+":
            result = num1 + num2
            self.display_string = f"{str(result):.11}"
            self.text_label_inside_display.config(text=self.display_string)
            self.operator = ""
            self.button_queue.clear()

        if self.operator == "-":
            result = num1 - num2
            self.display_string = f"{str(result):.11}"
            self.text_label_inside_display.config(text=self.display_string)
            self.operator = ""
            self.button_queue.clear()

        if self.operator == "*":
            result = num1 * num2
            self.display_string = f"{str(result):.11}"
            self.text_label_inside_display.config(text=self.display_string)
            self.operator = ""
            self.button_queue.clear()

        if self.operator == "/":
            if num2 == 0:
                result = "ERROR"
                self.display_string = result
                self.text_label_inside_display.config(text=self.display_string)
                self.operator = ""
                self.button_queue.clear()
            else:
                result = num1 / num2
                self.display_string = f"{str(result):.11}"
                self.text_label_inside_display.config(text=self.display_string)
                self.operator = ""
                self.button_queue.clear()


if __name__ == "__main__":
    window = Tk()
    window.title("Calculator")
    # window.geometry("450x700")

    app = Calculator(window)

    window.mainloop()
