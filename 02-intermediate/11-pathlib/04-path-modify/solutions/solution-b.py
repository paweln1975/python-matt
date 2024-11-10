
abspath = Path(FILENAME).resolve()

if abspath.is_file():
    result = 'file'
elif abspath.is_dir():
    result = 'directory'
elif not abspath.exists():
    result = 'missing'
