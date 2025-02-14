async def worker(name, sleep):
    await asyncio.sleep(sleep)
    return f'{name}'

async def main():
    return await asyncio.gather(
        worker(name='a', sleep=1.0),
        worker(name='b', sleep=0.5),
        worker(name='c', sleep=1.5),
    )