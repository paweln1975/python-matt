class Abspath:
    def __init__(self, func):
        self.func = func

    def __call__(self, filepath):
        abspath = Path(filepath).absolute()
        return self.func(abspath)