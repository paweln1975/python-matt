"""
Name: DataFrame Mapping Substitute
Difficulty: medium
Lines: 10
Minutes: 8

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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 3)
>>> pd.set_option('display.max_rows', 10)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
                                             Definicja  ...                                 Kryteria wyjsciowe
TRL                                                     ...
1    Zaobserwowanie i opisanie podstawowych zasad d...  ...  Zweryfikowane publikacja badania lezacych u po...
2    Sformulowanie koncepcji technologicznej lub pr...  ...  Udokumentowany opis aplikacji / koncepcji, kto...
3    Przeprowadzanie eksperymentalnie i analityczni...  ...  Udokumentowane wyniki analityczne / eksperymen...
4    Przeprowadzenie weryfikacji komponentow techno...  ...  Udokumentowane wyniki testow potwierdzajace zg...
5    Przeprowadzenie weryfikacji komponentow techno...  ...  Udokumentowane wyniki testow potwierdzajace zg...
6    Dokonanie demonstracji technologii w srodowisk...  ...  Udokumentowane wyniki testow potwierdzajace zg...
7    Dokonanie demonstracji prototypu systemu w oto...  ...  Udokumentowane wyniki testow potwierdzajace zg...
8    Zakonczenie badan i demonstracja ostatecznej f...  ...  Udokumentowane wyniki testow weryfikujacych pr...
9    Weryfikacja technologii w srodowisku operacyjn...  ...            Udokumentowane wyniki operacyjne misji.
<BLANKLINE>
[9 rows x 4 columns]

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/astro-trl.xlsx'

LETTERS_PLEN = {'ą': 'a', 'ć': 'c', 'ę': 'e',
                'ł': 'l', 'ń': 'n', 'ó': 'o',
                'ś': 's', 'ż': 'z', 'ź': 'z'}

# English
# 1. Read data from `DATA` as `df: pd.DataFrame`
# 2. Select `Polish` spreadsheet
# 3. Set header and index to data from file
# 4. Mind the encoding
# 5. Substitute Polish Diacritics to English alphabet letters
# 6. Compare `df.replace(regex=True)` with `df.applymap()`
# 7. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
# 2. Wybierz arkusz `Polish`
# 3. Ustaw nagłówek i index na dane zaczytane z pliku
# 4. Zwróć uwagę na encoding
# 5. Podmień polskie znaki diakrytyczne na litery z alfabetu angielskiego
# 6. Porównaj `df.replace(regex=True)` z `df.applymap()`
# 7. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...