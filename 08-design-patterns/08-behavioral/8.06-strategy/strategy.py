from abc import ABC, abstractmethod


class ImageFileCompressor(ABC):
    @abstractmethod
    def compress(self, filename: str) -> None:
        pass


class JpegCompressor(ImageFileCompressor):
    def compress(self, filename: str) -> None:
        print(f"Compressing {filename} using JPEG compression.")

class PngCompressor(ImageFileCompressor):
    def compress(self, filename: str) -> None:
        print(f"Compressing {filename} using PNG compression.")


class ImageFilter(ABC):
    @abstractmethod
    def apply(self, filename: str) -> None:
        pass

class HighContrastFilter(ImageFilter):
    def apply(self, filename: str) -> None:
        print(f"Applying high contrast filter to {filename}.")

class BlackAndWhiteFilter(ImageFilter):
    def apply(self, filename: str) -> None:
        print(f"Applying black and white filter to {filename}.")

class ImageProcessor:
    def __init__(self, compressor: ImageFileCompressor, image_filter: ImageFilter) -> None:
        self.compressor = compressor
        self.image_filter = image_filter

    def process(self, filename: str) -> None:
        self.image_filter.apply(filename)
        self.compressor.compress(filename)

if __name__ == "__main__":
    jpeg_compressor = JpegCompressor()
    high_contrast_filter = HighContrastFilter()

    processor = ImageProcessor(jpeg_compressor, high_contrast_filter)
    processor.process("photo1.jpg")

    png_compressor = PngCompressor()
    bw_filter = BlackAndWhiteFilter()

    processor = ImageProcessor(png_compressor, bw_filter)
    processor.process("photo2.png")
