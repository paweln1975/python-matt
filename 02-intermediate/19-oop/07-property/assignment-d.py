"""
* Assignment: OOP Property NumericValues
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Modify class `Iris`
    2. Implement methods:
        a. `Iris.sum()` - returning sum of numeric attributes
        b. `Iris.len()` - returning number of numeric attributes
        c. `Iris.mean()` - returning mean of numeric attributes
    3. Use property `Iris.numeric_values`
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `Iris`
    2. Zaimplementuj metody:
        a. `Iris.sum()` - zwracającą sumę numerycznych atrybutów
        b. `Iris.len()` - zwracającą liczbę numerycznych atrybutów
        c. `Iris.mean()` - zwracającą średnią numerycznych atrybutów
    3. Użyj property `Iris.numeric_values`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `sum()`
    * `len()`
    * `sum() / len()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert hasattr(Iris, 'mean')
    >>> assert hasattr(Iris, 'sum')
    >>> assert hasattr(Iris, 'len')

    >>> assert isfunction(Iris.mean)
    >>> assert isfunction(Iris.sum)
    >>> assert isfunction(Iris.len)

    >>> result = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> result.len()
    4
    >>> result.sum()
    10.2
    >>> result.mean()
    2.55
"""


class Iris:
    def __init__(self, sl, sw, pl, pw, species):
        self.sepal_length = sl
        self.sepal_width = sw
        self.petal_length = pl
        self.petal_width = pw
        self.species = species

    @property
    def numeric_values(self):
        return tuple(x for x in vars(self).values()
                     if type(x) is float)

    # return sum of numeric attributes
    # type: Callable[[], float]
    def sum(self):
        ...

    # return number of numeric attributes
    # type: Callable[[], int]
    def len(self):
        ...

    # return mean of numeric attributes
    # type: Callable[[], float]
    def mean(self):
        ...

