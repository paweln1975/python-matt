#!/usr/bin/env python3

# Reference:
# https://python3.info/pandas/series/arithmetic.html

#%% Series Arithmetic



#%% Vectorized Operations
# s + 2,  s.add(2), s.__add__(2)
# s - 2,  s.sub(2), s.subtract(2), s.__sub__(2)
# s * 2,  s.mul(2), s.multiply(2), s.__mul__(2)
# s ** 2, s.pow(2), s.__pow__(2)
# s ** (1/2), s.pow(1/2), s.__sub__(1/2)
# s / 2,  s.div(2), s.divide(), s.__div__(2)
# s // 2, s.truediv(2), s.__truediv__(2)
# s % 2,  s.mod(2), s.__mod__(2)
# divmod(s, 2), s.divmod(2), s.__divmod__(2), (s//2, s%2)



#%% Broadcasting
# Uses inner join
# fill_value: If data in both corresponding Series locations is