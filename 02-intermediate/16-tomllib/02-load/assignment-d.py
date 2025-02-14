
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 11), \
'Python 3.11+ required'

>>> from pprint import pprint
>>> from pathlib import Path

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'

>>> result = sorted(result)
>>> pprint(result)
['avogel@nasa.gov',
 'bjohanssen@nasa.gov',
 'cbeck@nasa.gov',
 'mlewis@nasa.gov',
 'mwatney@nasa.gov',
 'rmartinez@nasa.gov']

>>> Path(FILE).unlink(missing_ok=True)
"""
# endregion

# region Show Imports
import tomllib
# endregion

# region Show Types
result: list[str]
# endregion

FILE = '_temporary.toml'

with open(FILE, mode='wb') as file:
    file.write(b"""
project = 'My App'
version = '1.0.0'

[database]
hostname = '127.0.0.1'
port = 5432
username = 'mwatney'
password = 'Ares3'
database = 'nasa'

[metadata]
release_date = 2020-01-01T00:00:00Z
authors = [
    { name = 'Mark Watney', email = 'mwatney@nasa.gov' },
    { name = 'Melisa Lewis', email = 'mlewis@nasa.gov' },
    { name = 'Rick Martinez', email = 'rmartinez@nasa.gov' },
    { name = 'Alex Vogel', email = 'avogel@nasa.gov' },
    { name = 'Beth Johanssen', email = 'bjohanssen@nasa.gov' },
    { name = 'Chris Beck', email = 'cbeck@nasa.gov' },
]
""")

# English
# 1. Read configuration from `FILE`
# 2. Define `result: list[str]` with author emails
# 3. Use `tomllib.load()`
# 4. Run doctests - all must succeed

# Polish
# 1. Wczytaj konfigurację z `FILE`
# 2. Zdefiniuj `result: list[str]` z adresami email autorów
# 3. Użyj `tomllib.load()`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `open(filename, mode='rb')`
# - `import tomllib`
# - `tomllib.load()`
# endregion

# %% Your code
with open(FILE, mode='rb') as file:
    config = tomllib.load(file)

authors = config['metadata']['authors']
result = [author['email'] for author in authors]
