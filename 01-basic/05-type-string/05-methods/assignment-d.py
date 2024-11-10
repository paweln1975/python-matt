"""
* Assignment: Type Str Normalization
* Type: class assignment
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Expected value is `Pana Twardowskiego III`
    2. Use only `str` methods to clean each variable
    3. Discuss how to create generic solution which fit all cases
    4. Implementation of such generic function will be in
       `Function Arguments Clean` chapter
    5. Run doctests - all must succeed

Polish:
    1. Oczekiwana wartość `Pana Twardowskiego III`
    2. Wykorzystaj tylko metody `str` do oczyszczenia każdej zmiennej
    3. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące
       do wszystkich przypadków
    4. Implementacja takiej generycznej funkcji będzie w rozdziale
       `Function Arguments Clean`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert example is not Ellipsis, \
    'Assign your result to variable `example`'
    >>> assert a is not Ellipsis, \
    'Assign your result to variable `a`'
    >>> assert b is not Ellipsis, \
    'Assign your result to variable `b`'
    >>> assert c is not Ellipsis, \
    'Assign your result to variable `c`'
    >>> assert d is not Ellipsis, \
    'Assign your result to variable `d`'
    >>> assert e is not Ellipsis, \
    'Assign your result to variable `e`'
    >>> assert f is not Ellipsis, \
    'Assign your result to variable `f`'
    >>> assert g is not Ellipsis, \
    'Assign your result to variable `g`'
    >>> assert h is not Ellipsis, \
    'Assign your result to variable `h`'
    >>> assert i is not Ellipsis, \
    'Assign your result to variable `i`'
    >>> assert type(example) is str, \
    'Variable `example` has invalid type, should be str'
    >>> assert type(a) is str, \
    'Variable `a` has invalid type, should be str'
    >>> assert type(b) is str, \
    'Variable `b` has invalid type, should be str'
    >>> assert type(c) is str, \
    'Variable `c` has invalid type, should be str'
    >>> assert type(d) is str, \
    'Variable `d` has invalid type, should be str'
    >>> assert type(e) is str, \
    'Variable `e` has invalid type, should be str'
    >>> assert type(f) is str, \
    'Variable `f` has invalid type, should be str'
    >>> assert type(g) is str, \
    'Variable `g` has invalid type, should be str'
    >>> assert type(h) is str, \
    'Variable `h` has invalid type, should be str'
    >>> assert type(i) is str, \
    'Variable `i` has invalid type, should be str'

    >>> example
    'Pana Twardowskiego III'
    >>> a
    'Pana Twardowskiego III'
    >>> b
    'Pana Twardowskiego III'
    >>> c
    'Pana Twardowskiego III'
    >>> d
    'Pana Twardowskiego III'
    >>> e
    'Pana Twardowskiego III'
    >>> f
    'Pana Twardowskiego III'
    >>> g
    'Pana Twardowskiego III'
    >>> h
    'Pana Twardowskiego III'
    >>> i
    'Pana Twardowskiego III'
"""

EXAMPLE = 'UL. Pana \tTWArdoWskIEGO 3'
A = 'ul Pana TwaRDOWSkiego III'
B = '\tul. Pana Twardowskiego trzeciego'
C = 'ulicaPana Twardowskiego III'
D = 'Pana \nTWARDOWSKIEGO 3'
E = 'UL. Pana TWARDowsKIEGO III'
F = 'ULICA Pana TWARDOWSKIEGO III '
G = 'ULICA. Pana TWARDowsKIEGO III'
H = ' Pana Twardowskiego 3 '
I = 'Pana\tTwardowskiego III '

example = EXAMPLE.upper().replace('UL. ', '').replace('\t', '') \
    .strip().title().replace('3', 'III')

# Expected result: 'Pana Twardowskiego III'
# type: str
a = A.upper().replace("UL", '').strip().replace('III', '3') \
     .title().replace('3', 'III')

# Expected result: 'Pana Twardowskiego III'
# type: str
b = B.upper().replace("\tUL.", '').strip().title() \
     .replace('Trzeciego', 'III')

# Expected result: 'Pana Twardowskiego III'
# type: str
c = C.replace('ulica', '')

# Expected result: 'Pana Twardowskiego III'
# type: str
d = D.upper().replace('III', '3').replace('\n', '') \
     .title().replace('3', 'III')

# Expected result: 'Pana Twardowskiego III'
# type: str

e = E.replace('III', '3').replace('UL. ', '') \
     .title().replace('3', 'III')

# Expected result: 'Pana Twardowskiego III'
# type: str
f = F.replace('III', '3').replace('ULICA ', '') \
     .title().replace('3', 'III').strip()

# Expected result: 'Pana Twardowskiego III'
# type: str
g = G.replace('III', '3').replace('ULICA. ', '') \
     .title().replace('3', 'III').strip()

# Expected result: 'Pana Twardowskiego III'
# type: str
h = H.strip().replace('3', 'III')

# Expected result: 'Pana Twardowskiego III'
# type: str
i = I.replace('\t', ' ').strip()


