import tkinter as tk
import ttkbootstrap as ttk

from tkinter import filedialog


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Siren")
        style = ttk.Style(theme="solar")
        style.theme_use()
        self.root.geometry("1280x720")
        self.setup_screen()

    def setup_screen(self):
        """
        Function used to select the folder path and choose what to do with the
        duplicate files.
        """
        tittle_main_menu = ttk.Label(
            master=root, 
            text="Welcome to Siren", 
            font="Arial 42 bold", 
            padding=100
        )
        tittle_main_menu.pack()

        explanation = ttk.Label(
            master=root,
            text="""To begin, provide the path to the folder containing the 
            images you want Siren to take a look at""",
            font="Arial 12",
            padding=10
        )
        explanation.pack()

        self.var = tk.StringVar(value="Click to choose folder path")

        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=(10, 50))

        file_path = ttk.Label(
            master=frame,
            textvariable=self.var,
            padding=5,
            background="black",
            width=40
        )
        file_path.pack(side=tk.LEFT)
        file_path.bind("<Button-1>", lambda event: self.update_file_path())
        find_duplicates_button = ttk.Button(
            master=frame,
            text="Find duplicates!",
            # command=self.update_file_path
        )
        find_duplicates_button.pack(side=tk.LEFT)

        self.delete_duplicates_var = tk.BooleanVar()
        change_folder_radio_button = ttk.Radiobutton(
            master=root,
            text="MOVE duplicates to another folder",
            variable=self.delete_duplicates_var,
            value=False,
            padding=5
        )
        change_folder_radio_button.pack()

        delete_duplicates_radio_button = ttk.Radiobutton(
            master=root,
            text="DELETE duplicates",
            variable=self.delete_duplicates_var,
            value=True,
            padding=5
        )
        delete_duplicates_radio_button.pack()

    def update_file_path(self):
            file_path = filedialog.askdirectory()
            if file_path:
                self.var.set(file_path)


    def choose_files_screen(self):
        pass


root = tk.Tk()
window =  MainWindow(root)
root.mainloop()