"""
* Assignment: Function Usecase Enumerate
* Type: class assignment
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Define function `myenumerate`:
        a. takes `data: list`
        b. returns tuple list with consecutive number and value from `data`
    2. Example:
        a. input: ['red', 'green', 'blue']
        b. output: [(0, 'red'), (1, 'green'), (2, 'blue')]
    3. Do not use built-in `enumerate()` function
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `myenumerate`:
       a. przyjmuje `data: list`
       b. zwraca listę tupli z kolejnym numerem i wartością z `data`
    2. Przykład:
        a. input: ['red', 'green', 'blue']
        b. output: [(0, 'red'), (1, 'green'), (2, 'blue')]
    3. Nie używaj wbudowanej funkcji `enumerate`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert myenumerate is not Ellipsis, \
    'Write solution inside `myenumerate` function'
    >>> assert isfunction(myenumerate), \
    'Object `myenumerate` must be a function'

    >>> myenumerate(['red', 'green', 'blue'])
    [(0, 'red'), (1, 'green'), (2, 'blue')]
"""

# Define function `myenumerate`:
# - takes `data: list`
# - returns number of elements in `data`
# Do not use built-in `len()` function
# type: Callable[[list], int]
def myenumerate(iterable):
    count = 0
    result = []
    for v in iterable:
        result.append((count, v))
        count += 1
    return result



