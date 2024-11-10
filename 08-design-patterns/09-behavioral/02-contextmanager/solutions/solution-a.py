
class File:
    filename: str
    buffer: list[str]

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.buffer = []

    def append(self, line: str) -> None:
        self.buffer.append(line + '\n')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        with open(self.filename, mode='w') as file:
            file.writelines(self.buffer)
