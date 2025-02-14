def __eq__(self, other):
        return self.__class__ is other.__class__ \
            and self.year == other.year \
            and self.name == other.name