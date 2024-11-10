#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/pathlib/path-relative.html

#%% File Path Relative
# Python works with both relative and absolute path
# Path is relative to currently running script
# Path separator \ (backslash) is used on Windows
# Path separator / (slash) is used on *nix operating systems: Linux,



#%% Current Directory
# Path is relative to currently running script
# . - Current directory



#%% Upper Directory
# Path is relative to currently running script
# .. - Parent directory



#%% Current Working Directory
# Returns an absolute path to current working directory



#%% Good Practices
# Never hardcode paths, use constant as a file name or file path
# Convention (singular form): FILE, FILENAME, FILEPATH, PATH
# Convention (plural form): FILES, FILENAMES, FILEPATHS, PATHS
# Note, that PATH is usually used for other purposes (sys.path or