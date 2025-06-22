import json
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import SudokuPuzzle, SolvingAttempt
from .forms import SudokuPuzzleForm, SudokuSolveForm
from django.contrib import messages

def puzzle_list(request):
    puzzles = SudokuPuzzle.objects.all()
    return render(request, 'sudoku/puzzle_list.html', {'puzzles': puzzles})

def puzzle_detail(request, pk):
    puzzle = get_object_or_404(SudokuPuzzle, pk=pk)
    return render(request, 'sudoku/puzzle_detail.html', {'puzzle': puzzle})


def puzzle_create(request):
    if request.method == 'POST':
        form = SudokuPuzzleForm(request.POST)
        if form.is_valid():
            # Tworzymy planszę 9x9 wypełnioną zerami
            board = [[0 for _ in range(9)] for _ in range(9)]

            # Wypełniamy planszę danymi z formularza
            for row in range(9):
                for col in range(9):
                    field_name = f'cell_{row}_{col}'
                    value = form.cleaned_data.get(field_name)
                    # Jeśli wartość jest None (puste pole), ustawiamy 0
                    board[row][col] = value if value is not None else 0

            puzzle = form.save(commit=False)
            puzzle.set_initial_board(board)
            # Tymczasowo ustawiamy solution jako kopię initial_board
            # W przyszłości można dodać algorytm rozwiązujący
            puzzle.set_solution(board)
            puzzle.save()

            messages.success(request, 'Łamigłówka została utworzona pomyślnie!')
            return redirect('sudoku:puzzle_list')
        else:
            messages.error(request, 'Proszę poprawić błędy w formularzu.')
    else:
        form = SudokuPuzzleForm()

    return render(request, 'sudoku/puzzle_form.html', {
        'form': form,
        'action': 'create'  # Dodajemy zmienną action
    })


