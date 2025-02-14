def get_files(path: Path):
    yield from path.glob(f'*.py')
    yield from path.glob(f'*.rst')