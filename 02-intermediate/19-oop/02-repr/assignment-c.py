"""
* Assignment: Operator String Repr
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Modify `Iris` to overwrite `__repr__()` method
    2. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `Iris` aby nadpisać metodę `__repr__()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Iris)
    >>> iris = Iris(DATA)

    >>> assert hasattr(Iris, '__repr__')
    >>> assert ismethod(iris.__repr__)
    >>> repr(iris)
    "Iris(values=[4.7, 3.2, 1.3, 0.2], species='setosa')"
"""

DATA = (4.7, 3.2, 1.3, 0.2, 'setosa')

# repr() -> Iris(values=[4.7, 3.2, 1.3, 0.2], species='setosa')
class Iris:
    values: list
    species: str

    def __init__(self, data):
        self.values = list(data[:-1])
        self.species = str(data[-1])


