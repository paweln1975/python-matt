#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/functional/pattern-closure.html

#%% Functional Pattern Closure
# Technique by which the data is attached to some code even after end of those other original functions is called as closures
# When the interpreter detects the dependency of inner nested function on the outer function, it stores or makes sure that the variables in which inner function depends on are available even if the outer function goes away
# Closures provides some form of data hiding
# Closures can avoid use of global variables
# Useful for replacing hard-coded constants
# Inner functions implicitly carry references to all of the local variables in the surrounding scope that are referenced by the function
# Since Python 2.2



#%% Recap



#%% Nested Function
# Function inside the function
# Nested functions can access the variables of the enclosing scope



#%% What is closure?



#%% Why?
# Closures provides some form of data hiding
# Closures can avoid use of global variables
# Useful for replacing hard-coded constants



#%% How Objects Were Born
# main - constructor
# say_hello - instance method
# firstname - instance variable (field)
# lastname - instance variable (field)