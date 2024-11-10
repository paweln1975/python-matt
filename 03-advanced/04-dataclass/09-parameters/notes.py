#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/dataclass/parameters.html

#%% Dataclass Parameters
# init - Generate __init__() method
# repr - Generate __repr__() method
# eq - Generate __eq__() and __ne__() methods
# order - Generate __lt__(), __le__(), __gt__(), and __ge__() methods
# unsafe_hash - If False: the __hash__() method is generated according to how eq and frozen are set
# frozen - If True: assigning to fields will generate an exception
# match_args - Generate __match_args__() method
# kw_only - Mark all fields as keyword-only
# slots - Create class with __slots__



#%% Init
# init=True by default
# Generate __init__() method



#%% Repr
# repr=True by default
# Generate __repr__() for pretty printing



#%% Frozen
# frozen=False by default
# Prevents object from modifications
# Assigning to fields will generate an exception



#%% Hash
# hash=False by default
# the __hash__() method is generated according to how eq and frozen are set



#%% Order
# order=False by default
# Generate __lt__(), __le__(), __gt__(), and __ge__() methods



#%% Match_args
# match_args=True by default
# Since Python 3.10



#%% Kw_only
# kw_only=False by default
# Mark all fields as keyword-only
# Since Python 3.10



#%% Slots
# slots=False by default
# Create class with __slots__
# Since Python 3.10