import tkinter as tk
from tkinter import *
from tkinter import ttk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#e4df9c")
        self.root.geometry("450x700")

        # Criando a imagem de fundo
        bg_image = tk.PhotoImage(file="rounded_display.png")

        # Criando a label e definindo a imagem de fundo e texto
        display_label = Label(self.root, image=bg_image, font=('Digit-7', 42), anchor="e")
        display_label.config(text="Seu texto aqui", fg="red", font=("Arial", 20), compound=tk.TOP, justify="center")

        # Posicionando a label usando o método grid e centralizando o texto dentro dela
        display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="NSEW")

        # Configurando as opções de redimensionamento para as células da grade
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

if __name__ == '__main__':
    window = Tk()
    window.title("Calculator")
    #window.geometry("450x700")

    app = Calculator(window)

    # Mainloop is a infinite loop  function that keeps the program running until
    # we close it, that is why we have to put it at the end of the code.
    window.mainloop()