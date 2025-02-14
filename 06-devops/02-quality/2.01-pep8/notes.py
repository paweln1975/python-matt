#!/usr/bin/env python3
# https://python3.info/devops/quality/pep8.html


# %% Quality PEP-8
# %%



# %% PEP 8 - Style Guide for Python Code
# - PEP8 song https://youtu.be/hgI0p1zf31k
# %%



# %% Tabs or spaces?
# - 4 spacje
# - IDE zamienia tab na 4 spacje
# %%



# %% Line length
# - najbardziej kontrowersyjna klauzula
# - 79 znaków kod
# - 72 znaki docstrings/comments
# - Python standard library is conservative and requires limiting lines to 79 characters (and docstrings/comments to 72)
# - soft wrap
# - co z monitorami 4k?
# - Preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces.
# %%



# %% File encoding
# - UTF-8
# - always remember to open files for reading and writing with encoding='utf-8'
# - All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren't English).
# - String literals and comments must also be in ASCII.
# - Authors whose names are not based on the Latin alphabet (latin-1, ISO/IEC 8859-1 character set) MUST provide a transliteration of their names in this character set.
# %%



# %% Comments
# - Comments that contradict the code are worse than no comments.
# - Comments should be complete sentences.
# - Block comments generally consist of one or more paragraphs built out of complete sentences
# - Each sentence ending in a period.
# - Python coders from non-English speaking countries: please write your comments in English, unless you are 120% sure that the code will never be read by people who don't speak your language.
# - Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).
# %%



# %% Documentation Strings
# - :pep:257 -- Docstring Conventions
# - Write docstrings for all public modules, functions, classes, and methods.
# - Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does.
# - For one liner docstrings, please keep the closing """ on the same line.
# - :pep:257 -- Docstring Conventions: For multiline str always use three double quote (""") characters
# %%



# %% Use better names, rather than comments
# %%



# %% Commented code?
# - NO!
# - Never commit files with commented code
# %%



# %% Author name or revision version
# - Do not put author name or revision version to the files
# - Version Control System is responsible for that
# %%



# %% Naming convention
# %%



# %% Class Attributes
# - Public attributes should have no leading underscores.
# - If your public attribute name collides with a reserved keyword, append a single trailing underscore to your attribute name.
# - cls is the preferred spelling for any variable or argument which is known to be a class, especially the first argument to a class method.
# %%



# %% Methods/Functions
# - Używanie _ w nazwach (snake_case) - // Python - snake ;)
# - method_name() or function_name()
# %%



# %% Modules names
# - modulename
# - module_name
# - Preferable one word
# %%



# %% Function/Method argument names
# - self
# %%



# %% Using __ and _ in names
# - W Pythonie nie ma private/protected/public
# - Funkcje o nazwie zaczynającej się od _ przez konwencję są traktowane jako prywatne
# %%



# %% Single or double quotes?
# - Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowu czy podwójne.
# - Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.
# - Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowu.
# - Z tego powodu w tej książce będziemy trzymać się powyższej konwencji.
# - Ma to znaczenie przy doctest, który zawsze korzysta z pojedynczych i rzuca errorem jak są podwójne
# - :pep:257 -- Docstring Conventions: For multiline str always use three double quote (""") characters
# %%



# %% Trailing Commas
# %%



# %% Indents
# %%



# %% Brackets
# %%



# %% Modules
# - Modules should explicitly declare the names in their public API using the __all__ attribute.
# - Setting __all__ to an empty list indicates that the module has no public API.
# %%



# %% Line continuation
# %%



# %% Blank lines
# - Surround top-level function and class definitions with two blank lines.
# - Method definitions inside a class are surrounded by a single blank line.
# - Extra blank lines may be used (sparingly) to separate groups of related functions.
# - Use blank lines in functions, sparingly, to indicate logical sections.
# %%



# %% Whitespace in function calls
# %%



# %% Whitespace in slices
# %%



# %% Whitespace in assignments
# %%



# %% Whitespace in math operators
# %%



# %% Whitespace in accessors
# %%



# %% Whitespace in functions
# %%



# %% Whitespace in conditionals
# %%



# %% Whitespace in exceptions
# %%



# %% Conditionals
# %%



# %% Negative Conditionals
# %%



# %% Checking if not empty
# %%



# %% Explicit return
# %%



# %% Explicit return value
# %%



# %% Imports
# - Każdy z importów powinien być w osobnej linii
# - importy systemowe na górze
# - importy bibliotek zewnętrznych poniżej systemowych
# - importy własnych modułów poniżej bibliotek zewnętrznych
# - jeżeli jest dużo importów, pomiędzy grupami powinna być linia przerwy
# %%



# %% Whitespace with type annotations
# %%



# %% Magic number i magic string
# - NO!
# %%



# %% PEP 8, but...
# - http://docs.python-requests.org/en/master/dev/contributing/#kenneth-reitz-s-code-style
# %%



# %% Static Code Analysis
# - More information in cicd-tools
# - More information in cicd-pipelines
# %%



# %% pycodestyle
# - Previously known as pep8
# - Python style guide checker.
# - pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8
# - Plugin architecture: Adding new checks is easy
# - Parseable output: Jump to error location in your editor
# - Small: Just one Python file, requires only stdlib
# - Comes with a comprehensive test suite
# %%



