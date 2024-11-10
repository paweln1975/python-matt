"""
* Assignment: Function Scope Locals
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Modify function `run` with local variables `a=1` and `b=2`
    2. Return `dict` with variable names and their values,
       example: {'a': 1, 'b': 2}
    3. Use `locals()` function
    6. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `run` z lokalnymi zmiennymi `a=1` i `b=2`
    2. Zwróć `dict` z nazwami zmiennych i ich wartościami,
       przykład: {'a': 1, 'b': 2}
    3. Użyj funkcji `locals()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert run is not Ellipsis, \
    'Write solution inside `run` function'
    >>> assert isfunction(run), \
    'Object `run` must be a function'

    >>> run()
    {'a': 1, 'b': 2}
"""

# Return `dict` with variable names and its values, example: {'a': 1, 'b': 2}
# Use `locals()` function
# type: Callable[[], dict[str,int]]
def run():
    a = 1
    b = 2
    return locals()


