
class DateTime:
    tzname: str

    def __init__(self, year, month, day, hour, minute, second, tzinfo):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.tzinfo = tzinfo

    @classmethod
    def from_datetime(cls, dt: datetime):
        year = dt.year
        month = dt.month
        day = dt.day
        hour = dt.hour
        minute = dt.minute
        second = dt.second
        tzinfo = ZoneInfo(cls.tzname)
        return cls(year, month, day, hour, minute, second, tzinfo)


class UTC(DateTime):
    tzname = 'Etc/UTC'


class CET(DateTime):
    tzname = 'Etc/GMT-1'


class CEST(DateTime):
    tzname = 'Etc/GMT-2'
