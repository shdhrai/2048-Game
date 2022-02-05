import tkinter as tk
import random
import colors as c


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        # Creating the Grid frame with width = 500 & height = 500
        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=4, width=500, height=500)
        self.main_grid.grid(pady=(100,10))
        self.main_grid.grid(padx=(10, 10))
        self.make_GUI()
        self.start_game()

        # Binding the Keys with movement that act as an event
        self.master.bind('1', self.left)
        self.master.bind('2', self.right)
        self.master.bind('3', self.up)
        self.master.bind('4', self.down)

        # Used to run the GUI window continuously
        self.mainloop()


    def make_GUI(self):
        # making tabular cells
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=125,
                    height=125)
                cell_frame.grid(row=i, column=j, padx=4, pady=4)
                cell_number = tk.Label(self.main_grid, bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        # making score board
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=50, anchor="center")
        tk.Label(
            score_frame,
            text="Score",
            fg ="#ff82ab",
            font=c.SCORE_LABEL_FONT).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0",relief = "solid", font=c.SCORE_FONT)
        self.score_label.grid(row=1)

    # Defining Starting state for the GUI
    def start_game(self):
        # creating intial matrix states for game
        self.matrix = [[0] * 4 for _ in range(4)]

        # fill 2 random cells with 2 or 4
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2,4])
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[self.matrix[row][col]])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[self.matrix[row][col]],
            fg=c.CELL_NUMBER_COLORS[self.matrix[row][col]],
            font=c.CELL_NUMBER_FONTS[self.matrix[row][col]],
            text=self.matrix[row][col])
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2,4])
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[self.matrix[row][col]])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[self.matrix[row][col]],
            fg=c.CELL_NUMBER_COLORS[self.matrix[row][col]],
            font=c.CELL_NUMBER_FONTS[self.matrix[row][col]],
            text=self.matrix[row][col])

        self.score = 0


    # Matrix Operations

    def stack(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix

    # Function to combine the same numbers that are near to each other.
    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]


    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix


    def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix


    # Adding a new 2 or 4 tile randomly to an empty cell after each move

    def add_new_tile(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4]) # Randomly select between 2 & 4


    # Updating the UI after every move

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(
                        bg=c.EMPTY_CELL_COLOR, text="")
                else:
                    self.cells[i][j]["frame"].configure(
                        bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.CELL_COLORS[cell_value],
                        fg=c.CELL_NUMBER_COLORS[cell_value],
                        font=c.CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks() # Update the widget task immediately


    # Keys for Movement(1 - Left, 2 - Right, 3 - Up, 4 - Down)

    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    # Checks whether we can play any move or not

    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False


    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False


    # Check if Game is Over

    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=3)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="Winner",
                bg=c.WINNER_BG,
                relief ="groove",
                fg=c.GAME_OVER_FONT_COLOR,
                font=c.GAME_OVER_FONT).pack()
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=3)
            game_over_frame.place(relx=0.5, rely=0.75, anchor="center")
            tk.Label(
                game_over_frame,
                text="Game Over",
                bg=c.LOSER_BG,
                relief="solid",
                fg=c.GAME_OVER_FONT_COLOR,
                font=c.GAME_OVER_FONT).pack()


def main():
    Game()


if __name__ == "__main__":
    main()