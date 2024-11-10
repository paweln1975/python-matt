#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/files/mode-write.html

#%% File Write
# Creates file if not exists
# Truncate the file before writing
# Works with both relative and absolute path
# Fails when directory with file cannot be accessed
# mode parameter to open() function is required



#%% Line
# File must end with a newline \n character
# POSIX Definition: A sequence of zero or more non-<newline> characters plus a terminating <newline> character.



#%% Write to File
# Always remember to close file



#%% Write One Line



#%% Write Multiple Lines
# Write a list of lines to the file.
# .writelines() does not add a line separator (\n)!!
#  Each line must add a separator at the end.



#%% Write Non-Str Data
# Join works only for strings
# Conversion to str must be performed before adding a separator and



#%% Reading From One File and Writing to Another