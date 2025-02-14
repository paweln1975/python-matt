result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = {0, 1, 2}
MEDIUM = {3, 4, 5, 6}
LARGE = {7, 8, 9}

for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if 0 <= digit < 3:
#         result['small'] += 1
#     elif 3 <= digit < 7:
#         result['medium'] += 1
#     elif 7 <= digit < 10:
#         result['large'] += 1

# %%
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if 0 <= digit and digit < 3:
#         result['small'] += 1
#     elif 3 <= digit and digit < 7:
#         result['medium'] += 1
#     elif 7 <= digit and digit < 10:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit < 3:
#         result['small'] += 1
#     elif digit < 7:
#         result['medium'] += 1
#     elif digit < 10:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit < 3:
#         result['small'] += 1
#     elif digit < 7:
#         result['medium'] += 1
#     else:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in [0,1,2]:
#         result['small'] += 1
#     elif digit in [3,4,5,6]:
#         result['medium'] += 1
#     elif digit in [7,8,9]:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in (0,1,2):
#         result['small'] += 1
#     elif digit in (3,4,5,6):
#         result['medium'] += 1
#     elif digit in (7,8,9):
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in {0,1,2}:
#         result['small'] += 1
#     elif digit in {3,4,5,6}:
#         result['medium'] += 1
#     elif digit in {7,8,9}:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in range(0,3):
#         result['small'] += 1
#     elif digit in range(3,7):
#         result['medium'] += 1
#     elif digit in range(7,10):
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = range(0,3)
# MEDIUM = range(3,7)
# LARGE = range(7,10)
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = [0,1,2]
# MEDIUM = [3,4,5,6]
# LARGE = [7,8,9]
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = (0,1,2)
# MEDIUM = (3,4,5,6)
# LARGE = (7,8,9)
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = {0,1,2}
# MEDIUM = {3,4,5,6}
# LARGE = {7,8,9}
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = [x for x in range(0,3)]
# MEDIUM = [x for x in range(3,7)]
# LARGE = [x for x in range(7,10)]
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = (x for x in range(0,3))
# MEDIUM = (x for x in range(3,7))
# LARGE = (x for x in range(7,10))
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = {x for x in range(0,3)}
# MEDIUM = {x for x in range(3,7)}
# LARGE = {x for x in range(7,10)}
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = {x for x in (0,1,2)}
# MEDIUM = {x for x in (3,4,5,6)}
# LARGE = {x for x in (7,8,9)}
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = (x for x in (0,1,2))
# MEDIUM = (x for x in (3,4,5,6))
# LARGE = (x for x in (7,8,9))
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = [x for x in (0,1,2)]
# MEDIUM = [x for x in (3,4,5,6)]
# LARGE = [x for x in (7,8,9)]
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in [x for x in range(0,3)]:
#         result['small'] += 1
#     elif digit in [x for x in range(3,7)]:
#         result['medium'] += 1
#     elif digit in [x for x in range(7,10)]:
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in (x for x in range(0,3)):
#         result['small'] += 1
#     elif digit in (x for x in range(3,7)):
#         result['medium'] += 1
#     elif digit in (x for x in range(7,10)):
#         result['large'] += 1

# %% Alternatively
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in {x for x in range(0,3)}:
#         result['small'] += 1
#     elif digit in {x for x in range(3,7)}:
#         result['medium'] += 1
#     elif digit in {x for x in range(7,10)}:
#         result['large'] += 1