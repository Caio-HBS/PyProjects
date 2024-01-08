import tkinter as tk
import ttkbootstrap as ttk

# TODO: Add player tracking.
# TODO: Add functions.
# TODO: Add final screen to show success or failure.


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.game_grid = [[None, None, None], [None, None, None], [None, None, None]]
        self.root.title("Tic-Tac Toe")
        style = ttk.Style(theme="solar")
        style.theme_use()
        self.root.geometry("500x500")

        self.main_title_screen()

    def main_title_screen(self):
        """
        Renders the main menu screen.
        """
        tittle_main_menu = ttk.Label(
            master=self.root, text="Tic-Tac Toe", font="Arial 42 bold", padding=10
        )

        tittle_main_menu.pack()

        start_game_button_style = ttk.Style()
        start_game_button_style.configure("primary.TButton", font="Arial 24 bold")
        start_game_button = ttk.Button(
            master=self.root,
            text="Start Game",
            padding=10,
            cursor="hand2",
            style="primary.TButton",
            command=lambda: self.kill_current_screen_and_draw_new_one(self.game_screen),
        )
        start_game_button.pack(pady=165)

        creator = ttk.Label(master=self.root, text="made by: Caio Bianchi")
        creator.pack()

        version = ttk.Label(master=self.root, text="ver. 0.0.1")
        version.pack(anchor="se")

    def game_screen(self):
        """
        Renders the game screen.
        """
        player1_label = ttk.Label(
            master=self.root, text="Player 1", font="Arial 24", padding=10
        )
        player1_label.grid(row=0, column=0, padx=10, pady=10)

        player2_label = ttk.Label(
            master=self.root, text="Player 2", font="Arial 24 bold", padding=10
        )
        player2_label.grid(row=0, column=1, padx=10, pady=10)

        # Creating a 3x3 grid of buttons
        for i in range(3):
            for j in range(3):
                button = ttk.Button(
                    master=self.root,
                    text="",
                    command=lambda i=i, j=j: self.on_button_click(i, j),
                )
                button.grid(row=i + 1, column=j, padx=10, pady=10)

    def on_button_click(self, row: int, col: int, current_player: str):
        """
        Handles updating the `game_grid` as well as the styling on the player labels.

        Args:
            row: the row of the pressed button;
            col: the column of the pressed button;
            current_player: the player who clicked the button.
        """
        # Prevents from clicking cells with values:
        if self.game_grid[row][col] is None:
            self.game_grid[row][col] = "X" # TODO: add styling change on the labels based on who's turn it is.
            print(self.game_grid)

        

    def kill_current_screen_and_draw_new_one(self, new_window):
        """
        Kills the current drawn screen and calls the new one.

        Args:
            new_window: the window to be rendered after killing the last one.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

        new_window()

    def check_game_status(self) -> bool:
        """
        Checks if the game is over and returns a boolean based on it.
        """

        # Three consecutive "X's" or "O's" in the same a row.
        for row in self.game_grid:
            if all(cell == row[0] for cell in row if cell is not None):
                return True

        # Three consecutive "X's" or "O's" in the same a column.
        for col in range(3):
            if all(
                row[col] == self.game_grid[0][col]
                for row in self.game_grid
                if row[col] is not None
            ):
                return True

        # Three consecutive "X's" or "O's" in the main diagonal (NW to SE).
        if all(
            self.game_grid[i][i] == self.game_grid[0][0]
            for i in range(3)
            if self.game_grid[i][i] is not None
        ):
            return True

        # Three consecutive "X's" or "O's" in the secondary diagonal (SW to NE).
        if all(
            self.game_grid[i][2 - i] == self.game_grid[0][2]
            for i in range(3)
            if self.game_grid[i][2 - i] is not None
        ):
            return True

        # No winners.
        return False
