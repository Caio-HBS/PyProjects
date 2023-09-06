import tkinter as tk
import ttkbootstrap as ttk

from tkinter import filedialog


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Siren")
        style = ttk.Style(theme="solar")
        style.theme_use()
        # self.root.geometry("1280x720")

        self.setup_screen()

    def setup_screen(self):
        """
        Renders the main page with the folder select screen.
        """
        tittle_main_menu = ttk.Label(
            master=root, text="Welcome to Siren", font="Arial 42 bold", padding=100
        )
        tittle_main_menu.pack()

        explanation = ttk.Label(
            master=root,
            text="""To begin, provide the path to the folder containing the 
            images you want Siren to take a look at""",
            font="Arial 12",
            padding=10,
        )
        explanation.pack()

        self.file_path_var = tk.StringVar(value="Click to choose folder path")

        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=(10, 50))

        file_path = ttk.Label(
            master=frame,
            textvariable=self.file_path_var,
            padding=5,
            background="black",
            width=40,
        )
        file_path.pack(side=tk.LEFT)
        file_path.bind("<Button-1>", lambda event: self.update_file_path())
        find_duplicates_button = ttk.Button(
            master=frame,
            text="Find duplicates!",
            command=self.check_and_render_second_page,
        )
        find_duplicates_button.pack(side=tk.LEFT)

        self.delete_duplicates_var = tk.StringVar(value="MOVE Files")

        change_folder_radio_button = ttk.Radiobutton(
            master=root,
            text="MOVE duplicates to another folder",
            variable=self.delete_duplicates_var,
            value="MOVE Files",
            padding=5,
        )
        change_folder_radio_button.pack()

        delete_duplicates_radio_button = ttk.Radiobutton(
            master=root,
            text="DELETE duplicates",
            variable=self.delete_duplicates_var,
            value="DELETE Files",
            padding=5,
        )
        delete_duplicates_radio_button.pack()

    def choose_files_screen(self):
        """
        Renders the secondary screen where the user selects what files will be
        kept and what files will be moved/deleted.
        """
        duplicates_label = ttk.Label(
            master=self.root,
            text="Found duplicates",
            font="Arial 12 bold",
        )
        duplicates_label.grid(row=0, column=0, padx=15, pady=(5, 1), sticky="w")

        main_frame = ttk.Frame(master=self.root)#, borderwidth=2, relief="solid")
        main_frame.grid(row=1, column=0, padx=10, pady=(1, 10), sticky="nsew")
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        right_frame = ttk.Frame(
            master=main_frame, 
            borderwidth=2, 
            relief="solid", 
            width=740, 
            height=600
        )
        right_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        left_frame = ttk.Frame(main_frame, borderwidth=2, relief="solid")
        left_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

        execute_button = ttk.Button(
            master=left_frame, 
            text=self.delete_duplicates_var.get(),
        )
        execute_button.grid(row=0, column=0, padx=10, pady=10)

        label1 = ttk.Label(
            master=left_frame, 
            text=
"""
WARNING: if you selected the option to 
delete the duplicate files on the previous menu, 
know that you won't ever be able to recover them.
""",
            justify="center"
        )
        label1.grid(row=1, column=0, padx=1, pady=10)

        label2 = ttk.Label(
            master=left_frame,
            text="""
If you chose the option to move the duplicates, we 
will automatically create a folder called "duplicates" 
inside the folder you selected on the previous screen.
            """,
            justify="center"
        )
        label2.grid(row=2, column=0, padx=1, pady=10)

        version_label = ttk.Label(main_frame, text="Ver. 1.0.0 - Caio Bianchi", anchor="se", font="Arial 8")
        version_label.grid(row=1, column=1, padx=1, pady=5, sticky="se")



# ---------------------------------FUNCTIONS---------------------------------- #

    def update_file_path(self):
        """
        Renders the choose folder window and sets its path to the StringVar
        already initialized.
        """
        file_path = filedialog.askdirectory()
        if file_path:
            self.file_path_var.set(file_path)

    def clear_current_page(self):
        """
        Destroys all the widgets in the current page.
        """
        for widget in self.root.pack_slaves():
            widget.destroy()

    def check_and_render_second_page(self):
        """
        Checks to see if the file file_path_var actually has a path. Proceeds if
        it has one.
        """
        if self.file_path_var.get() != "Click to choose folder path":
            self.clear_current_page()
            self.choose_files_screen()


root = tk.Tk()
window = MainWindow(root)
root.mainloop()
