#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/operator-new/arithmetic.html

#%% Operator Arithmetic
# Left Operators
# Right Operators
# In-Place Operators



#%% Numeric
# -obj -> obj.__neg__()
# +obj -> obj.__pos__()
# Example: -1 or +1



#%% Left Operators
# obj + other -> obj.__add__(other)
# obj - other -> obj.__sub__(other)
# obj * other -> obj.__mul__(other)
# obj ** other -> obj.__pow__(other)
# obj @ other -> obj.__matmul__(other)
# obj / other -> obj.__truediv__(other)
# obj // other -> obj.__floordiv__(other)
# obj % other -> obj.__mod__(other)



#%% In-Place Operators
# obj += other -> obj.__iadd__(other)
# obj -= other -> obj.__isub__(other)
# obj *= other -> obj.__imul__(other)
# obj **= other -> obj.__ipow__(other)
# obj @= other -> obj.__imatmul__(other)
# obj /= other -> obj.__itruediv__(other)
# obj //= other -> obj.__ifloordiv__(other)
# obj %= other -> obj.__imod__(other)



#%% Right Operators
# obj + other - when obj.__add__(other) fail -> other.__radd__(obj)
# obj - other - when obj.__sub__(other) fail -> other.__rsub__(obj)
# obj * other - when obj.__mul__(other) fail -> other.__rmul__(obj)
# obj ** other - when obj.__pow__(other) fail -> other.__rpow__(obj)
# obj @ other - when obj.__matmul__(other) fail -> other.__rmatmul__(obj)
# obj / other - when obj.__truediv__(other) fail -> other.__rtruediv__(obj)
# obj // other - when obj.__floordiv__(other) fail -> other.__rfloordiv__(obj)
# obj % other - when obj.__mod__(other) fail -> other.__rmod__(obj)