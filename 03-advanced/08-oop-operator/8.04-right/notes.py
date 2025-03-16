#!/usr/bin/env python3
# https://python3.info/advanced/oop-operator/right.html


# %% Operator Right
# - x + y - if method "add" on object x fails, then call "radd" on object y (y.__radd__(x))
# - x - y - if method "sub" on object x fails, then call "rsub" on object y (y.__rsub__(x))
# - x * y - if method "mul" on object x fails, then call "rmul" on object y (y.__rmul__(x))
# - x ** y - if method "pow" on object x fails, then call "rpow" on object y (y.__rpow__(x))
# - x @ y - if method "matmul" on object x fails, then call "rmatmul" on object y (y.__rmatmul__(x))
# - x / y - if method "truediv" on object x fails, then call "rtruediv" on object y (y.__rtruediv__(x))
# - x // y - if method "floordiv" on object x fails, then call "rfloordiv" on object y (y.__rfloordiv__(x))
# - x % y - if method "mod" on object x fails, then call "rmod" on object y (y.__rmod__(x))
# %%



# %% Syntax
# %%



# %% Recap
# %%



# %% Left Operation
# %%



# %% Right Operation
# %%



class Vector:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def __add__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        return Vector(x=self.x+other.x, y=self.y+other.y)

    def __radd__(self, other):
        return self.__add__(other)


v1 = Vector(1, 2)
v2 = Vector(2, 2)
print(v1+v2)

v1 = Vector(1, 2)
v2 = (2, 2)
print(v1+v2)

v1 = (2, 2)
v2 = Vector(1, 2)
print(v1+v2)