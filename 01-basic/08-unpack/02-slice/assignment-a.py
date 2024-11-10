"""
* Assignment: Unpack Slice Text
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Define variables:
        a. `result_a: str` with text 'Mark Watney' sliced from `DATA_A`
        b. `result_b: str` with text 'Melissa Lewis' sliced from `DATA_B`
        c. `result_c: str` with text 'Rick Martinez' sliced from `DATA_C`
        d. `result_d: str` with text 'Alex Vogel' sliced from `DATA_D`
        e. `result_e: str` with text 'Beth Johanssen' sliced from `DATA_E`
        f. `result_f: str` with text 'Chris Beck' sliced from `DATA_F`
    2. Use slice to remove title and military rank
    3. Remove also whitespaces at the beginning and end of a text
    4. Use only `slice` to clean text, do not use string methods
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne:
        a. `result_a: str` z tekstem 'Mark Watney' wyciętym z `DATA_A`
        b. `result_b: str` z tekstem 'Melissa Lewis' wyciętym z `DATA_B`
        c. `result_c: str` z tekstem 'Rick Martinez' wyciętym z `DATA_C`
        d. `result_d: str` z tekstem 'Alex Vogel' wyciętym z `DATA_D`
        e. `result_e: str` z tekstem 'Beth Johanssen' wyciętym z `DATA_E`
        f. `result_f: str` z tekstem 'Chris Beck' wyciętym z `DATA_F`
    2. Użyj slice do usunięcia tytułu naukowego i stopnia wojskowego
    3. Usuń również białe znaki na początku i końcu tekstu
    4. Użyj tylko `slice` do oczyszczenia tekstu, nie używaj metod stringa
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert type(result_a) is str, \
    'Variable `result_a` has invalid type, should be str'

    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'
    >>> assert type(result_b) is str, \
    'Variable `result_b` has invalid type, should be str'

    >>> assert result_c is not Ellipsis, \
    'Assign your result to variable `result_c`'
    >>> assert type(result_c) is str, \
    'Variable `result_c` has invalid type, should be str'

    >>> assert result_d is not Ellipsis, \
    'Assign your result to variable `result_d`'
    >>> assert type(result_d) is str, \
    'Variable `result_d` has invalid type, should be str'

    >>> assert result_e is not Ellipsis, \
    'Assign your result to variable `result_e`'
    >>> assert type(result_e) is str, \
    'Variable `result_e` has invalid type, should be str'

    >>> assert result_f is not Ellipsis, \
    'Assign your result to variable `result_f`'
    >>> assert type(result_f) is str, \
    'Variable `result_f` has invalid type, should be str'

    >>> result_a
    'Mark Watney'
    >>> result_b
    'Melissa Lewis'
    >>> result_c
    'Rick Martinez'
    >>> result_d
    'Alex Vogel'
    >>> result_e
    'Beth Johanssen'
    >>> result_f
    'Chris Beck'
"""

EXAMPLE = 'lt. Mark Watney, PhD'
example = EXAMPLE[4:-5]


DATA_A = 'prof. Mark Watney'
DATA_B = 'Melissa Lewis, PhD'
DATA_C = 'lt. col. Rick Martinez'
DATA_D = 'dr Alex Vogel'
DATA_E = 'Beth Johanssen\t'
DATA_F = 'dr Chris Beck, MD-PhD'



# Use slice to remove title and military rank
# Leave only name and surname: 'Mark Watney'
# type: str
result_a = DATA_A[6:]

# Use slice to remove title and military rank
# Leave only name and surname: 'Melissa Lewis'
# type: str
result_b = DATA_B[:-5]

# Use slice to remove title and military rank
# Leave only name and surname: 'Rick Martinez'
# type: str
result_c = DATA_C[9:]

# Use slice to remove title and military rank
# Leave only name and surname: 'Alex Vogel'
# type: str
result_d = DATA_D[3:]

# Use slice to remove title and military rank
# Leave only name and surname: 'Beth Johanssen'
# type: str
result_e = DATA_E[:-1]

# Use slice to remove title and military rank
# Leave only name and surname: 'Chris Beck'
# type: str
result_f = DATA_F[3:13]


