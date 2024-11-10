"""
* Assignment: Functional Callable Define
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define function `run()` without any parameter
    2. Function `run()` must return `myfunc: Callable`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `run()` bez żadnego parametru
    2. Funkcja `run()` ma zwracać `myfunc: Callable`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(run)
    >>> assert isfunction(myfunc)
    >>> assert isfunction(run())

    >>> myfunc()
    'hello from myfunc'

    >>> run()()
    'hello from myfunc'
"""


def myfunc():
    return 'hello from myfunc'


# Without any parameter
# Returns myfunc function
# type: Callable[[Callable], Callable]
def run():
    ...


