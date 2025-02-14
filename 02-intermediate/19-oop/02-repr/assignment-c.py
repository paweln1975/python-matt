
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass, ismethod
>>> assert isclass(Iris)
>>> iris = Iris(DATA)

>>> assert hasattr(Iris, '__repr__')
>>> assert ismethod(iris.__repr__)

>>> repr(iris)
"Iris(values=[4.7, 3.2, 1.3, 0.2], species='setosa')"
"""
# endregion

# region Show Types
from typing import Callable
Iris: type
__repr__: Callable[[object], str]
# endregion

DATA = (4.7, 3.2, 1.3, 0.2, 'setosa')

# English
# 1. Modify `Iris` to overwrite `__repr__()` method
# 2. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Iris` aby nadpisać metodę `__repr__()`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
class Iris:
    values: list
    species: str

    def __init__(self, data):
        self.values = list(data[:-1])
        self.species = str(data[-1])

    def __repr__(self):
        return f"Iris(values={self.values}, species='{self.species}')"
