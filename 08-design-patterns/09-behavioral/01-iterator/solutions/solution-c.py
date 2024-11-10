
@dataclass
class Range:
    start: int
    stop: int
    step: int = 1
    _current: int = 0

    def __iter__(self):
        self._current = self.start
        return self

    def __next__(self):
        if self._current >= self.stop:
            raise StopIteration
        result = self._current
        self._current += self.step
        return result
