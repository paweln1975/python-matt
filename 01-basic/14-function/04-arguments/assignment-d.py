
"""
* Assignment: Function Arguments Translate
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Define function `translate`:
        a. parameter `text: str` (required)
        b. return `str` with translated text
    2. If letter is in `PL` then substitute letter,
       otherwise take original letter
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `translate`:
        a. parametr `text: str` (wymagany)
        b. zwróć `str` z przetłumaczonym tekstem
    2. Jeżeli litera jest w `PL` to podmień literę,
        w przeciwnym przypadku to weź oryginalną literę
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert translate is not Ellipsis, \
    'Write solution inside `translate` function'
    >>> assert isfunction(translate), \
    'Object `translate` must be a function'

    >>> translate('zażółć')
    'zazolc'
    >>> translate('gęślą')
    'gesla'
    >>> translate('jaźń')
    'jazn'
    >>> translate('zażółć gęślą jaźń')
    'zazolc gesla jazn'
"""

PL = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}

# Define function `translate`:
# - parameter `text: str` (required)
# - return `str` with translated text
# If letter is in `PL` then substitute letter,
# otherwise take original letter
# type: Callable[[str], str]
def translate(text):
    return ''.join(PL.get(letter, letter) for letter in text)


