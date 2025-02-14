async def a():
    print('a: before')
    asyncio.sleep(1.0)
    print('a: after')

async def b():
    print('b: before')
    asyncio.sleep(0.5)
    print('b: after')

async def c():
    print('c: before')
    asyncio.sleep(1.5)
    print('c: after')