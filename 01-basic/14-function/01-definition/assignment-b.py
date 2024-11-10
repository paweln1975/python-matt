"""
* Assignment: Function Definition Call
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Call function `run` three times
    2. Run doctests - all must succeed

Polish:
    1. Wywołaj funkcję `run` trzy razy
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(run), \
    'Object `run` must be a function'

    >>> content = open(__file__).read()
    >>> content.count('run'+'()') - 1
    3
"""

def run():
    print('Beetlejuice')


# Call function `run` three times
# type: None
run()
run()
run()



