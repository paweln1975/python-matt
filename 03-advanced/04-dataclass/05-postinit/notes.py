#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/dataclass/postinit.html

#%% Dataclass Postinit
# Dataclasses generate __init__()
# Overloading __init__() manually will destroy it
# For init time validation there is __post_init__()
# It is run after all parameters are set in the class
# Hence you have to take care about negative cases (errors)



#%% Problem
# Init serves not only for fields initialization
# It could be also used for value validation



#%% Solution
# Creating own __init__() will overload init from dataclasses
# Therefore in dataclasses there is __post_init__() method
# It is run after init (as the name suggest)
# It works on fields, which already saved (it was done in __init__)
# No need to assign it once again
# You can focus only on bailing-out (checking only negative path - errors)



#%% Type Conversion
# __post_init__() can also be used to convert data
# Example str 2000-01-02 to date object date(2000, 1, 2)



#%% InitVar
# Init-only fields
# Added as parameters to the generated __init__
# Passed to the optional __post_init__ method
# They are not otherwise used by Data Classes