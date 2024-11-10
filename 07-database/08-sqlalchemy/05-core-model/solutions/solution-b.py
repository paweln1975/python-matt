
from dataclasses import dataclass


@dataclass
class Astronaut:
    name: str
    country: str
    date: str


@dataclass
class SpaceAgency:
    name: str
    country: str
    date: str


watney = Astronaut('Watney', 'USA', '1969-07-21')
nasa = SpaceAgency('NASA', 'USA', '1958-07-29')
