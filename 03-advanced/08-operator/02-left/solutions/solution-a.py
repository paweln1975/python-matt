
@dataclass
class Position:
    x: int = 0
    y: int = 0

    def __matmul__(self, other: tuple[int, int]) -> None:
        self.x = other[0]
        self.y = other[1]

    #%% Alternative Solution
    def __matmul__(self, other: tuple[int, int]) -> None:
        self.x, self.y = other
