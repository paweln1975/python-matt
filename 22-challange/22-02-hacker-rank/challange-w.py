#!/bin/python3

import math
import os
import random
import re
import sys

"""
Processes a list of names and email addresses, filtering and sorting Gmail users.

This function reads input from the user, filters out names associated with Gmail
addresses, sorts them alphabetically, and prints the result.

Input:
    The function takes no parameters but reads input from the user:
    - First line: An integer N, representing the number of entries.
    - Next N lines: Each line contains a space-separated pair of strings:
      firstName and emailID.

Returns:
    None. The function prints the sorted list of names directly.

Local Variables:
    N (int): The number of entries to process.
    tab (list): A list to store names associated with Gmail addresses.
    first_multiple_input (list): Temporary list to store each input line split into parts.
    firstName (str): The first name from each input line.
    emailID (str): The email address from each input line.

Behavior:
    1. Reads the number of entries (N) from user input.
    2. Iterates N times, each time reading a name and email address.
    3. If the email address ends with '@gmail.com', the name is added to 'tab'.
    4. After processing all inputs, sorts the 'tab' list alphabetically.
    5. Prints each name in the sorted 'tab' list on a new line.

Note:
    - The function assumes valid input format and does not include error handling.
    - Email filtering is case-sensitive and only matches exact '@gmail.com' endings.
    - The sorting is based on Python's default string sorting, which is alphabetical.
"""
def execute():
    
    N = int(input().strip())
    tab = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if emailID.endswith('@gmail.com'):
            tab.append(firstName)

    tab.sort()
    for name in tab:
        print(name)

if __name__ == '__main__':
    execute()
