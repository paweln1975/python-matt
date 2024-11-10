#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/syntax-quantifier.html

#%% Regex Syntax Quantifier
# Quantifier specifies how many occurrences of preceding qualifier or character class
# Exact
# Greedy
# Lazy



#%% Exact
# Exact match
# {n} - exactly n repetitions



#%% Greedy
# Prefer longest matches
# Works better with numbers
# Not that good results for text
# Default behavior
# {n,m} - minimum n repetitions, maximum m times, prefer longer
# {,n} - maximum n repetitions, prefer longer
# {n,} - minimum n repetitions, prefer longer
# {0,1} - minimum 0 repetitions, maximum 1 repetitions (maybe)
# * - minimum 0 repetitions, no maximum, prefer longer (alias to {0,})
# + - minimum 1 repetitions, no maximum, prefer longer (alias to {1,})
# ? - minimum 0 repetitions, maximum 1 repetitions, prefer longer (alias to {0,1})



#%% Lazy
# Prefer shortest matches
# Works better with text
# Not that good results for numbers
# Non-greedy
# {n,m}? - minimum n repetitions, maximum m times, prefer shorter
# {,n}? - maximum n repetitions, prefer shorter
# {n,}? - minimum n repetitions, prefer shorter
# {0,1}? - minimum 0 repetitions, maximum 1 repetitions (maybe)
# *? - minimum 0 repetitions, no maximum, prefer shorter (alias to {0,}?)
# +? - minimum 1 repetitions, no maximum, prefer shorter (alias to {1,}?)
# ?? - minimum 0 repetitions, maximum 1 repetition, prefer shorter (alias to {0,1}?)



#%% Greedy vs. Lazy