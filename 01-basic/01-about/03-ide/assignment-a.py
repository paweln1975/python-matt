"""
* Assignment: About IDE Usage
* Complexity: easy
* Lines of code: 0 lines
* Time: 8 min

English:
    1. How to do in your IDE:
        a. Run...
        b. Run in console
        c. Debug...
        d. Python Console
        e. Terminal
        f. Full Screen
        g. Distraction Free Mode
        h. Reformat Code
        i. Scope
    2. What are the keyboard shortcuts for each option?
    3. What is the difference between `Run...` and `Debug...`?
    4. What is the difference between `Python Console` and `Terminal`
    5. What is the difference between `Distraction Free Mode` and `Full Screen`
    6. Set Scope to hide Virtualenv directory
    7. Run doctests - all must succeed

Polish:
    1. Jak zrobić w Twoim IDE:
        a. Run...
        b. Run in console
        c. Debug...
        d. Python Console
        e. Terminal
        f. Full Screen
        g. Distraction Free Mode
        h. Reformat Code
        i. Scope
    2. Jakie są skróty klawiszowe do poszczególnych opcji?
    3. Czym się różni `Run...` od `Debug...`?
    4. Czym się różni `Python Console` od `Terminal`
    5. Czym się różni `Distraction Free Mode` od `Full Screen`
    6. Ustaw Scope tak, aby ukryć katalog z Virtualenv
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> sys.tracebacklimit = 0
    >>> assert sys.version_info > (3, 11, 0), \
    'Python 3.12+ is required'
"""


import sys

print('Your Python version:', sys.version[:6])


