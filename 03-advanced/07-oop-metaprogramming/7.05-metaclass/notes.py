#!/usr/bin/env python3
# https://python3.info/advanced/oop-metaprogramming/metaclass.html


# %% Metaprogramming Metaclass
# - Object is an instance of a class
# - Class is an instance of a Metaclass
# - Class defines how an object behaves
# - Metaclass defines how a class behaves
# %%



# %% Recap
# - Functions are instances of a function class
# %%



# %% Class Creation
# - type(str, tuple, dict) will create a class object
# %%



# %% Function Based Metaclass
# - Metaclass is a function which returns a class
# %%



# %% Class Based Metaclass
# - Typically Metaclasses are defined as a class
# - Metaclass is a class which returns a class from it's constructor
# %%



# %% Using Metaclasses
# - Metaclasses are used by setting the metaclass keyword argument
# - This works for both function and class based metaclasses
# - For future, we will use the class based metaclasses and metaclass=... syntax
# - It is exactly equivalent to other ones, but it is more common in practice
# %%



# %% Rationale
# - Metaclasses allow you to do 'extra things' when creating a class
# - Allow customization of class instantiation
# - Most commonly used as a class-factory
# - Registering the new class with some registry
# - Replace the class with something else entirely
# - Inject logger instance
# - Injecting static fields
# - Ensure subclass implementation
# - Metaclasses run when Python defines class (even if no instance is created)
# %%



# %% Hiding Metaclass
# - Metaclasses can be hidden by using inheritance
# - This is a common pattern in Python frameworks
# %%



# %% Metaclass Arguments
# - Metaclasses can accept additional arguments
# - Arguments can be passed to metaclass using metaclass=... syntax
# - This behavior allows for more customization
# %%



# %% Metaclass Protocol
# - __prepare__(metacls, name, bases, **kwargs) -> dict - on class namespace initialization
# - __new__(metacls, classname, bases, attrs) -> cls - before class creation
# - __init__(self, name, bases, attrs) -> None - after class creation
# - __call__(self, *args, **kwargs) - when the class is called (instantiated)
# %%



# %% Instance vs. Class vs. Metaclass
# - MRO - Method Resolution Order
# - MRO is a list of classes that Python will use to search for methods
# - MRO is defined by C3 Linearization algorithm
# - MRO is defined by __mro__ attribute
# %%



# %% Class Bases
# - Bases for an instance stays the same
# - Bases of a class changes when using a metaclass
# %%



# %% Type Metaclass
# - All types (user-defined and built-in) are instances of a type class
# - This is also true for an object type
# - Even type type is an instance of a type
# %%



# %% Metaclass replacements
# - Metaclasses allows for more customization, but at a cost of complexity
# - There are several ways, how you can achieve the same effect
# %%



