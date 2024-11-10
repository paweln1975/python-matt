"""
* Assignment: Type Float Percent
* Type: homework
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Pressure in International Standard Atmosphere (ISA)
       at sea level is: 1 ata = 1013.25 hPa
    2. Calculate `pO2` - partial pressure of oxygen at sea level in hPa
    3. To calculate partial pressure use ratio
          100% --- 1013.25 hPa
       20.946% --- ? hPa
    4. Run doctests - all must succeed

Polish:
    1. Ciśnienie w Międzynarodowej Standardowej Atmosfera (ISA)
       na poziomie morza wynosi: 1 ata = 1013.25 hPa
    2. Oblicz `pO2` - ciśnienie parcjalne tlenu na poziomie morza w hPa
    3. Aby policzyć ciśnienie parcjalne skorzystaj z proporcji
          100% --- 1013.25 hPa
       20.946% --- ? hPa
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 ata = 1013.25 hPa
    * ISA - International Standard Atmosphere
    * Atmosphere gas composition:
        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert ata is not Ellipsis, \
    'Assign your result to variable `ata`'
    >>> assert type(ata) is float, \
    'Variable `ata` has invalid type, should be float'

    >>> assert pO2 is not Ellipsis, \
    'Assign your result to variable `pO2`'
    >>> assert type(pO2) is float, \
    'Variable `pO2` has invalid type, should be float'

    >>> ata
    101325.0
    >>> round(pO2, 1)
    212.2
"""

PERCENT = 100
N2 = 78.084 / PERCENT
O2 = 20.946 / PERCENT
Ar = 0.9340 / PERCENT
CO2 = 0.0407 / PERCENT
Others = 0.001 / PERCENT

Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa

# Pressure in ISA at sea level is: 1 ata = 1013.25 hPa
# type: float
ata = 1013.25 * hPa

# 20.946% of pressure at sea level in hPa
# type: float
pO2 = ((20.946/PERCENT)*ata) / hPa

