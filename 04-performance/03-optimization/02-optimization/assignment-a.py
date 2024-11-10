"""
* Assignment: Memoization
* Complexity: medium
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Create empty `dict` named `CACHE`
    2. In the dictionary, we will store the results of calculating
       the function for the given parameters:
        a. key: function argument
        b. value: calculation result
    3. Modify function `factorialA(n: int)`
    4. Before running the function, check if the result has already
       been calculated:
        a. if so, return data from `CACHE`
        b. if not, calculate, update `CACHE` and return the value
    5. Compare the speed of operation
    6. Run doctests - all must succeed

Polish:
    1. Stwórz pusty `dict` o nazwie `CACHE`
    2. W słowniku będziemy przechowywali wyniki wyliczenia funkcji
       dla zadanych parametrów:
        a. klucz: argument funkcji
        b. wartość: wynik obliczeń
    3. Zmodyfikuj funkcję `factorialA(n: int)`
    4. Przed uruchomieniem funkcji, sprawdź czy wynik został już
       wcześniej obliczony:
        a. jeżeli tak, to zwraca dane z `CACHE`
        b. jeżeli nie, to oblicza, aktualizuje `CACHE` i zwraca wartość
    5. Porównaj prędkość działania
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
   
"""

from timeit import timeit
import sys
sys.setrecursionlimit(5000)


def factorialA(n: int) -> int:
    return 1 if n==0 else n*factorialA(n-1)


# Do not modify anything below
def factorialB(n: int) -> int:
    return 1 if n==0 else n*factorialB(n-1)


durationA = timeit(
    stmt='factorialA(500); factorialA(400); factorialA(450); factorialA(350)',
    globals=globals(),
    number=10000,
)

durationB = timeit(
    stmt='factorialB(500); factorialB(400); factorialB(450); factorialB(350)',
    globals=globals(),
    number=10000
)

times_faster = durationB / durationA
print(f'factorialA time: {durationA:.4f} seconds')
print(f'factorialB time: {durationB:.4f} seconds')
print(f'Cached solution is {times_faster:.0f} times faster')



