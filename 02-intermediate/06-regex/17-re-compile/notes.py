#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/re-compile.html

#%% Regex RE Compile
# re.compile()
# Used when pattern is reused (especially in the loop)



#%% Without Compilation
# Python will compile pattern during every loop iteration
# After compilation it will perform matching



#%% With Compilation
# Python will compile pattern once, before loop
# Then in the loop, only matching is performed