"""
>>> sys.tracebacklimit = 0

>>> assert sys.version_info > (3, 12, 0), \
'Python 3.12+ is required'

>>> assert 'VIRTUAL_ENV' in os.environ, \
'Please make sure you are using venv environment.'
"""

import os
import sys
import importlib
import re


print(f'Venv:', 'VIRTUAL_ENV' in os.environ)
print(f'Python:', sys.version[:6])

module_name = re.compile(r'^[\w_\-]+')

with open('requirements.txt') as file:
    for line in file:
        modname = r.group() if (r := module_name.search(line)) else None
        if not modname:
            continue
        try:
            module = importlib.import_module(modname)
        except Exception as err:
            print(f'{modname}: {err.__class__.__name__}')
        else:
            version = getattr(module, '__version__', 'unknown')
            print(f'{modname}: {version}')
