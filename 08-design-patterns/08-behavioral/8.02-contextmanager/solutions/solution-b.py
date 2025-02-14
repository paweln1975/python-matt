class File:
    BUFFER_LIMIT: int = 100
    filename: str
    buffer: list[str]

    def __init__(self, filename):
        self.filename = filename
        self.buffer = []

    def append(self, line: str):
        to_append = line + '\n'
        if getsizeof(to_append) >= self.BUFFER_LIMIT:
            raise BufferError('Cannot fit data into buffer (even empty)')
        if getsizeof(self.buffer) + getsizeof(to_append) >= self.BUFFER_LIMIT:
            self.write(mode='a')
        self.buffer.append(to_append)

    def write(self, mode):
        to_write, self.buffer = self.buffer, []
        with open(self.filename, mode=mode) as file:
            file.writelines(to_write)

    def __enter__(self):
        self.write(mode='w')
        return self

    def __exit__(self, *args):
        self.write(mode='a')