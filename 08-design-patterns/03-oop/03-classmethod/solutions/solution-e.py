
class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    @classmethod
    def from_json(cls, data: str):
        values = json.loads(data)
        return cls(**values)


class ScienceFiction(Movie):
    pass

class History(Movie):
    pass

class Adventure(Movie):
    pass
