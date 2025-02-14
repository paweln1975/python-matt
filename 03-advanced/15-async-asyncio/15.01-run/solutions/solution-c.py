async def check(url):
    resp = await fetch(url)
    license = 'Matt Harasymczuk' in resp.text
    return {'url': url, 'license': license}

async def main():
    todo = [check(url) for url in DATA]
    return await asyncio.gather(*todo)