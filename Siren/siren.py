import os
import tkinter as tk
import ttkbootstrap as ttk

from tkinter import filedialog
from PIL import Image, ImageTk
from difPy import dif


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Siren")
        style = ttk.Style(theme="solar")
        style.theme_use()
        #self.root.geometry("1165x695")

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
            padding=(10, 10),
        )
        duplicates_label.pack(anchor="nw")

        main_frame = ttk.Frame(master=self.root, width=1145, height=695)
        main_frame.pack()
        main_frame.pack_propagate(0)

        left_frame = ttk.Frame(
            master=main_frame,
            #height=600,
            #width=1000,
            borderwidth=2,
            relief="solid",
        )
        left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        left_frame.pack_propagate(0)

        # Create a canvas for the left_frame
        canvas = tk.Canvas(left_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar for the canvas
        scrollbar = tk.Scrollbar(left_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to contain the image thumbnails
        image_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=image_frame, anchor=tk.NW)

        image_thumbnails = self.load_image_thumbnails()
        self.image_labels = []
        num_columns = 6

        if image_thumbnails:
            for i, img_tk in enumerate(image_thumbnails):
                row = i // num_columns
                col = i % num_columns
                label = ttk.Label(left_frame, image=img_tk)
                label.image = img_tk
                label.grid(row=row, column=col, padx=9, pady=9)
                self.image_labels.append(label)

            # Bind mouse wheel events to the canvas for scrolling
            canvas.bind("<Configure>", lambda event, canvas=canvas: self.on_canvas_configure(event))
        else:
            no_duplicates_found_label = ttk.Label(
                master=left_frame, 
                text="No duplicates found", 
                font="Arial 12 bold"
            )
            no_duplicates_found_label.pack(anchor="nw", padx=10, pady=10,)

        right_frame = ttk.Frame(
            master=main_frame, 
            borderwidth=2, 
            relief="solid", 
        )
        right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        right_frame.pack_propagate(0)
        # TODO: handle the files.
        execute_button = ttk.Button(
            master=right_frame,
            text=self.delete_duplicates_var.get(),
        )
        execute_button.grid(row=0, column=0, padx=10, pady=10)

        label1 = ttk.Label(
            master=right_frame,
            text="""
WARNING: if you selected the option to 
delete the duplicate files on the previous menu, 
know that you won't ever be able to recover them.
""",
            justify="center",
        )
        label1.grid(row=1, column=0, padx=1, pady=10)

        label2 = ttk.Label(
            master=right_frame,
            text="""
If you chose the option to move the duplicates, we 
will automatically create a folder called "duplicates" 
inside the folder you selected on the previous screen.
            """,
            justify="center",
        )
        label2.grid(row=2, column=0, padx=1, pady=10)

        version_label = ttk.Label(
            right_frame, text="Ver. 1.0.0 - Caio Bianchi", anchor="se", font="Arial 8"
        )
        version_label.pack(side=tk.BOTTOM)
        version_label.pack_propagate(0)

    # ---------------------------------FUNCTIONS---------------------------------- #

    def update_file_path(self):
        """
        Renders the choose folder window and sets its path to the StringVar
        already initialized. If there are no image files on the folder, prompts
        the user for a new folder.
        """
        files_in_folder = []
        file_path = filedialog.askdirectory()

        for filename in os.listdir(file_path):
            if filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
                files_in_folder.append(filename)

        if files_in_folder == []:
            self.file_path_var.set("No images, select another folder")
        else:
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
        it has one. Also doesn't let the user proceed if there are no images on
        the selected folder.
        """
        if (self.file_path_var.get() != "Click to choose folder path") and (
            self.file_path_var.get() != "No images, select another folder"
        ):
            self.clear_current_page()
            self.choose_files_screen()

    def load_image_thumbnails(self):
        folder_path = self.file_path_var.get()
        duplicates = []
        image_thumbnails = []

        x = dif(folder_path)
        result_json = x.result

        for key, value in result_json.items():
            duplicates.append(os.path.basename(value["location"]))
            matches = value.get("matches", {})
            for match_data in matches.values():
                duplicates.append(os.path.basename(match_data["location"]))

        for filename in duplicates:
            img = Image.open(os.path.join(folder_path, filename))
            img.thumbnail((100, 100))
            img_tk = ImageTk.PhotoImage(img)
            image_thumbnails.append(img_tk)
        return image_thumbnails

root = tk.Tk()
window = MainWindow(root)
root.mainloop()
