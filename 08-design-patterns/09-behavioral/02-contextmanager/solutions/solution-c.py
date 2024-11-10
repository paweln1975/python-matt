
class File:
    filename: str
    buffer: list[str]
    timer: Timer
    AUTOSAVE_SECONDS: float = 1.0

    def __init__(self, filename):
        self.filename = filename
        self.buffer = []

    def append(self, line):
        self.buffer.append(line + '\n')

    def write(self, mode='a'):
        to_write = self.buffer.copy()
        self.buffer = []
        with open(self.filename, mode=mode) as file:
            file.writelines(to_write)
        self.set_timer()

    def set_timer(self):
        if hasattr(self, 'timer'):
            self.timer.cancel()
        self.timer = Timer(self.AUTOSAVE_SECONDS, self.write)
        self.timer.start()

    def __enter__(self):
        self.write(mode='w')
        return self

    def __exit__(self, *args):
        self.write()
        self.timer.cancel()
