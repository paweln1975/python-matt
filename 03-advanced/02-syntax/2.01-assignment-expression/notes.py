import re
#!/usr/bin/env python3
# https://python3.info/advanced/syntax/assignment-expression.html


# %% Syntax Assignment Expression
# - Since Python 3.8: :pep:572 -- Assignment Expressions
# - Also known as "Walrus operator"
# - Also known as "Named expression"
# %%

total = 0
partial_sums = [total:=total + v for v in range(1, 11)]
print(partial_sums)
# [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

print(f'{total=}')
# total=55

# %% Syntax
# %%



# %% Usage
# %%

email = 'mwatney@nasa.gov'

pattern = r'([a-z]+)@nasa.gov'
if result := re.search(pattern, email):
    username = result.group(1)
    print(f'{username=}')

# username='mwatney'

DATA = [{'name': 'Melissa Lewis', 'email': 'mlewis@nasa.gov'},
             {'name': 'Rick Martinez', 'email': 'rmartinez@nasa.gov'},
             {'name': 'Alex Vogel', 'email': 'avogel@esa.int'},
             {'name': 'Pan Twardowski', 'email': 'ptwardowski@polsa.gov.pl'},
             {'name': 'Chris Beck', 'email': 'cbeck@nasa.gov'},
             {'name': 'Beth Johanssen', 'email': 'bjohanssen@nasa.gov'},
             {'name': 'Mark Watney', 'email': 'mwatney@nasa.gov'},
             {'name': 'Ivan Ivanovich', 'email': 'iivanovich@roscosmos.ru'}]
DOMAINS = ('esa.int', 'nasa.gov')

result = [email for user in DATA if (email:=user['email']) and email.endswith(DOMAINS)]
print(result)

# ['mlewis@nasa.gov', 'rmartinez@nasa.gov', 'avogel@esa.int',
# 'cbeck@nasa.gov', 'bjohanssen@nasa.gov', 'mwatney@nasa.gov']


DATA = [
    'Mark Watney',
    'Melissa Lewis',
    'Rick Martinez',
]

result = [{'firstname': name[0], 'lastname': name[1]}
          for fullname in DATA
          if (name := fullname.split())]
print(result)
# [{'firstname': 'Mark', 'lastname': 'Watney'},
# {'firstname': 'Melissa', 'lastname': 'Lewis'},
# {'firstname': 'Rick', 'lastname': 'Martinez'}]

result = [{'firstname': firstname, 'lastname': lastname}
          for fullname in DATA
          if (name := fullname.split())
          and (firstname := name[0])
          and (lastname := name[1])]
print(result)
# [{'firstname': 'Mark', 'lastname': 'Watney'},
# {'firstname': 'Melissa', 'lastname': 'Lewis'},
# {'firstname': 'Rick', 'lastname': 'Martinez'}]


# %% Value of the Expression
# - First defines identifier with value
# - Then returns the value from the identifier
# - Both operations in the same line
# - result = (x := 1)
# %%



# %% Do-While Loop
# %%



# %% Unpacking Optionals
# %%



# %% Assign in the Expression
# - if x := 1: ...
# %%



# %% Assignment and Evaluation
# - if x := 1: ...
# - if x := 0: ...
# %%



# %% What Assignment Expression is?
# - if x := 1: ... is equivalent to x = 1; if x:
# %%



# %% What Assignment Expression is not?
# - It's not substitution for equals
# - x = 1 - works
# - x := 1 - SyntaxError
# %%



# %% Assignment vs. Assignment Expression
# %%
