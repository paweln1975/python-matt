#!/usr/bin/env python3
# https://python3.info/testing/unittest/patch.html


# %% Unittest Patch
# %%



# %% Patch Randint
# %%



# %% Patch Date in Different Files
# - class User is in the myfile.py file
# - tests are in the mytests.py file
# - cannot patch('date.today', return_value=...) because it is immutable
# %%



# %% Patch Date in the Same File
# - class User is in the myfile.py file
# - tests are also in the myfile.py file
# - mind additional import inside of a context manager
# - this is due to the fact, that date will be mocked (date.today())
# - and today.return_value is also a date object (date(2024, 1, 2))
# %%



