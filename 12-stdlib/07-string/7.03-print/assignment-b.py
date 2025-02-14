"""
Name: Przeliczanie temperatury
Difficulty: easy
Lines: 8
Minutes: 13

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result  # doctest: +SKIP
-------------------------------------------
| Temperature | -     20°C | ....-4....°F |
-------------------------------------------
| Temperature | -     15°C | ....+5....°F |
-------------------------------------------
| Temperature | -     10°C | ...+14....°F |
-------------------------------------------
| Temperature | -      5°C | ...+23....°F |
-------------------------------------------
| Temperature | +      0°C | ...+32....°F |
-------------------------------------------
| Temperature | +      5°C | ...+41....°F |
-------------------------------------------
| Temperature | +     10°C | ...+50....°F |
-------------------------------------------
| Temperature | +     15°C | ...+59....°F |
-------------------------------------------
| Temperature | +     20°C | ...+68....°F |
-------------------------------------------
| Temperature | +     25°C | ...+77....°F |
-------------------------------------------
| Temperature | +     30°C | ...+86....°F |
-------------------------------------------
| Temperature | +     35°C | ...+95....°F |
-------------------------------------------
| Temperature | +     40°C | ...+104...°F |
-------------------------------------------

Hints:
Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
Celsius to Fahrenheit: (°C * 1.8) + 32 = °F

"""

# %% SetUp

def celsius_to_fahrenheit(degree):
    return degree*1.8 + 32

# English
# 1. Write a program that will display a table of Celsius to Fahrenheit conversions in the range from -20 to +40 degrees Celsius (every 5 degrees).
# 2. The result must be as shown in the listing below
# 3. The sign must always be displayed
# 4. Pay attention to the text justification
# 5. Pay attention to filling the space not occupied by numbers
# 6. Run doctests - all must succeed

# Polish
# 1. Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni).
# 2. Wynik musi być taki jak na listingu poniżej
# 3. Znak ma być zawsze wyświetlany
# 4. Zwróć uwagę na wyjustowanie tekstu
# 5. Zwróć uwagę na wypełnienie miejsca niezajętego przez cyfry
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...