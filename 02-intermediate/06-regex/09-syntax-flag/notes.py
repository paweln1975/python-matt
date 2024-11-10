#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/syntax-flag.html

#%% Regex Syntax Flag
# re.ASCII - perform ASCII-only matching instead of full Unicode matching
# re.IGNORECASE - case-insensitive search
# re.MULTILINE - match can start in one line, and end in another
# re.DOTALL - dot (.) matches also newline characters
# re.UNICODE - turns on unicode character support for \w
# re.VERBOSE - ignores spaces (except \s) and allows for comments in in re.compile()
# re.DEBUG - display debugging information during pattern compilation



#%% IGNORECASE
# Short: i
# Long: re.IGNORECASE
# Case-insensitive search
# Has Unicode support i.e. Ą and ą



#%% UNICODE
# Short: u
# Long: re.UNICODE
# On by default
# Turns on unicode character support
# Works for \w and \W



#%% ASCII
# Short: a
# Long: re.ASCII
# Perform ASCII-only matching instead of full Unicode matching
# Works for \w, \W, \b, \B, \d, \D, \s and \S
# ASCII only search is faster, but does not include unicode characters



#%% MULTILINE
# Short: m
# Long: re.MULTILINE
# Match can start in one line, and end in another
# Changes meaning of ^, now it is a start of a line
# Changes meaning of $, now it is an end of line



#%% DOTALL
# Short: s
# Long: re.DOTALL
# Dot (.) matches also newline characters
# By default newlines are not matched by .



#%% DEBUG
# Long: re.DEBUG
# Display debugging information during pattern compilation



#%% VERBOSE
# Short: x
# Long: re.VERBOSE
# Ignores spaces (except \s) and allows for comments in in re.compile()