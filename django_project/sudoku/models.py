from django.db import models
import json

class SudokuPuzzle(models.Model):
    DIFFICULTY_CHOICES = [
        ('EASY', 'Łatwy'),
        ('MEDIUM', 'Średni'),
        ('HARD', 'Trudny'),
        ('EXPERT', 'Ekspert'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    # Przechowujemy planszę początkową jako string JSON (lista 9x9)
    initial_board = models.TextField()
    # Przechowujemy rozwiązanie jako string JSON (lista 9x9)
    solution = models.TextField()
    solved = models.BooleanField(default=False)
    solve_time = models.FloatField(null=True, blank=True)  # czas rozwiązania w sekundach

    def set_initial_board(self, board):
        """Zapisuje planszę początkową jako JSON"""
        self.initial_board = json.dumps(board)

    def get_initial_board(self):
        """Pobiera planszę początkową jako listę 9x9"""
        return json.loads(self.initial_board)

    def set_solution(self, solution):
        """Zapisuje rozwiązanie jako JSON"""
        self.solution = json.dumps(solution)

    def get_solution(self):
        """Pobiera rozwiązanie jako listę 9x9"""
        return json.loads(self.solution)

    class Meta:
        ordering = ['-created_at']
        
    
    def solve_puzzle(self):
        def find_empty(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        return (i, j)
            return None

        def is_valid(board, num, pos):
            # Sprawdź wiersz
            for j in range(9):
                if board[pos[0]][j] == num and pos[1] != j:
                    return False

            # Sprawdź kolumnę
            for i in range(9):
                if board[i][pos[1]] == num and pos[0] != i:
                    return False

            # Sprawdź kwadrat 3x3
            box_x = pos[1] // 3
            box_y = pos[0] // 3
            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    if board[i][j] == num and (i, j) != pos:
                        return False
            return True

        def solve(board):
            empty = find_empty(board)
            if not empty:
                return True

            row, col = empty
            for num in range(1, 10):
                if is_valid(board, num, (row, col)):
                    board[row][col] = num
                    if solve(board):
                        return True
                    board[row][col] = 0
            return False

        # Tworzymy kopię planszy początkowej
        board = [row[:] for row in self.get_initial_board()]
        
        # Próbujemy rozwiązać
        if solve(board):
            # Jeśli się udało, zapisujemy rozwiązanie
            self.set_solution(board)
            # Zapisujemy zmiany w bazie danych
            self.save()
            return True
        return False

class SolvingAttempt(models.Model):
    puzzle = models.ForeignKey(SudokuPuzzle, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    current_board = models.TextField()  # JSON string reprezentujący aktualny stan
    is_completed = models.BooleanField(default=False)