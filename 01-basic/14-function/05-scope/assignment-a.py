"""
* Assignment: Function Scope Locals
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Modify function `run`
    2. Calling function should print value of local variables `a` and `b`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `run`
    2. Wywołanie funkcji powinno wypisać wartość zmiennych lokalnych `a` i `b`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert run is not Ellipsis, \
    'Write solution inside `run` function'
    >>> assert isfunction(run), \
    'Object `run` must be a function'

    >>> run()
    a=1, b=2
"""

# Calling function should print value of local variables `a` and `b`
# type: Callable[[], None]
def run():
    a = 1
    b = 2
    print(f'a={a}, b={b}')

# more advanced

def run2():
    a = 1
    b = 2
    print(f'{a=}, {b=}')
