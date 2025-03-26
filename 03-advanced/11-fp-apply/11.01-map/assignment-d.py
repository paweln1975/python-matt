"""
Name: Functional Map Logs
Difficulty: medium
Lines: 7
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

>>> from pprint import pprint

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is map, \
'Variable `result` has invalid type, must be a map'

>>> result = list(result)
>>> assert all(type(row) is dict for row in result), \
'All elements in result must be dict'

>>> pprint(result)
[{'datetime': datetime.datetime(1969, 7, 14, 21, 0),
  'level': 'INFO',
  'message': 'Terminal countdown started'},
 {'datetime': datetime.datetime(1969, 7, 16, 13, 31, 53),
  'level': 'WARNING',
  'message': 'S-IC engine ignition (#5)'},
 {'datetime': datetime.datetime(1969, 7, 16, 13, 33, 23),
  'level': 'DEBUG',
  'message': 'Maximum dynamic pressure (735.17 lb/ft^2)'},
 {'datetime': datetime.datetime(1969, 7, 16, 13, 34, 44),
  'level': 'WARNING',
  'message': 'S-II ignition'},
 {'datetime': datetime.datetime(1969, 7, 16, 13, 35, 17),
  'level': 'DEBUG',
  'message': 'Launch escape tower jettisoned'},
 {'datetime': datetime.datetime(1969, 7, 16, 13, 39, 40),
  'level': 'DEBUG',
  'message': 'S-II center engine cutoff'},
 {'datetime': datetime.datetime(1969, 7, 16, 16, 22, 13),
  'level': 'INFO',
  'message': 'Translunar injection'},
 {'datetime': datetime.datetime(1969, 7, 16, 16, 56, 3),
  'level': 'INFO',
  'message': 'CSM docked with LM/S-IVB'},
 {'datetime': datetime.datetime(1969, 7, 16, 17, 21, 50),
  'level': 'INFO',
  'message': 'Lunar orbit insertion ignition'},
 {'datetime': datetime.datetime(1969, 7, 16, 21, 43, 36),
  'level': 'INFO',
  'message': 'Lunar orbit circularization ignition'},
 {'datetime': datetime.datetime(1969, 7, 20, 17, 44),
  'level': 'INFO',
  'message': 'CSM/LM undocked'},
 {'datetime': datetime.datetime(1969, 7, 20, 20, 5, 5),
  'level': 'WARNING',
  'message': 'LM powered descent engine ignition'},
 {'datetime': datetime.datetime(1969, 7, 20, 20, 10, 22),
  'level': 'ERROR',
  'message': 'LM 1202 alarm'},
 {'datetime': datetime.datetime(1969, 7, 20, 20, 14, 18),
  'level': 'ERROR',
  'message': 'LM 1201 alarm'},
 {'datetime': datetime.datetime(1969, 7, 20, 20, 17, 39),
  'level': 'WARNING',
  'message': 'LM lunar landing'},
 {'datetime': datetime.datetime(1969, 7, 21, 2, 39, 33),
  'level': 'DEBUG',
  'message': 'EVA started (hatch open)'},
 {'datetime': datetime.datetime(1969, 7, 21, 2, 56, 15),
  'level': 'WARNING',
  'message': '1st step taken lunar surface (CDR)'},
 {'datetime': datetime.datetime(1969, 7, 21, 2, 56, 15),
  'level': 'WARNING',
  'message': 'Neil Armstrong first words on the Moon'},
 {'datetime': datetime.datetime(1969, 7, 21, 3, 5, 58),
  'level': 'DEBUG',
  'message': 'Contingency sample collection started (CDR)'},
 {'datetime': datetime.datetime(1969, 7, 21, 3, 15, 16),
  'level': 'INFO',
  'message': 'LMP on lunar surface'},
 {'datetime': datetime.datetime(1969, 7, 21, 5, 11, 13),
  'level': 'DEBUG',
  'message': 'EVA ended (hatch closed)'},
 {'datetime': datetime.datetime(1969, 7, 21, 17, 54),
  'level': 'WARNING',
  'message': 'LM lunar liftoff ignition (LM APS)'},
 {'datetime': datetime.datetime(1969, 7, 21, 21, 35),
  'level': 'INFO',
  'message': 'CSM/LM docked'},
 {'datetime': datetime.datetime(1969, 7, 22, 4, 55, 42),
  'level': 'WARNING',
  'message': 'Transearth injection ignition (SPS)'},
 {'datetime': datetime.datetime(1969, 7, 24, 16, 21, 12),
  'level': 'INFO',
  'message': 'CM/SM separation'},
 {'datetime': datetime.datetime(1969, 7, 24, 16, 35, 5),
  'level': 'WARNING',
  'message': 'Entry'},
 {'datetime': datetime.datetime(1969, 7, 24, 16, 50, 35),
  'level': 'WARNING',
  'message': 'Splashdown (went to apex-down)'},
 {'datetime': datetime.datetime(1969, 7, 24, 17, 29),
  'level': 'INFO',
  'message': 'Crew egress'}]

Hints:
Note, that last time has no seconds
This is not bug, time without seconds is in NASA history records [1]

"""

