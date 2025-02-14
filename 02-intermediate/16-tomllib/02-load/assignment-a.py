
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 11), \
'Python 3.11+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is str, \
'Variable `result` has invalid type, should be str'

>>> from pprint import pprint
>>> pprint(result)
'1.0.0'

>>> from pathlib import Path
>>> Path(FILE).unlink(missing_ok=True)
"""
# endregion

# region Show Imports
import tomllib
# endregion

# region Show Types
result: str
# endregion

FILE = '_temporary.toml'

with open(FILE, mode='wb') as file:
    file.write(b"""
project = 'My App'
version = '1.0.0'
""")

# English
# 1. Read configuration from `FILE`
# 2. Define `result: str` with version read from config
# 3. Use `tomllib.load()`
# 4. Run doctests - all must succeed

# Polish
# 1. Wczytaj konfigurację z `FILE`
# 2. Zdefiniuj `result: str` z wersją wczytaną z konfiguracji
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

result = config['version']
