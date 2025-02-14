"""
Name: Accessor Descriptor Simple
Difficulty: easy
Lines: 9
Minutes: 5

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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> class Temperature:
...     kelvin = Kelvin()

>>> t = Temperature()
>>> t.kelvin = 1
>>> t.kelvin
1
>>> t.kelvin = -1
Traceback (most recent call last):
ValueError: Negative temperature

"""

# %% SetUp

# English
# 1. Define descriptor class `Kelvin`
# 2. Temperature must always be positive
# 3. Use descriptors to check boundaries at each value modification
# 4. All tests must pass
# 5. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę deskryptor `Kelvin`
# 2. Temperatura musi być zawsze być dodatnia
# 3. Użyj deskryptorów do sprawdzania zakresów przy każdej modyfikacji
# 4. Wszystkie testy muszą przejść
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
