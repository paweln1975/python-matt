"""
* Assignment: Functional Scope Global
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define in global scope `SELECT: set[str]` with values:
       `'setosa', 'versicolor'`
    2. Define function `sumif(values, species)`
    3. Function sums `values`, only when `species` is in `SELECT`
    4. When `species` is not in `select` return `0` (zero)
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj w przestrzeni globalnej `SELECT: set[str]` z wartościami:
       `'setosa', 'versicolor'`
    2. Zdefiniuj funkcję `sumif(values, species)`
    3. Funkcja sumuje `values`, tylko gdy `species` jest w `SELECT`
    4. Gdy `species` nie występuje w `select` zwróć `0` (zero)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction, signature

    >>> assert type(SELECT) is set, \
    'Define in global scope `SELECT: set[str]`'

    >>> assert 'setosa' in SELECT, \
    'Value setosa must be in SELECT'

    >>> assert 'versicolor' in SELECT, \
    'Value versicolor must be in SELECT'

    >>> assert isfunction(sumif), \
    'Define function `sumif(values, species)`'

    >>> signature(sumif)
    <Signature (values, species)>

    >>> sum(sumif(X,y) for *X, y in DATA[1:])
    49.1
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


# Sums values, when species is in SELECT, else return 0 (zero)
# type: Callable[[list[float], str], float]
def sumif():
    ...

