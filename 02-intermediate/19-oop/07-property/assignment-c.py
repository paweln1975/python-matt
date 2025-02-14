
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

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
# endregion

# region Show Types
Iris: type
numeric_values: property
# endregion

# English
# 1. Define property `numeric_values` in class `Iris`
# 2. Accessing `numeric_values` should return a tuple
#    with all numeric attribute values
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj property `numeric_values` w klasie `Iris`
# 2. Dostęp do `numeric_values` powinien zwrócić tuplę
#    z wszystkimi wartościami atrybutów numerycznych
# 3. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `var(self)`
# - `dict.values()`
# - `instanceof()`
# - `type()`
# - `@property`
# endregion

# %% Your code
class Iris:
    def __init__(self, sl, sw, pl, pw, species):
        self.sepal_length = sl
        self.sepal_width = sw
        self.petal_length = pl
        self.petal_width = pw
        self.species = species

    @property
    def numeric_values(self):
        return self.sepal_length, self.sepal_width, self.petal_length, self.petal_width
