@dataclass
class Date:
    year: int
    month: int
    day: int

    def clone(self):
        return Date(
            year = self.year,
            month = self.month,
            day = self.day)