# %% SetUp

from datetime import date, datetime, time

result: map

DATA = """1969-07-14, 21:00:00, INFO, Terminal countdown started
1969-07-16, 13:31:53, WARNING, S-IC engine ignition (#5)
1969-07-16, 13:33:23, DEBUG, Maximum dynamic pressure (735.17 lb/ft^2)
1969-07-16, 13:34:44, WARNING, S-II ignition
1969-07-16, 13:35:17, DEBUG, Launch escape tower jettisoned
1969-07-16, 13:39:40, DEBUG, S-II center engine cutoff
1969-07-16, 16:22:13, INFO, Translunar injection
1969-07-16, 16:56:03, INFO, CSM docked with LM/S-IVB
1969-07-16, 17:21:50, INFO, Lunar orbit insertion ignition
1969-07-16, 21:43:36, INFO, Lunar orbit circularization ignition
1969-07-20, 17:44:00, INFO, CSM/LM undocked
1969-07-20, 20:05:05, WARNING, LM powered descent engine ignition
1969-07-20, 20:10:22, ERROR, LM 1202 alarm
1969-07-20, 20:14:18, ERROR, LM 1201 alarm
1969-07-20, 20:17:39, WARNING, LM lunar landing
1969-07-21, 02:39:33, DEBUG, EVA started (hatch open)
1969-07-21, 02:56:15, WARNING, 1st step taken lunar surface (CDR)
1969-07-21, 02:56:15, WARNING, Neil Armstrong first words on the Moon
1969-07-21, 03:05:58, DEBUG, Contingency sample collection started (CDR)
1969-07-21, 03:15:16, INFO, LMP on lunar surface
1969-07-21, 05:11:13, DEBUG, EVA ended (hatch closed)
1969-07-21, 17:54:00, WARNING, LM lunar liftoff ignition (LM APS)
1969-07-21, 21:35:00, INFO, CSM/LM docked
1969-07-22, 04:55:42, WARNING, Transearth injection ignition (SPS)
1969-07-24, 16:21:12, INFO, CM/SM separation
1969-07-24, 16:35:05, WARNING, Entry
1969-07-24, 16:50:35, WARNING, Splashdown (went to apex-down)
1969-07-24, 17:29, INFO, Crew egress"""

# English
# 1. Iterate over `DATA` with Apollo 11 timeline [1]
# 2. From each line extract date, time, level and message
# 3. Collect data to `result: map`
# 4. Run doctests - all must succeed

# Polish
# 1. Iteruj po `DATA` z harmonogramem Apollo 11 [1]
# 2. Dla każdej linii wyciągnij datę, czas, poziom logowania oraz wiadomość
# 3. Zbierz dane do `result: map`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
from dataclasses import dataclass

@dataclass
class Log:
    d: date
    t: time
    level: str
    message: str

    def get_log_dict(self):
        return {
            'datetime': datetime.combine(date.fromisoformat(str(self.d)), time.fromisoformat(str(self.t))),
            'level': self.level,
            'message': self.message
        }

def parse(line):
    data = line.strip().split(', ')
    return Log(*data).get_log_dict()

# Define `result: map` with `parse()` function applied to `DATA`
# type: map
result = map(parse, DATA.splitlines())