#!/usr/bin/env python3

# Reference:
# https://python3.info/oop/paradigm/interface.html

#%% Abstract Interface
# Python don't have interfaces, although you can achieve similar effect
# Since Python 3.8 there are Protocols, which effectively are interfaces
# Interfaces cannot be instantiated
# Interfaces can be implemented
# Implemented class must define all interface methods (implement interface)
# Only public method declaration



#%% Problem
# Different method names
# Different method return type
# Different parameter names
# Different parameter types



#%% Solution
# Interface specifies method names, method return type, parameter names and types
# This way, you can substitute one class with another without changing much code



#%% Dependency Inversion Principle
# One of S.O.L.I.D. principles
# DIP - Dependency Inversion Principle
# Always depend on an abstraction not concrete implementation



#%% Interface Names
# Account
# IAccount
# AccountIface
# AccountInterface



#%% Syntax
# raise NotImplementedError



#%% Other Languages
# This currently does not exists in Python
# In fact it is not even a valid Python syntax
# But it could greatly improve readability



#%% Should Fields be in the Interface?
# Generally no, but...
# Encapsulation requires state to be hidden inside of a class
# Therefore all fields should be private, and there should be public methods to manipulate them
# Public methods should be in the interface
# Although in Python, all fields are public, and we set their values directly without setters and getters
# Then, they should be in the interface (this is controversial)



#%% Interface vs Abstract Class
# Abstract class: Regular classes and you can inherit from them
# Abstract class: This allows to have a default implementation of some methods
# Abstract class: In the child class only abstract methods have to be implemented
# Abstract class: Validation is dynamic (in the runtime)
# Interface: Validation is static (without running the code)
# Interface: Cannot have methods with implementation
# Interface: Contain only methods names and returning types, parameter names and types