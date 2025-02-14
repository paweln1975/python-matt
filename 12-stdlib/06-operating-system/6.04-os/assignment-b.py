"""
Name: Tree
Difficulty: hard
Lines: 60
Minutes: 21

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result  # doctest: +SKIP
root:.
[.]
┣━[.idea]
┃  ┣━[scopes]
┃  ┃  ┗━scope_settings.xml
┃  ┣━.name
┃  ┣━demo.iml
┃  ┣━encodings.xml
┃  ┣━misc.xml
┃  ┣━modules.xml
┃  ┣━vcs.xml
┃  ┗━workspace.xml
┣━[test1]
┃  ┗━test1.txt
┣━[test2]
┃  ┣━[test2-2]
┃  ┃  ┗━[test2-3]
┃  ┃      ┣━test2
┃  ┃      ┗━test2-3-1
┃  ┗━test2
┣━folder_tree_maker.py
┗━tree.py

"""

# %% SetUp

result: str

# English
# 1. Using unicode characters: "┣━", "┗━" , "┃  "
# 2. Generate output similar to `tree` command.
# 3. Run doctests - all must succeed

# Polish
# 1. Za pomocą znaków unicode: "┣━", "┗━" , "┃  "
# 2. Wygeneruj wynik przypominający wynik polecenia `tree`.
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...