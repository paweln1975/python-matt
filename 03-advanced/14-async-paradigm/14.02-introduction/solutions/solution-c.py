async def a():
    print('a: before')
    time.sleep(1.0)
    print('a: after')

async def b():
    print('b: before')
    time.sleep(0.5)
    print('b: after')

async def c():
    print('c: before')
    time.sleep(1.5)
    print('c: after')