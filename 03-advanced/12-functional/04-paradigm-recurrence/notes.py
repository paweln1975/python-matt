#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/functional/paradigm-recurrence.html

#%% Functional Recurrence
# Also known as recursion
# Iteration in functional languages is usually accomplished via recursion
# Recursive functions invoke themselves
# Operation is repeated until it reaches the base case
# In general, recursion requires maintaining a stack, which consumes space in a linear amount to the depth of recursion.
# This could make recursion prohibitively expensive to use instead of imperative loops.
# However, a special form of recursion known as tail recursion can be recognized and optimized by a compiler into the same code used to implement iteration in imperative languages.
# Tail recursion optimization can be implemented by transforming the program into continuation passing style during compiling, among other approaches. [#WikipediaFunc]_



#%% Recurrence in Python
# Python isn't a functional language
# CPython implementation doesn't optimize tail recursion
# Tail recursion is not a particularly efficient technique in Python
# Rewriting the algorithm iteratively, is generally a better idea
# Uncontrolled recursion causes stack overflows!



#%% Recursion Depth Limit
# Default recursion depth limit is 1000
# Warning: Anaconda sets default recursion depth limit to 2000



#%% Tail Recursion
# Tail recursion is a special form of recursion
# The recursive call is the last thing executed by the function
# Tail recursion can be optimized by the compiler
# The compiler can reuse the stack frame of the current function call
# Tail recursion can be transformed into a loop
# Python doesn't optimize tail recursion