@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[Group] | None = None

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.groups):
            raise StopIteration
        result = self.groups[self._iter_index]
        self._iter_index += 1
        return result