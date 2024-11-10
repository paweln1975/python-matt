#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/abstract/abstract-class.html

#%% Abstract Base Class
# Since Python 3.0: :pep:3119 -- Introducing Abstract Base Classes
# Cannot instantiate
# Possible to indicate which method must be implemented by child
# Inheriting class must implement all methods
# Some methods can have implementation
# Python Abstract Base Classes [#pydocabc]_



#%% Syntax
# Inherit from ABC
# At least one method must be abstractmethod or abstractproperty
# Body of the method is not important, it could be raise NotImplementedError or pass



#%% Implement Abstract Methods
# All abstract methods must be covered
# Abstract base class can have regular (not abstract) methods
# Regular methods will be inherited as normal
# Regular methods does not need to be overwritten



#%% ABCMeta
# Uses metaclass=ABCMeta
# Not recommended since Python 3.4
# Use inheriting ABC instead



#%% Abstract Property
# abc.abstractproperty is deprecated since Python 3.3
# Use property with abc.abstractmethod instead



#%% Problem: Base Class Has No Abstract Method



#%% Problem: Base Class Does Not Inherit From ABC



#%% Problem: All Abstract Methods are not Implemented



#%% Problem: Some Abstract Methods are not Implemented



#%% Problem: Child Class has no Abstract Property
# Using abstractproperty



#%% Problem: Child Class has no Abstract Properties
# Using property and abstractmethod



#%% Problem: Invalid Order of Decorators
# Invalid order of decorators: @property and @abstractmethod
# Should be: first @property then @abstractmethod



#%% Problem: Overwrite ABC File



#%% Further Reading
# https://docs.python.org/dev/library/collections.abc.html#collections-abstract-base-classes
# https://www.youtube.com/watch?v=S_ipdVNSFlo