class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_tuple(cls, data: tuple[str,str]):
        title = data[0]
        author = data[1]
        return cls(title, author)


class ScienceFiction(Book):
    pass

class History(Book):
    pass

class Adventure(Book):
    pass