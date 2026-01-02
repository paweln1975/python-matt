import random
from enum import Enum
EMPTY_CELL = '.'
FROG_CELL = 'F'
FLY_CELL = 'X'

class FrogMove(Enum):
    SUCCESS = 1
    FAIL = 0

class Board:
    """Class representing a game board for a frog game.
    Attributes:
        size (int): The size of the board (size x size).
        grid (list of lists of str): The 2D grid representing the board.
        frog_position (tuple of int): The current position of the frog on the board.
    Methods:
        load_from_file(filename): Loads the board configuration from a file.
        move_frog(new_x, new_y): Moves the frog to a new position on the board.
        display(): Displays the current state of the board.

    Data representation:
        - '.' represents an empty cell
        - 'F' represents the frog
        - 'X' represents a fly
    """
    def __init__(self, size, filename=None):
        self.size = size
        self.grid = [[EMPTY_CELL for _ in range(size)] for _ in range(size)]
        self.frog_position = (0, 0)
        self.grid[0][0] = FROG_CELL  # F represents the frog
        self.filepath = filename

        if self.filepath:
            self.load_from_file(self.filepath)

    def load_from_file(self, filename = None):
        if filename is None:
            filename = self.filepath

        if filename:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    for j, char in enumerate(line.strip()):
                        self.grid[i][j] = char
                        if char == FROG_CELL:
                            self.frog_position = (i, j)
        self._validate_board()

    def _validate_board(self):
        frog_count = sum(row.count(FROG_CELL) for row in self.grid)
        if frog_count != 1:
            raise ValueError("Board must contain exactly one frog.")

        # Ensure all rows are of correct size
        for row in self.grid:
            if len(row) != self.size:
                raise ValueError("All rows must be of size {}".format(self.size))

        # Ensure all characters are valid
        valid_chars = {EMPTY_CELL, FROG_CELL, FLY_CELL}
        for row in self.grid:
            for char in row:
                if char not in valid_chars:
                    raise ValueError("Invalid character '{}' in board.".format(char))

    def get_list_of_neighboring_flies(self):
        x, y = self.frog_position
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if self.grid[nx][ny] == FLY_CELL:
                        neighbors.append((nx, ny))
        return neighbors

    def move_frog_to_random_neighbor(self) -> FrogMove:
        neighbors = self.get_list_of_neighboring_flies()
        if neighbors:
            new_position = random.choice(neighbors)
            return self.move_frog(new_position[0], new_position[1])
        else:
            return FrogMove.FAIL

    def move_frog(self, new_x, new_y) -> FrogMove:
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            if self.grid[new_x][new_y] == FLY_CELL:
                self.grid[self.frog_position[0]][self.frog_position[1]] = EMPTY_CELL
                self.frog_position = (new_x, new_y)
                self.grid[new_x][new_y] = FROG_CELL
                return FrogMove.SUCCESS
            else:
                return FrogMove.FAIL
        else:
            raise ValueError("Move out of bounds")

    def frog_walk(self) -> list[tuple[int, int]]:
        path = []
        while True:
            move_result = self.move_frog_to_random_neighbor()
            if move_result == FrogMove.SUCCESS:
                path.append(self.frog_position)
            else:
                break
        return path

    def check_all_flies_eaten(self) -> bool:
        for row in self.grid:
            if FLY_CELL in row:
                return False
        return True

    def simulate_frog_walk(self, n: int) -> tuple[int, list[tuple[int, int]]]:
        path = []
        count = 0
        for _ in range(n):
            count += 1
            self.load_from_file()
            path = self.frog_walk()
            if self.check_all_flies_eaten():
                break

        return count, path

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()



if __name__ == "__main__":
    board = Board(5, 'board.txt')
    board.display()
    sim_count, moves = board.simulate_frog_walk(1000)
    if board.check_all_flies_eaten():
        print("Frog ate all flies!")
        print("Frog's path:", moves)
        board.display()
    else:
        print("Frog could not eat all flies.")
    print("Simulations run:", sim_count)
