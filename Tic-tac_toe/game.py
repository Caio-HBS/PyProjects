import tkinter as tk
import ttkbootstrap as ttk

# TODO: Add functions.
# TODO: Add final screen to show success or failure.

BASE_GAME_GRID = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.players = [
            {"name": "player1", "symbol": "X", "string": "Player 1"},
            {"name": "player2", "symbol": "O", "string": "Player 2"},
        ]
        self.current_player = self.players[0]
        self.count = 0
        self.game_grid = BASE_GAME_GRID
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
            master=self.root, text="Player 1", font="Arial 24 bold", padding=10
        )
        player1_label.grid(row=0, column=0)

        player2_label = ttk.Label(
            master=self.root, text="Player 2", font="Arial 24", padding=10
        )
        player2_label.grid(row=0, column=2)

        # Handles the 3x3 grid of buttons.
        for i in range(3):
            for j in range(3):
                button = ttk.Button(
                    master=self.root,
                    text="",
                    command=lambda i=i, j=j: self.on_button_click(i, j),
                )
                button.grid(row=i + 1, column=j, padx=10, pady=10)

    def on_button_click(self, row: int, col: int):
        """
        Handles updating the `game_grid` as well as the styling on the player labels.

        Args:
            row: the row of the pressed button;
            col: the column of the pressed button.
        """
        # Prevents from clicking cells with values.
        if self.game_grid[row][col] is None:
            self.game_grid[row][col] = (
                "X" if self.current_player["name"] == "player1" else "O"
            )

            # Update text on the buttons.
            button = self.root.grid_slaves(row=row + 1, column=col)[0]
            button["text"] = self.game_grid[row][col]

            # Inverts the player (and its styling) after a valid move.
            player1_label = self.root.grid_slaves(row=0, column=0)[0]
            player2_label = self.root.grid_slaves(row=0, column=2)[0]

            if self.current_player["name"] == "player1":
                self.current_player = self.players[1]
                player1_label.config(font="Arial 24")
                player2_label.config(font="Arial 24 bold")
            else:
                self.current_player = self.players[0]
                player1_label.config(font="Arial 24 bold")
                player2_label.config(font="Arial 24")

            self.count += 1

            if self.count == 9:
                # TODO: trigger draw screen.
                return
            else:
                if self.check_game_status():
                    print(f"{self.current_player['string']} won")

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
            if row[0] == row[1] == row[2] and row[0] != None:
                return True

        # Three consecutive "X's" or "O's" in the same a column.
        if self.game_grid[0][0] == self.game_grid[1][0] == self.game_grid[2][0] and self.game_grid[0][0] != None:
            return True
        if self.game_grid[0][1] == self.game_grid[1][1] == self.game_grid[2][1] and self.game_grid[0][1] != None:
            return True
        if self.game_grid[0][2] == self.game_grid[1][2] == self.game_grid[2][2] and self.game_grid[0][2] != None:
            return True

        # Three consecutive "X's" or "O's" in the each diagonal.
        if self.game_grid[0][0] == "X" and self.game_grid[1][1] == "X" and self.game_grid[2][2] == "X":
            return True
        elif self.game_grid[0][0] == "O" and self.game_grid[1][1] == "O" and self.game_grid[2][2] == "O":
            return True

        if self.game_grid[0][2] == "X" and self.game_grid[1][1] == "X" and self.game_grid[2][0] == "X":
            return True
        elif self.game_grid[0][2] == "O" and self.game_grid[1][1] == "O" and self.game_grid[2][0] == "O":
            return True
        
        # TODO: handle draw.

        # No winners.
        return False
