from dataclasses import dataclass
from abc import ABC, abstractmethod

class Stream(ABC):
    @abstractmethod
    def write(self, n: int) -> None:
        pass

class CloudStream(Stream):
    def write(self, data: str) -> None:
        print(f"Storing: {data}")

@dataclass
class EncryptedCloudStream(Stream):
    stream: Stream

    def write(self, data: str) -> None:
        encrypted_data = self.encrypt(data)
        self.stream.write(encrypted_data)

    def encrypt(self, data: str) -> str:
        # Simple encryption logic (for demonstration purposes)
        return ''.join(chr(ord(c) + 1) for c in data)

@dataclass
class CompressedCloudStream(Stream):
    stream: Stream

    def write(self, data: str) -> None:
        compressed_data = self.compress(data)
        self.stream.write(compressed_data)

    def compress(self, data: str) -> str:
        # Simple compression logic (for demonstration purposes)
        return data.replace(" ", "")

if __name__ == '__main__':
    cloud_stream = CloudStream()
    encrypted_stream = EncryptedCloudStream(cloud_stream)
    compressed_encrypted_stream = CompressedCloudStream(encrypted_stream)
    compressed_encrypted_stream.write("Hello, World!")