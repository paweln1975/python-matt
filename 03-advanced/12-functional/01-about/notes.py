#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/functional/about.html

#%% Functional About
# Programming paradigm
# Programs are constructed by applying and composing functions
# Functions are treated as first-class citizens
# Functional programming avoids side effects
# Functional programming provides referential transparency
# Instead of loop use map and recurrence
# Functions can be bound to names (including local identifiers), passed as arguments, and returned from other functions, just as any other data type can [#WikipediaFunc]_
# Imperative program will use a loop to traverse and modify a list, while a functional program, would prefer using a higher-order map function that takes a function and a list, generating and returning a new list by applying the function to each list item [#Spiewak2008]_
# Restricting side effects, can decrease number of bugs, be easier to debug and test, and be more suited to formal verification [#Hughes1984]_ [#Hudak1989]_
# Functional Design Patterns - Scott Wlaschin https://www.youtube.com/watch?v=srQt1NAHYC0
# The Functional Programmer's Toolkit - Scott Wlaschin - https://www.youtube.com/watch?v=Nrp_LZ-XGsY



#%% Advantages
# Comprehensibility: Pure functions don't change states and are entirely dependent on input, and are consequently simple to understand.
# Concurrency: As pure functions avoid changing variables or any data outside it, concurrency implementation is easier.
# Lazy evaluation: Functional programming encourages lazy evaluation, which means that the value is evaluated and stored only when required.
# Easier debugging and testing: Pure functions take arguments once and produce unchangeable output. With immutability and no hidden output, debugging and testing becomes easier.



#%% Disadvantages
# Potentially poorer performance: Immutable values combined with recursion might lead to a reduction in performance.
# Coding difficulties: Though writing pure functions is easy, combining it with the rest of the application and I/O operations can be tough.
# No loops can be challenging: Writing programs in a recursive style instead of loops can be a daunting task.



#%% Applications



#%% Further Reading
# Functional Design Patterns - Scott Wlaschin - https://www.youtube.com/watch?v=srQt1NAHYC0
# The Functional Programmer's Toolkit - Scott Wlaschin - https://www.youtube.com/watch?v=Nrp_LZ-XGsY



#%% Doctests