
"""
* Assignment: Function Arguments Clean
* Type: homework
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Define function `clean`:
        a. parameter `text: str` (required)
        b. returns `str` with cleaned text
    2. To clean text:
        a. Remove unwanted whitespaces
        b. Remove unwanted special characters
        c. Remove unwanted fragments
        d. Format text
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `clean`:
        a. parametr `text: str` (wymagany)
        b. zwraca `str` z oczyszczonym tekstem
    2. Aby oczyścić tekst:
        a. Usuń niechciane białe znaki
        b. Usuń niechciane znaki specjalne
        c. Usuń niechciane fragmenty
        d. Sformatuj tekst
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert clean is not Ellipsis, \
    'Write solution inside `clean` function'
    >>> assert isfunction(clean), \
    'Object `clean` must be a function'

    >>> clean('ul.Mieszka II')
    'Mieszka II'
    >>> clean('UL. Zygmunta III WaZY')
    'Zygmunta III Wazy'
    >>> clean('  bolesława chrobrego ')
    'Bolesława Chrobrego'
    >>> clean('ul Jana III SobIESkiego')
    'Jana III Sobieskiego'
    >>> clean('\tul. Jana trzeciego Sobieskiego')
    'Jana III Sobieskiego'
    >>> clean('ulica Jana III Sobieskiego')
    'Jana III Sobieskiego'
    >>> clean('ULICA JANA III SOBIESKIEGO  ')
    'Jana III Sobieskiego'
    >>> clean('ULICA JANA III SOBIeskieGO')
    'Jana III Sobieskiego'
    >>> clean(' Jana 3 Sobieskiego  ')
    'Jana III Sobieskiego'
"""

# Define function `clean`:
# - parameter `text: str` (required)
# - returns `str` with cleaned text
#
# To clean text:
# - Remove unwanted whitespaces
# - Remove unwanted special characters
# - Remove unwanted fragments
# - Format text
# type: Callable[[str], str]
def clean(text: str):
    text = text.strip()
    text = text.lower().title()
    prefixes_to_remove = ['Ulica', 'Ul.', 'Ul']
    text_to_replace = {'Trzeciego': 'III',
                       '3': 'III',
                       'Ii': 'II',
                       'IIi': 'III'}
    for prefix in prefixes_to_remove:
        text = text.removeprefix(prefix)
    text = text.strip()
    for t, new_t in text_to_replace.items():
        text = text.replace(t, new_t)

    return text
