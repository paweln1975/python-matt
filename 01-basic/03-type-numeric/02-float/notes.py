#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-numeric/float.html

#%% Numeric Float
# Represents floating point number (vide IEEE-754)
# Could be both signed and unsigned
# Default float size is 64 bit
# Python automatically extends float when need bigger number



#%% Without Zero Notation
# .1 - notation without leading zero (0.1)
# 1. - notation without trailing zero (1.0)
# Used by numpy

x = -1.0
print(.1 == 0.1)

#%% Engineering Notation
# The exponential is a number divisible by 3
# Allows the numbers to explicitly match their corresponding SI prefixes
# 1e3 is equal to 1000.0 (kilo)
# 1e-3 is equal to 0.001 (milli)

x = 1e3
x = 1e23
print(x)

#%% Scientific notation
# 1.23e3 is equal to 1230.0
# 1.23e-3 is equal to 1.23e-3

# 1e3 = kilo
# 1e6 = mega etc

print(float(1.230_001_001e-3))


#%% Type Conversion
# float(object) - converts object to float



#%% Thousand separator
# Underscore (_) can be used as a thousand separator



#%% Decimal Separator
# 1.0 - Decimal point
# 1,0 - Decimal comma
# 0٫‎1 - Arabic decimal separator (Left to right)
# More information: [#WikipediaDecimalSeparator]_



#%% Round Number
# round(number, ndigits) - Round a number to n decimal places

PI = 3.1415
print(f'Liczba PI={PI:.2f}')

#%% Further Reading
# Wikipedia. Decimal separator. Year: 2024. Retrieved: 2024-07-01. URL:  https://en.wikipedia.org/wiki/Decimal_separator



#%% Homework