def puzzle_solve(request, pk):
    puzzle = get_object_or_404(SudokuPuzzle, pk=pk)
    
    if not puzzle:
        messages.error(request, 'Nie znaleziono takiej łamigłówki.')
        return redirect('sudoku:puzzle_list')
        
    solution = puzzle.get_solution()

    if request.method == 'POST':
        form = SudokuSolveForm(puzzle, request.POST)
        if not form.is_valid():
            messages.error(request, 'Formularz zawiera błędy. Sprawdź wprowadzone dane.')
            return render(request, 'sudoku/puzzle_solve.html', {
                'puzzle': puzzle,
                'form': form,
                'start_time': timezone.now().timestamp()
            })

        # Sprawdź czy rozwiązanie jest poprawne
        user_solution = [[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                value = form.cleaned_data.get(f'cell_{row}_{col}')
                user_solution[row][col] = value if value is not None else 0

        # Funkcje pomocnicze do sprawdzania poprawności
        def check_row(board, row):
            numbers = [x for x in board[row] if x != 0]
            return len(numbers) == len(set(numbers))

        def check_column(board, col):
            numbers = [board[row][col] for row in range(9) if board[row][col] != 0]
            return len(numbers) == len(set(numbers))

        def check_box(board, start_row, start_col):
            numbers = []
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    if board[row][col] != 0:
                        numbers.append(board[row][col])
            return len(numbers) == len(set(numbers))

        # Sprawdzanie wszystkich reguł Sudoku
        is_correct = True

        # Sprawdź czy wszystkie liczby są od 1 do 9
        for row in range(9):
            for col in range(9):
                if user_solution[row][col] not in range(1, 10):
                    is_correct = False
                    break

        # Sprawdź wiersze, kolumny i kwadraty 3x3
        if is_correct:
            for i in range(9):
                if not check_row(user_solution, i) or not check_column(user_solution, i):
                    is_correct = False
                    break

            # Sprawdź kwadraty 3x3
            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    if not check_box(user_solution, row, col):
                        is_correct = False
                        break

        # Sprawdź zgodność z rozwiązaniem
        if is_correct:
            is_correct = user_solution == solution

        # Zapisz próbę rozwiązania
        completed_at = timezone.now() if is_correct else None
        attempt = SolvingAttempt.objects.create(
            puzzle=puzzle,
            current_board=json.dumps(user_solution),
            is_completed=is_correct,
            completed_at=completed_at
        )

        if is_correct:
            messages.success(request, 'Gratulacje! Rozwiązanie jest poprawne!')
            puzzle.solved = True
            solve_duration = (completed_at - attempt.started_at).total_seconds()
            puzzle.solve_time = solve_duration
            puzzle.save()
        else:
            messages.error(request, 'Niestety, rozwiązanie nie jest poprawne. Spróbuj ponownie!')

        return redirect('sudoku:puzzle_detail', pk=puzzle.pk)

    # Jeśli metoda to GET, renderuj formularz
    form = SudokuSolveForm(puzzle)
    return render(request, 'sudoku/puzzle_solve.html', {
        'puzzle': puzzle,
        'form': form,
        'start_time': timezone.now().timestamp()
    })


def puzzle_edit(request, pk):
    puzzle = get_object_or_404(SudokuPuzzle, pk=pk)

    if request.method == 'POST':
        form = SudokuPuzzleForm(request.POST, instance=puzzle)
        if form.is_valid():
            # Tworzymy planszę 9x9 wypełnioną zerami
            board = [[0 for _ in range(9)] for _ in range(9)]

            # Wypełniamy planszę danymi z formularza
            for row in range(9):
                for col in range(9):
                    field_name = f'cell_{row}_{col}'
                    value = form.cleaned_data.get(field_name)
                    board[row][col] = value if value is not None else 0

            puzzle = form.save(commit=False)
            puzzle.set_initial_board(board)
            # Aktualizujemy też solution jako kopię initial_board
            puzzle.set_solution(board)
            puzzle.save()

            messages.success(request, 'Łamigłówka została zaktualizowana pomyślnie!')
            return redirect('sudoku:puzzle_detail', pk=puzzle.pk)
        else:
            messages.error(request, 'Proszę poprawić błędy w formularzu.')
    else:
        initial_board = puzzle.get_initial_board()
        initial_data = {'difficulty': puzzle.difficulty}

        # Dodajemy początkowe wartości dla komórek planszy
        for row in range(9):
            for col in range(9):
                field_name = f'cell_{row}_{col}'
                initial_data[field_name] = initial_board[row][col] if initial_board[row][col] != 0 else None

        form = SudokuPuzzleForm(instance=puzzle, initial=initial_data)

    return render(request, 'sudoku/puzzle_form.html', {
        'form': form,
        'puzzle': puzzle,
        'action': 'edit'
    })


def puzzle_delete(request, pk):
    puzzle = get_object_or_404(SudokuPuzzle, pk=pk)

    if request.method == 'POST':
        puzzle.delete()
        messages.success(request, 'Łamigłówka została usunięta.')
        return redirect('sudoku:puzzle_list')

    return render(request, 'sudoku/puzzle_delete.html', {
        'puzzle': puzzle
    })


def puzzle_generate_solution(request, pk):
    if request.method == 'POST':
        puzzle = get_object_or_404(SudokuPuzzle, pk=pk)
        try:
            if puzzle.solve_puzzle():
                messages.success(request, 'Rozwiązanie zostało wygenerowane pomyślnie!')
                # Wyświetl informację o rozwiązaniu
                solution = puzzle.get_solution()
                initial = puzzle.get_initial_board()
                print(f"Initial board: {initial}")
                print(f"Solution: {solution}")
            else:
                messages.error(request, 'Nie można znaleźć rozwiązania dla tej łamigłówki!')
        except Exception as e:
            messages.error(request, f'Wystąpił błąd podczas generowania rozwiązania: {str(e)}')
        return redirect('sudoku:puzzle_edit', pk=pk)
    return redirect('sudoku:puzzle_list')