class SudokuSolver:
    def __init__(self, board):
        # Konwertujemy planszę na listę list (macierz 9x9)
        self.board = [row[:] for row in board]
        # Przechowujemy możliwe wartości dla każdej komórki
        self.possibilities = [[set(range(1, 10)) if self.board[i][j] == 0 
                             else set() for j in range(9)] for i in range(9)]
        
    def is_valid(self, row, col, num):
        # Sprawdzenie wiersza
        for x in range(9):
            if self.board[row][x] == num:
                return False
        # Sprawdzenie kolumny
        for x in range(9):
            if self.board[x][col] == num:
                return False
        # Sprawdzenie kwadratu 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self):
        # Implementacja algorytmu rozwiązującego
        # (będziemy implementować w kolejnym kroku)
        pass

    def get_board(self):
        return self.board