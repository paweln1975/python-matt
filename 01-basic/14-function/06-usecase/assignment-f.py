"""
* Assignment: Function Usecase Zip
* Type: class assignment
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Define function `myzip`:
        a. takes two parameters `a: list`, `b: list`
        b. pairs `a` elements with `b` elements in form of `list[tuple]`
        c. first from `a` is paired with first from `b`, etc.
        d. collect number of pairs equal to the count of shortest list
    2. Example:
        a. input: ['Mark', 'Melissa'] and ['Watney', 'Lewis']
        b. output: [('Mark', 'Watney'), ('Melissa', 'Lewis')]
    3. Do not use built-in `zip()` function
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `myzip`:
       a. przyjmuje `data: list`
       b. paruje elementy `a` z elementami z `b` w formie `list[tuple]`
       c. pierwszy z `a` ma być sparowany z pierwszym z `b`, itd.
       d. zbierz tyle par ile bło wartości w najkrótszej liście
    2. Przykład:
        a. input: ['Mark', 'Melissa'] i ['Watney', 'Lewis']
        b. output: [('Mark', 'Watney'), ('Melissa', 'Lewis')]
    3. Nie używaj wbudowanej funkcji `zip`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert myzip is not Ellipsis, \
    'Write solution inside `myzip` function'
    >>> assert isfunction(myzip), \
    'Object `myzip` must be a function'

    >>> firstnames = ['Mark', 'Melissa', 'Rick']
    >>> lastnames = ['Watney', 'Lewis', 'Martinez']
    >>> myzip(firstnames, lastnames)
    [('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Rick', 'Martinez')]

    >>> firstnames = ['Mark', 'Melissa', 'Rick']
    >>> lastnames = ['Watney', 'Lewis']
    >>> myzip(firstnames, lastnames)
    [('Mark', 'Watney'), ('Melissa', 'Lewis')]
"""

# Define function `myzip`:
# - takes two parameters `a: list`, `b: list`
# - pairs `a` elements with `b` elements in form of `list[tuple]`
# - first from `a` is paired with first from `b`, etc.
# - collect number of pairs equal to the count of shortest list
# Do not use built-in `zip()` function
# type: Callable[[list], int]
def mylen(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count
def myzip(iterable_first, iterable_second):
    count_first = mylen(iterable_first)
    count_second = mylen(iterable_second)
    count = min(count_first, count_second)

    result = []
    i = 0
    while i < count:
        result.append((iterable_first[i], iterable_second[i]))
        i += 1
    return result


