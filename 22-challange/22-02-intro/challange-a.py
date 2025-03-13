"""
Input Format
A single line containing a positive integer.

Output
Print Weird if the number is weird. Otherwise, print Not Weird.

Given an integer, perform the following conditional actions:

* If n is odd, print Weird
* If n is even and in the inclusive range of 2 to 5, print Not Weird
* If n is even and in the inclusive range of 6 to 20, print Weird
* If n is even and greater than 20, print Not Weird

>>> is_weird(1)
'Weird'

>>> is_weird(11)
'Weird'

>>> is_weird(31)
'Weird'

>>> is_weird(2)
'Not Weird'

>>> is_weird(4)
'Not Weird'

>>> is_weird(6)
'Weird'

>>> is_weird(14)
'Weird'

>>> is_weird(20)
'Weird'

>>> is_weird(26)
'Not Weird'
"""

def is_odd(n: int) -> bool:
    return n % 2 == 1

def is_weird(n: int) -> str:
    weird = True
    if is_odd(n):
        weird = True
    elif not is_odd(n) and 2 <= n <= 5:
        weird = False
    elif not is_odd(n) and 6 <= n <= 20:
        weird = True
    elif not is_odd(n) and n > 20:
        weird = False
    return 'Weird' if weird else 'Not Weird'