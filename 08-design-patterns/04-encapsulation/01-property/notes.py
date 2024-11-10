#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/encapsulation/property.html

#%% Encapsulation Property
# Disable attribute modification
# Logging value access
# Check boundary
# Raise exceptions such as ValueError or TypeError
# Check argument type



#%% Setter and Getter Methods
# Not only Java, but C++ and many others too



#%% Pythonic Way



#%% Encapsulation



#%% Protocol
# myattribute = property() - creates property
# @myattribute.getter - getter for attribute
# @myattribute.setter - setter for attribute
# @myattribute.deleter - deleter for attribute
# Method name must be the same as attribute name
# myattribute has to be property
# @property - creates property and a getter



#%% Property Descriptor
# name = property()



#%% Property Decorator
# Typically used when, there is only getter and no setter and deleter methods



#%% Property Class
# property() has 4 arguments
# fset: Callable - setter method
# fget: Callable - getter method
# fdel: Callable - deleter method
# doc: str - docstring



#%% Property Lambda
# property() has 4 arguments
# fset: Callable - setter method
# fget: Callable - getter method
# fdel: Callable - deleter method
# doc: str - docstring