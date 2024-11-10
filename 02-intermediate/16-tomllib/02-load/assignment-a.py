"""
* Assignment: TOML Load Version
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Read configuration from `FILE`
    2. Define `result: str` with version read from config
    3. Use `tomllib.load()`
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj konfigurację z `FILE`
    2. Zdefiniuj `result: str` z werją wczytaną z konfiguracji
    3. Użyj `tomllib.load()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * open(filename, mode='rb')
    * import tomllib
    * tomllib.load()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from pathlib import Path

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> pprint(result)
    '1.0.0'

    >>> Path(FILE).unlink(missing_ok=True)
"""
import tomllib


FILE = '_temporary.toml'

with open(FILE, mode='wb') as file:
    file.write(b"""
project = 'My App'
version = '1.0.0'
""")


# Read configuration from `FILE`
# Define `result: str` with version read from config
# type: str
result = ...

