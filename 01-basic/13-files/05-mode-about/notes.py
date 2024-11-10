#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/files/mode-about.html

#%% File Modes
# Text - easy to read and write
# Binary - Fast and efficient
# Read - Get data from file
# Write - Save data to file (overwrite existing data)
# Append - Add line to file
# Update - Read and Write (rarely used)



#%% Modes
# r - For reading – The file pointer is placed at the beginning of the file. This is the default mode.
# r+ - Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
# w - Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# w+ - Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
# rb - Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
# rb+ - Opens a file for both reading and writing in binary format.
# wb+ - Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
# a - Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# ab - Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# a+ - Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# ab+ - Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# x - Open for exclusive creation, failing if the file already exists (Python 3)



#%% Short Notation
# Most commonly used
# By default text mode is used
# mode='r' - read in text mode (default)
# mode='w' - write in text mode
# mode='a' - append in text mode



#%% Text Mode
# Text - easy to read and write
# mode='rt' - read in text mode
# mode='wt' - write in text mode
# mode='at' - append in text mode



#%% Binary Mode
# Binary - Fast and efficient
# mode='rb' - read in binary mode
# mode='wb' - write in binary mode
# mode='ab' - append in binary mode



#%% Update Mode
# Reading and Writing
# Text mode is used if not specified otherwise
# mode='r+' - read in text mode
# mode='w+' - write in text mode
# mode='a+' - append in text mode
# mode='rt+' - update in text mode
# mode='wt+' - update in text mode
# mode='at+' - update in text mode
# mode='rb+' - update in binary mode
# mode='wb+' - update in binary mode
# mode='ab+' - update in binary mode



#%% Recap