
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = open(FILE).read()
>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is str, \
'Variable `result` has invalid type, should be str'

>>> from os import remove
>>> remove(FILE)

>>> print(result)
"firstname","group1_gid","group1_name","group2_gid","group2_name","lastname"
"Mark","1","staff","","","Watney"
"Melissa","1","staff","2","admins","Lewis"
"Rick","","","","","Martinez"
<BLANKLINE>
"""
# endregion

# region Show Imports
import csv
# endregion

FILE = r'_temporary.csv'

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "groups": [
        {"gid": 1, "name": "staff"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "groups": [
        {"gid": 1, "name": "staff"},
        {"gid": 2, "name": "admins"}]},

    {"firstname": "Rick", "lastname": "Martinez", "groups": []},
]

# English
# 1. Convert `DATA` to format with one column per each attribute for example:
#    - `mission1_year`, `mission2_year`,
#    - `mission1_name`, `mission2_name`
# 2. Note, that enumeration starts with one
# 3. Sort `fieldnames`
# 4. Save data to `FILE`
# 5. Run doctests - all must succeed

# Polish
# 1. Przekonwertuj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
#    - `mission1_year`, `mission2_year`,
#    - `mission1_name`, `mission2_name`
# 2. Zwróć uwagę, że enumeracja zaczyna się od jeden
# 3. Posortuj `fieldnames`
# 4. Zapisz dane do `FILE`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
result = []
for user in DATA:
    firstname = user["firstname"]
    lastname = user["lastname"]
    groups = user["groups"]
    user_dict = {'firstname': firstname, 'lastname': lastname}
    for group_nr, group in enumerate(groups, start=1):
        gid = group["gid"]
        name = group["name"]
        user_dict.update({f'group{group_nr}_gid': gid,
                           f'group{group_nr}_name': name})
    result.append(user_dict)


header = set()
for row in result:
    header.update(row.keys())

with open(FILE, mode='wt', encoding='utf-8') as file:
    writer = csv.DictWriter(file,
                            fieldnames=sorted(header),
                            lineterminator='\n',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)
