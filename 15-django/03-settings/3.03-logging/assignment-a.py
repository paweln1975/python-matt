"""
Name: Django Settings LOGGING
Difficulty: easy
Lines: 15
Minutes: 3

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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

Hints:
'django.db': {'handlers': ['console'], 'level': 'DEBUG'}

"""

# %% SetUp

# English
# 0. Use `myproject.myproject`
# 1. Modify the file: `myproject/settings.py`
# 2. Set `LOGGING` to display in the console all SQL queries
# 3. Run doctests - all must succeed

# Polish
# 0. Użyj `myproject.myproject`
# 1. Zmodyfikuj plik: `myproject/settings.py`
# 2. Ustaw `LOGGING` aby wyświetlał w konsoli wszystkie zapytania SQL
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    },
}