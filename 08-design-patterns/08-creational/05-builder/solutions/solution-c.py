
class Texture:
    file: str
    width: int
    height: int
    quality: int

    def with_file(self, file):
        self.file = file
        return self

    def with_width(self, width):
        if width < 0:
            raise ValueError
        self.width = width
        return self

    def with_height(self, height):
        if height < 0:
            raise ValueError
        self.height = height
        return self

    def with_quality(self, quality):
        if not 1 <= quality < 100:
            raise ValueError
        self.quality = quality
        return self
