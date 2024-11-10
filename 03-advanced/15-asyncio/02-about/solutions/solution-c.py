
async def a():
    print('a: before')
    await asyncio.sleep(1.0)
    print('a: after')
    return 'a'

async def b():
    print('b: before')
    await asyncio.sleep(0.5)
    print('b: after')
    return 'b'

async def c():
    print('c: before')
    await asyncio.sleep(1.5)
    print('c: after')
    return 'c'
