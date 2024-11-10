
class File:
    AUTOSAVE_SECONDS: float = 1.0
    _content: list[str]
    _timer: Timer
    filename: str

    def __init__(self, filename):
        self.filename = filename
        self._content = list()

    def _set_timer(self):
        if hasattr(self, '_timer'):
            self._timer.cancel()
        self._timer = Timer(self.AUTOSAVE_SECONDS, self._writefile)
        self._timer.start()

    def __enter__(self):
        with open(self.filename, mode='w') as file:
            file.write('')
        self._set_timer()
        return self

    def __exit__(self, *args):
        self._writefile()
        self._timer.cancel()

    def _writefile(self):
        with open(self.filename, mode='a') as file:
            file.writelines(self._content)
        self._content = []
        self._set_timer()

    def append(self, line):
        self._content.append(line+'\n')
