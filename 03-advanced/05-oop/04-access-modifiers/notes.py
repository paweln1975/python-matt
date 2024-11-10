#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/oop/access-modifiers.html

#%% OOP Access Modifiers
# Methods are always public
# There is no public, protected, and private keywords
# Protecting is only by convention [#pydocprivatevar]_



#%% Name Convention
# name(self) - public method
# _name(self) - protected method (non-public by convention)
# __name(self) - private method (name mangling)
# __name__(self) - system method
# name_(self) - avoid name collision with keywords or built-in functions (and_, or_, id_, type_)



#%% Public Methods
# Methods are always public



#%% Protected Methods
# Methods are always public
# Protecting is only by convention [#pydocprivatevar]_



#%% Private Methods
# Methods are always public
# Protecting is only by convention [#pydocprivatevar]_
# Name mangling - adding a name of a class to the method name
# Name mangling is used to avoid name collision in subclasses



#%% System Methods
# Also known as magic methods



#%% Dir
# dir() - show all attributes of an object
# callable() - check if an attribute is callable
# In order to get methods you need to filter them by checking if they are callable