async def a():
    print('a: before')
    await asyncio.sleep(1.0)
    print('a: after')

async def b():
    print('b: before')
    await asyncio.sleep(0.5)
    print('b: after')

async def c():
    print('c: before')
    await asyncio.sleep(1.5)
    print('c: after')