
class Abspath:
    def __init__(self, func):
        self._func = func

    def __call__(self, file):
        abspath = Path(file).absolute()
        return self._func(abspath)
