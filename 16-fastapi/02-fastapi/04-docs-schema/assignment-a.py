"""
* Assignment: FastAPI Schema Model
* Complexity: easy
* Lines of code: 15 lines
* Time: 13 min

English:
    1.

Polish:
    1. Stworzyć dwa endpointy: `GET /astronaut` i `POST /astronaut`
    2. Endpoint POST, przyjmuje dane w formacie JSON:
        a) firstname - wymagane
        b) lastname - wymagane
        c) age - opcjonalne
        d) height - opcjonalne
        e) weight - opcjonalne
        f) missions - opcjonalna list[str]
    3. Używając Pydantic Schema (Base Model) zamodeluj dane wejściowe
    4. Zapisz dane do pliku `FILE`
    5. Endpoint GET, odczytuje z pliku i wysyła je użytkownikowi

Hint:
    * Documentation: http://localhost:8000/docs

Tests:
    >>> import sys; sys.tracebacklimit = 0

"""
import json
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel as Schema


app = FastAPI()
FILE = '_temporary.txt'


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)


