def abspath(func):
    def wrapper(filepath):
        abspath = Path(filepath).absolute()
        return func(abspath)
    return wrapper