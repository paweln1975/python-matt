import random
MAX_SIZE = 4

def random_chance(probability: float) -> bool:
    return random.uniform(0, 100) < probability

class Plant:
    def __init__(self):
        self.size = 0

    def grow(self):
        self.size += 1
        if self.size > MAX_SIZE:
            raise RuntimeError("Error in plant growth: maximum size exceeded")
        return self.size

    def harvest(self) -> bool:
        if self.size == MAX_SIZE:
            self.size = 0
            return True
        return False

    def kill(self):
        self.size = 0

class Board:

    def __init__(self, size: int):
        self.size = size
        self.harvested_count = 0
        self.grid = [[Plant() for _ in range(self.size)] for _ in range(self.size)]

    def grow_plants(self, probability: float = 50.0):
        for row in self.grid:
            for plant in row:
                if random_chance(probability):
                    plant.grow()

    def harvest_plants(self):
        for row in self.grid:
            for plant in row:
                if plant.harvest():
                    self.harvested_count += 1

    def kill_plants_for_random_row(self, death_chance: float = 10.0):
        row_index = random.randint(0, self.size - 1)
        for plant in self.grid[row_index]:
            if random_chance(death_chance):
                plant.kill()

    def kill_plants_for_random_column(self, death_chance: float = 10.0):
        col_index = random.randint(0, self.size - 1)
        for row in self.grid:
            plant = row[col_index]
            if random_chance(death_chance):
                plant.kill()

    def print_board(self):
        for row in self.grid:
            print(' '.join(str(plant.size) for plant in row))
        print()

def simulate(board_size: int, harvested_max: int, growth_probability: float = 50.0,
             death_chance: float = 10.0) -> int:
    board = Board(board_size)
    count = 0
    while True:
        board.grow_plants(growth_probability)
        board.kill_plants_for_random_row(death_chance)
        board.kill_plants_for_random_column(death_chance)
        board.print_board()
        board.harvest_plants()
        count += 1
        if board.harvested_count >= harvested_max:
            break

    return count

if __name__ == "__main__":
    board_size = 5
    harvested_max = 25
    steps = simulate(board_size, harvested_max)
    print(f"Number of step to harvest {harvested_max} plants in the {board_size}x{board_size} board: {steps}")
