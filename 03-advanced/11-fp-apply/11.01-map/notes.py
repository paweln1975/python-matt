#!/usr/bin/env python3
# https://python3.info/advanced/fp-apply/map.html


# %% FP Apply Map
# %%



# %% About
# - Converts elements in sequence
# - Lazy evaluated
# - map(callable, *iterables)
# - required callable - Function
# - required iterables - 1 or many sequence or iterator objects
# %%



# %% Problem
# %%



# %% Solution
# - List Comprehension
# - Map
# %%



# %% Lazy Evaluation
# %%



# %% For Loop
# %%



# %% Multiple Arguments
# %%
def power(x, y):
    return x ** y

test_list = [1, 2, 3, 4]
test_powers = [2, 2, 3, 4]

result = list(map(power, test_list, test_powers))
print(result)


# %% Starmap
# %%

from itertools import starmap
test_data = [(x, x) for x in range(1, 5)]

result = list(starmap(power, test_data))
print(result)

# %% Not A Generator
# - from inspect import isgeneratorfunction, isgenerator
# - isgeneratorfunction(callable) - Check if the object is a generator function
# - isgenerator(iterator) - Check if the object is a generator iterator
# - map() is not a generator function
# %%



# %% Performance
# - Date: 2024-12-01
# - Python: 3.13.0
# - IPython: 8.30.0
# - System: macOS 15.1.1
# - Computer: MacBook M3 Max
# - CPU: 16 cores (12 performance and 4 efficiency) / 3nm
# - RAM: 128 GB RAM LPDDR5
# %%


from doctest import testmod as run_tests

DATA = """150,4,setosa,versicolor,virginica
5.1,3.5,1.4,0.2,0
7.0,3.2,4.7,1.4,1
6.3,3.3,6.0,2.5,2
4.9,3.0,1.4,0.2,0
6.4,3.2,4.5,1.5,1
5.8,2.7,5.1,1.9,2"""


def get_labelencoder(header: str) -> dict[int, str]:
    """
    >>> get_labelencoder('150,4,setosa,versicolor,virginica')
    {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    """
    nrows, nfeatures, *class_labels = header.split(',')
    return dict(enumerate(class_labels))

header, *lines = DATA.splitlines()
label_encoder = get_labelencoder(header)

def get_data(line: str) -> tuple:
    """
    >>> get_data('5.1,3.5,1.4,0.2,0')
    (5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> get_data('7.0,3.2,4.7,1.4,1')
    (7.0, 3.2, 4.7, 1.4, 'versicolor')
    >>> get_data('6.3,3.3,6.0,2.5,2')
    (6.3, 3.3, 6.0, 2.5, 'virginica')
    """
    *values, species = line.split(',')
    values = map(float, values)
    species = label_encoder[int(species)]
    return tuple(values) + (species,)


if __name__ == '__main__':
    run_tests()
    result = list(map(get_data, lines))
    print(result)