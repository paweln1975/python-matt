#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/modules/venv.html

#%% Module venv
# Isolated Python environment
# Allows to have multiple versions of Python for one project
# For testing on different versions: python3.11, python3.12, python3.13
# Test libraries and frameworks before upgrading (create venv, install requirements, run tests, delete if fails)
# Allows to have different versions of libraries and frameworks for each project
# Difference between venv and virtualenv
# venv is bundled with Python since 3.3 (no installation required)
# virtualenv is independent package installed via pip
# virtualenvwrapper is additionally installed command line tools



#%% Venv vs Virtualenv



#%% Create
# venv-py312 is the name of venv folder
# See "Directory Naming Convention" below



#%% Run Ad-Hoc
# Will run python with from virtual environment
# With all the modules already installed



#%% Activate
# bin for macOS, Linux, BSD
# Scripts for Windows
# Note the direction of slash and backslash (OS dependent)



#%% Install Modules Ad-Hoc



#%% Directory Naming Convention
# No standard naming convention
# Naming directory like module (venv) name is a good idea
# Adding Python version is also a good practice
# Optionally naming per main framework/library version
# Dot at the beginning hides directory on Linux and macOS (but doesn't work on Windows)
# Underscore is Python convention for private/protected, but does not work for OS and Git



#%% Good Practices
# python3.12 -m venv -h
# python3.12 -m venv --upgrade-deps venv-py312
# Name venv directory similar to python version venv-py3.12
# Place in your project directory
# Add venv directory to .gitignore (important!)
# Change prompt by appending at the end of venv-3.12/bin/activate:



#%% Bash Prompt
# Default on most Linux distributions
# \e[  – This string tells bash prompt to apply color from next character.
# 0;32m  – This string represents the colors. The number before the; represent typeface. And the number after the ; represent color code.
# \e[0m – This string will tell the bash prompt to apply the color to the previous character.



#%% Zsh Prompt
# Default on macOS
# Colors: black, blue, cyan, green, magenta, red, white, yellow



#%% Shebang



#%% Further Reading
# https://github.com/pypa/virtualenv/issues/2007