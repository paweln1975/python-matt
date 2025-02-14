def __repr__(self):
        clsname = self.__class__.__name__
        values = tuple(self._dump().values())
        return f'{clsname}{values}'