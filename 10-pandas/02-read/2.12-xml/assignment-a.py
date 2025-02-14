"""
Name: Pandas Read XML
Difficulty: medium
Lines: 1
Minutes: 3

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
>>> pd.set_option('display.width', 250)
>>> pd.set_option('display.max_columns', 20)
>>> pd.set_option('display.max_rows', 30)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` has invalid type, should be `pd.DataFrame`'

>>> result
           common               botanical  zone         light     price  availability
0       bloodroot  sanguinaria canadensis     4  mostly shady  2.40 USD         31599
1       columbine    aquilegia canadensis     3  mostly shady  9.40 USD         30699
2  marsh marigold        caltha palustris     4  mostly sunny  6.80 USD         51799
3         cowslip        caltha palustris     4  mostly shady  9.90 USD         30699

Hints:
`pip install --upgrade lxml`

"""

# %% SetUp

from io import StringIO
import pandas as pd

result: pd.DataFrame

DATA = """
    <catalog>
        <plant>
            <common>bloodroot</common>
            <botanical>sanguinaria canadensis</botanical>
            <zone>4</zone>
            <light>mostly shady</light>
            <price>2.40 USD</price>
            <availability>031599</availability>
        </plant>
        <plant>
            <common>columbine</common>
            <botanical>aquilegia canadensis</botanical>
            <zone>3</zone>
            <light>mostly shady</light>
            <price>9.40 USD</price>
            <availability>030699</availability>
        </plant>
        <plant>
            <common>marsh marigold</common>
            <botanical>caltha palustris</botanical>
            <zone>4</zone>
            <light>mostly sunny</light>
            <price>6.80 USD</price>
            <availability>051799</availability>
        </plant>
        <plant>
            <common>cowslip</common>
            <botanical>caltha palustris</botanical>
            <zone>4</zone>
            <light>mostly shady</light>
            <price>9.90 USD</price>
            <availability>030699</availability>
        </plant>
    </catalog>
"""

# English
# 1. Read data from `DATA` as `pd.DataFrame`
# 2. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `pd.DataFrame`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...