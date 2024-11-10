#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/dataclass/mutable-args.html

#%% Dataclass Mutable Attrs
# problem with dict, list, set
# You should not set mutable objects as a default function argument
# field() creates new empty list for each object
# It does not reuse reference
# Discussion: https://github.com/ericvsmith/dataclasses/issues/3



#%% Recap
# You should not set mutable objects as a default function argument
# Problem with mutable data structures like: dict, list, set
# This problem occurs also in Java Script, PHP, Ruby, etc
# This is how all dynamically typed languages work
# Method signature is evaluated once, when the function is defined
# Method body is evaluated each time, when the function is called



#%% Problem



#%% Solution



#%% Default Values



#%% Default Factory



#%% Short Notation
# list is a callable object