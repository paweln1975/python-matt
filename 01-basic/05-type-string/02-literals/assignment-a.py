"""
* Assignment: Type Str Unicode
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: str` with text: 'Hello 😀'
    2. Unicode codepoint for smiley emoticon (😀) is '\U0001F600'
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z tekstem: 'Hello 😀'
    2. Kod znaku emotikony uśmieszek (😀) to '\U0001F600'
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> '😀' in result
    True
    >>> result
    'Hello 😀'
"""

# Define `result: str` with text: 'Hello 😀'
# Unicode codepoint for smiley emoticon (😀) is '\U0001F600'
# type: str
result = 'Hello ' + '\U0001F600'

