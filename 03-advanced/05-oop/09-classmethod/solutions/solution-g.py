
class Timezone:
    dt: datetime
    tzname: str

    def __init__(self, dt):
        self.dt = dt

    @classmethod
    def from_timestamp(cls, timestamp: int):
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        return cls(dt)


class CET(Timezone):
    tzname = 'Central European Time'


class CEST(Timezone):
    tzname = 'Central European Summer Time'
