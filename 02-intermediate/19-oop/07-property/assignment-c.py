"""
* Assignment: OOP Property NumericValues
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Define property `numeric_values` in class `Iris`
    2. Accessing `numeric_values` should return a tuple
       with all numeric attribute values
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj property `numeric_values` w klasie `Iris`
    2. Dostęp do `numeric_values` powinien zwrócić tuplę
       z wszystkimi wartościami atrybutów numerycznych
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `var(self)`
    * `dict.values()`
    * `instanceof()`
    * `type()`
    * `@property`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert hasattr(Iris, '__init__')
    >>> assert hasattr(Iris, 'numeric_values')
    >>> assert not isfunction(Iris.numeric_values)

    >>> assert Iris.numeric_values.__class__ is property
    >>> assert Iris.numeric_values.fdel is None
    >>> assert Iris.numeric_values.fset is None
    >>> assert Iris.numeric_values.fget is not None

    >>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> setosa.numeric_values
    (5.1, 3.5, 1.4, 0.2)
"""


class Iris:
    def __init__(self, sl, sw, pl, pw, species):
        self.sepal_length = sl
        self.sepal_width = sw
        self.petal_length = pl
        self.petal_width = pw
        self.species = species

    # Create property `numeric_values`,
    # which returns a tuple of values of all `float` type attributes
    # type: Callable[[], tuple[float]]
    def numeric_values(self):
        ...


