"""
Name: Memoization
Difficulty: medium
Lines: 5
Minutes: 13

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

"""

# %% SetUp

from timeit import timeit
import sys

sys.setrecursionlimit(5000)

# English
# 1. Create empty `dict` named `CACHE`
# 2. In the dictionary, we will store the results of calculating
#    the function for the given parameters:
#    - key: function argument
#    - value: calculation result
# 3. Modify function `factorialA(n: int)`
# 4. Before running the function, check if the result has already
#    been calculated:
#    - if so, return data from `CACHE`
#    - if not, calculate, update `CACHE` and return the value
# 5. Compare the speed of operation
# 6. Run doctests - all must succeed

# Polish
# 1. Stwórz pusty `dict` o nazwie `CACHE`
# 2. W słowniku będziemy przechowywali wyniki wyliczenia funkcji
#    dla zadanych parametrów:
#    - klucz: argument funkcji
#    - wartość: wynik obliczeń
# 3. Zmodyfikuj funkcję `factorialA(n: int)`
# 4. Przed uruchomieniem funkcji, sprawdź czy wynik został już
#    wcześniej obliczony:
#    - jeżeli tak, to zwraca dane z `CACHE`
#    - jeżeli nie, to oblicza, aktualizuje `CACHE` i zwraca wartość
# 5. Porównaj prędkość działania
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def factorialA(n: int) -> int:
    return 1 if n==0 else n*factorialA(n-1)

# Do not modify anything below
def factorialB(n: int) -> int:
    return 1 if n==0 else n*factorialB(n-1)

durationA = timeit(
    stmt='factorialA(50); factorialA(40); factorialA(45); factorialA(35)',
    globals=globals(),
    number=10000,
)

durationB = timeit(
    stmt='factorialB(50); factorialB(40); factorialB(45); factorialB(35)',
    globals=globals(),
    number=10000,
)

times_faster = durationB / durationA
print(f'factorialA time: {durationA:.4f} seconds')
print(f'factorialB time: {durationB:.4f} seconds')
print(f'Cached solution is {times_faster:.0f} times faster')
# factorialA time: 0.0654 seconds
# factorialB time: 0.0658 seconds
# Cached solution is 1 times faster