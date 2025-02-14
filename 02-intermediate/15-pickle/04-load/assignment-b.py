
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from os import remove
>>> remove(FILE)

>>> from pprint import pprint
>>> pprint(result)
[('Mark', 'Watney', 1),
 ('Melissa', 'Lewis', 3),
 ('Rick', 'Martinez', 1),
 ('Alex', 'Vogel', None),
 ('Chris', 'Beck', 1),
 ('Beth', 'Johanssen', 2)]
"""
# endregion

# region Show Imports
import pickle
# endregion

# region Show Types
result: list[tuple[str,str,int]]
# endregion

FILE = r'_temporary.pkl'

with open(FILE, mode='wb') as file:
    file.write(
        b'\x80\x04\x95\x81\x00\x00\x00\x00\x00\x00\x00]'
        b'\x94(\x8c\x04Mark\x94\x8c\x06Watney\x94K\x01\x87'
        b'\x94\x8c\x07Melissa\x94\x8c\x05Lewis\x94K\x03\x87'
        b'\x94\x8c\x04Rick\x94\x8c\x08Martinez\x94K\x01\x87'
        b'\x94\x8c\x04Alex\x94\x8c\x05Vogel\x94N\x87'
        b'\x94\x8c\x05Chris\x94\x8c\x04Beck\x94K\x01\x87'
        b'\x94\x8c\x04Beth\x94\x8c\tJohanssen\x94K\x02\x87\x94e.'
    )

# English
# 1. Define `result: list[User]` with data from `FILE`
# 2. Use `pickle` module
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: list[User]` z danymi z `FILE`
# 2. Użyj modułu `pickle`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code

result = pickle.load(open(FILE, 'rb'))
