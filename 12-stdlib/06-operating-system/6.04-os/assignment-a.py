"""
Name: Recursive folders walking
Difficulty: easy
Lines: 30
Minutes: 21

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

Hints:
Gdyby był problem ze znalezieniem pliku, a ścieżka jest poprawna to zastosuj `shell=True`
`os.walk()`
`subprocess.run()`

Why:
Browsing directories and search algorithms
Sanitizing parameters
Logging events in the program
Executing commands in the system
Capturing command output
Error codes
Navigating to directories
Relative and absolute paths
Joining paths

"""

# %% SetUp

result: float

# English
# 1. Check if directory "Python" already exists on your Desktop
# 2. If it doesn't exist then create it using `os.mkdir()`
# 3. Using `subprocess.call()` create file `README.rst` in this directory and add text "Ehlo World" to it
# 4. Recursively walk through all directories on your Desktop
# 5. Find all `README` files (with any extension)
# 6. Display their contents using command:
#    - `cat` (macOS, Linux)
#    - `type` (Windows)
# 7. Construct path to above `README` file using `os.path.join()`
# 8. Path should be relative to the file that is currently being run
# 9. If after walking through the entire Desktop recursively the script doesn't find file `LICENSE.rst`, then it should throw information `logging.critical()` and exit with error code `1`.
# 10. Run doctests - all must succeed

# Polish
# 1. Sprawdź czy katalog "Python" już istnieje na pulpicie w Twoim systemie
# 2. Jeżeli nie istnieje to za pomocą `os.mkdir()` stwórz go w tym miejscu
# 3. Za pomocą `subprocess.call()` w tym katalogu stwórz plik `README.rst` i dodaj do niego tekst "Ehlo World"
# 4. Przeszukaj rekurencyjnie wszystkie katalogi na pulpicie
# 5. Znajdź wszystkie pliki `README` (z dowolnym rozszerzeniem)
# 6. Wyświetl ich zawartość za pomocą polecenia:
#    - `cat` (macOS, Linux)
#    - `type` (Windows)
# 7. Ścieżkę do powyższego pliku `README` skonstruuj za pomocą `os.path.join()`
# 8. Ścieżka ma być względna w stosunku do pliku, który aktualnie jest uruchamiany
# 9. Jeżeli po przeszukaniu całego Pulpitu rekurencyjnie skrypt nie znajdzie pliku `LICENSE.rst`, to ma rzucić informację `logging.critical()` i wyjść z kodem błędu `1`.
# 10. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...