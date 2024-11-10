#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/encapsulation/descriptor.html

#%% Encapsulation Descriptor
# Add managed attributes to objects
# Outsource functionality into specialized classes
# Descriptors: classmethod, staticmethod, property, functions in general
# __del__(self) is reserved when object is being deleted by garbage collector (destructor)
# __set_name() After class creation, Python default metaclass will call it with cls and classname



#%% Protocol
# __get__(self, cls, *args) -> self
# __set__(self, cls, value) -> None
# __delete__(self, cls) -> None
# __set_name__(self)



#%% Property vs Reflection vs Descriptor



#%% Inheritance



#%% Function Descriptor
# Function are Descriptors too