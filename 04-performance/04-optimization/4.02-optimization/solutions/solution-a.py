CACHE = {}

def factorialA(n: int) -> int:
    if n not in CACHE:
        CACHE[n] = 1 if n==0 else n*factorialA(n-1)
    return CACHE[n]


# Do not modify anything below
def factorialB(n: int) -> int:
    return 1 if n==0 else n*factorialB(n-1)


durationA = timeit(
    stmt='factorialA(50); factorialA(40); factorialA(45); factorialA(35)',
    globals=globals(),
    number=10000,
)

durationB = timeit(
    stmt='factorialB(50); factorialB(40); factorialB(45); factorialB(35)',
    globals=globals(),
    number=10000,
)

times_faster = durationB / durationA
print(f'factorialA time: {durationA:.4f} seconds')
print(f'factorialB time: {durationB:.4f} seconds')
print(f'Cached solution is {times_faster:.0f} times faster')
# factorialA time: 0.0014 seconds
# factorialB time: 0.0643 seconds
# Cached solution is 45 times faster

# Decorator
CACHE_DECORATOR = {}

def cache(func):
    def wrapper(n):
        if n not in CACHE_DECORATOR:
            CACHE_DECORATOR[n] = func(n)
        return CACHE_DECORATOR[n]
    return wrapper

@cache
def factorialC(n: int) -> int:
    return 1 if n==0 else n*factorialC(n-1)


durationC = timeit(
    stmt='factorialC(50); factorialC(40); factorialC(45); factorialC(35)',
    globals=globals(),
    number=10000,
)

print(f'factorialC time: {durationC:.4f} seconds')
# factorialC time: 0.0015 seconds