from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, request) -> bool:
        pass

    def process_request(self, request) -> bool:
        handled = self.handle(request)
        if handled and self._successor:
            return self._successor.process_request(request)
        return False

class AuthHandler(Handler):
    def handle(self, request) -> bool:
        if 'auth' in request and request['auth'] == 'valid_token':
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False

class LoggerHandler(Handler):
    def handle(self, request) -> bool:
        print(f"Logging request: {request}")
        return True

class CompressorHandler(Handler):
    def handle(self, request) -> bool:
        if 'data' in request:
            original_size = len(request['data'])
            request['data'] = f"compressed({request['data']})"
            compressed_size = len(request['data'])
            print(f"Compressed data from {original_size} to {compressed_size} bytes.")
            return True
        else:
            print("No data to compress.")
        return False

@dataclass
class Server:
    handler : Handler

    def process_request(self, request) -> bool:
        return self.handler.process_request(request)

if __name__ == "__main__":
    compressor = CompressorHandler()
    logger = LoggerHandler(successor=compressor)
    auth = AuthHandler(successor=logger)

    server = Server(handler=auth)

    request1 = {'auth': 'valid_token', 'data': 'This is some important data.'}
    print("Processing Request 1:")
    server.process_request(request1)

    print("\nProcessing Request 2:")
    request2 = {'auth': 'invalid_token', 'data': 'This is some important data.'}
    server.process_request(request2)

    print("\nProcessing Request 3:")
    request3 = {'auth': 'valid_token'}
    server.process_request(request3)
