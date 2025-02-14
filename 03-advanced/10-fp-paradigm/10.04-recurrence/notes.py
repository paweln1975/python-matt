#!/usr/bin/env python3
# https://python3.info/advanced/fp-paradigm/recurrence.html


# %% Functional Recurrence
# - Also known as recursion
# - Iteration in functional languages is usually accomplished via recursion
# - Recursive functions invoke themselves
# - Operation is repeated until it reaches the base case
# - In general, recursion requires maintaining a stack, which consumes space in a linear amount to the depth of recursion.
# - This could make recursion prohibitively expensive to use instead of imperative loops.
# - However, a special form of recursion known as tail recursion can be recognized and optimized by a compiler into the same code used to implement iteration in imperative languages.
# - Tail recursion optimization can be implemented by transforming the program into continuation passing style during compiling, among other approaches. [#WikipediaFunc]_
# - Axiom - An axiom, postulate, or assumption is a statement that is taken to be true, to serve as a premise or starting point for further reasoning and arguments.
# %%



# %% Recurrence in Python
# - Python isn't a functional language
# - CPython implementation doesn't optimize tail recursion
# - Tail recursion is not a particularly efficient technique in Python
# - Rewriting the algorithm iteratively, is generally a better idea
# - Uncontrolled recursion causes stack overflows!
# %%



# %% Problem
# %%



# %% Solution: Iteration
# - 5! = 5 * 4 * 3 * 2 * 1
# - factorial(5) = 5 * 4 * 3 * 2 * 1
# - factorial(5) = product(1,6)
# %%



# %% Solution: Recurrence
# - n! = n * (n-1)!  # when n==0 -> 1
# - factorial(5) = 5 * factorial(4)
# %%



# %% Solution: Reduce + Mul + Range
# - 5! = 5 * 4 * 3 * 2 * 1
# %%



# %% Recursion Depth Limit
# - Default recursion depth limit is 1000
# - Warning: Anaconda sets default recursion depth limit to 2000
# %%



# %% Tail Recursion
# - Tail recursion is a special form of recursion
# - The recursive call is the last thing executed by the function
# - Tail recursion can be optimized by the compiler
# - The compiler can reuse the stack frame of the current function call
# - Tail recursion can be transformed into a loop
# - Python doesn't optimize tail recursion
# %%



# %% Performance
# - Date: 2024-12-16
# - Python: 3.13.1
# - IPython: 8.30.0
# - System: macOS 15.2
# - Computer: MacBook M3 Max
# - CPU: 16 cores (12 performance and 4 efficiency) / 3nm
# - RAM: 128 GB RAM LPDDR5
# %%



