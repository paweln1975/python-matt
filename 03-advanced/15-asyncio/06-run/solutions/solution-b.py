
async def run(name, sleep):
    await asyncio.sleep(sleep)
    return f'{name}'

async def main():
    return await asyncio.gather(
        run(name='a', sleep=1.0),
        run(name='b', sleep=0.5),
        run(name='c', sleep=1.5),
    )
