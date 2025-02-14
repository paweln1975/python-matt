
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 11), \
'Python 3.11+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is dict, \
'Variable `result` has invalid type, should be dict'

>>> assert result['hostname'] == '127.0.0.1'
>>> assert result['port'] == 5432
>>> assert result['username'] == 'mwatney'
>>> assert result['password'] == 'Ares3'
>>> assert result['database'] == 'nasa'

>>> from pathlib import Path
>>> Path(FILE).unlink(missing_ok=True)
"""
# endregion

# region Show Imports
import tomllib
# endregion

# region Show Types
result: dict[str, str|int]
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
""")

# English
# 1. Read configuration from `FILE`
# 2. Define `result: dict` with database config
# 3. Use `tomllib.load()`
# 4. Run doctests - all must succeed

# Polish
# 1. Wczytaj konfigurację z `FILE`
# 2. Zdefiniuj `result: dict` z konfiguracją bazy danych
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

result = config['database']
