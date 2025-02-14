
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass
>>> assert isclass(Encoder), \
'Encoder must be a class'
>>> assert issubclass(Encoder, json.JSONEncoder), \
'Encoder must inherit from `json.JSONEncoder`'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is str, \
'Variable `result` has invalid type, should be str'

>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{"mission": "Ares 3",
 "launch_date": "2035-06-29T00:00:00",
 "destination": "Mars",
 "destination_landing": "2035-11-07T00:00:00",
 "destination_location": "Acidalia Planitia",
 "crew": [{"name": "Melissa Lewis", "birthdate": "1995-07-15"},
          {"name": "Rick Martinez", "birthdate": "1996-01-21"},
          {"name": "Alex Vogel", "birthdate": "1994-11-15"},
          {"name": "Chris Beck", "birthdate": "1999-08-02"},
          {"name": "Beth Johanssen", "birthdate": "2006-05-09"},
          {"name": "Mark Watney", "birthdate": "1994-10-12"}]}
"""
# endregion

# region Show Imports
import json
from datetime import date, datetime
# endregion

# region Show Types
result: str
# endregion

DATA = {
    'mission': 'Ares 3',
    'launch_date': datetime(2035, 6, 29),
    'destination': 'Mars',
    'destination_landing': datetime(2035, 11, 7),
    'destination_location': 'Acidalia Planitia',
    'crew': [
        {'name': 'Melissa Lewis', 'birthdate': date(1995, 7, 15)},
        {'name': 'Rick Martinez', 'birthdate': date(1996, 1, 21)},
        {'name': 'Alex Vogel', 'birthdate': date(1994, 11, 15)},
        {'name': 'Chris Beck', 'birthdate': date(1999, 8, 2)},
        {'name': 'Beth Johanssen', 'birthdate': date(2006, 5, 9)},
        {'name': 'Mark Watney', 'birthdate': date(1994, 10, 12)}]}

# English
# 1. Define `result: str` with JSON encoded `DATA`
# 2. Use encoder class
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: str` z zakodowanym `DATA` w JSON
# 2. Użyj enkodera klasowego
# 3. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `json.dumps(default=...)`
# - `isinstance(obj, date|datetime)`
# - `date.toisoformat()`
# - `datetime.toisoformat()`
# endregion

# %% Your code
class Encoder(json.JSONEncoder):
    def default(self, obj):
        return obj.isoformat()

result = json.dumps(DATA, cls=Encoder)
