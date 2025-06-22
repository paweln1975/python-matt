from django import forms
from .models import SudokuPuzzle

class SudokuPuzzleForm(forms.ModelForm):
    class Meta:
        model = SudokuPuzzle
        fields = ['difficulty']
        labels = {
            'difficulty': 'Poziom trudności',
        }

    # Pola dla każdej komórki planszy 9x9
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for row in range(9):
            for col in range(9):
                field_name = f'cell_{row}_{col}'
                self.fields[field_name] = forms.IntegerField(
                    required=False,
                    min_value=0,
                    max_value=9,
                    widget=forms.NumberInput(attrs={
                        'class': 'sudoku-cell',
                        'data-row': row,
                        'data-col': col,
                    })
                )


class SudokuSolveForm(forms.Form):
    def __init__(self, puzzle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial_board = puzzle.get_initial_board()

        for row in range(9):
            for col in range(9):
                field_name = f'cell_{row}_{col}'
                initial_value = initial_board[row][col]

                self.fields[field_name] = forms.IntegerField(
                    required=False,
                    min_value=1,
                    max_value=9,
                    widget=forms.NumberInput(attrs={
                        'class': 'sudoku-cell',
                        'data-row': row,
                        'data-col': col,
                        'readonly': initial_value != 0,
                        'value': initial_value if initial_value != 0 else '',
                    })
                )
