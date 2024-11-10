
class Abspath:
    def __init__(self, func):
        self.func = func

    def __call__(self, relpath):
        abspath = Path(relpath).absolute()
        return self.func(abspath)
