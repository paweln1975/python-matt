"""
Name: FastAPI Schema Model
Difficulty: easy
Lines: 15
Minutes: 13

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

Hints:
Documentation: http://localhost:8000/docs

"""

# %% SetUp

import json
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel as Schema

app = FastAPI()
FILE = '_temporary.txt'

# English

# Polish
# 1. Stworzyć dwa endpointy: `GET /astronaut` i `POST /astronaut`
# 2. Endpoint POST, przyjmuje dane w formacie JSON:
#    - firstname - wymagane
#    - lastname - wymagane
#    - age - opcjonalne
#    - height - opcjonalne
#    - weight - opcjonalne
#    - missions - opcjonalna list[str]
# 3. Używając Pydantic Schema (Base Model) zamodeluj dane wejściowe
# 4. Zapisz dane do pliku `FILE`
# 5. Endpoint GET, odczytuje z pliku i wysyła je użytkownikowi

# %% Result
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)