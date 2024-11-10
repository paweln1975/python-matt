
class Timezone:
    dt: datetime
    tzname: str

    def __init__(self, dt):
        self.dt = dt

    @classmethod
    def from_timestamp(cls, data: int):
        dt = datetime.fromtimestamp(data, tz=timezone.utc)
        return cls(dt)


class CET(Timezone):
    tzname = 'Central European Time'


class CEST(Timezone):
    tzname = 'Central European Summer Time'
