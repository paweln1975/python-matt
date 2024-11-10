#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/match/about.html

#%% Match About
# Since Python 3.10: :pep:636 -- Structural Pattern Matching: Tutorial
# Significantly faster for sequences and mappings [#Shaw2022]_
# Since Python 3.11: For sequences if faster around 80% [#Shaw2022]_
# Since Python 3.11: For mappings if faster around 80% [#Shaw2022]_
# https://github.com/python/cpython/blob/main/Grammar/python.gram#L479



#%% Problem



#%% Solution



#%% Patterns
# literal pattern
# capture pattern
# wildcard pattern
# constant value pattern
# sequence pattern
# mapping pattern
# class pattern
# OR pattern
# walrus pattern



#%% Recap
# x - assign x = subject
# 'x' - test subject == 'x'
# x.y - test subject == x.y
# x() - test isinstance(subject, x)
# {'x': 'y'} - test isinstance(subject, Mapping) and subject.get('x') == 'y'
# ['x'] - test isinstance(subject, Sequence) and len(subject) == 1 and subject[0] == 'x'
# Source: [#Hettinger2021]_



#%% Further Reading
# https://peps.python.org/pep-0622/
# https://peps.python.org/pep-0636/