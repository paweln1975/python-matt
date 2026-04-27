import re
from dataclasses import dataclass


@dataclass
class Message:
    content: str

class AuthToken:
    pass

class NotificationClient:
    def __init__(self, ip_address: str):
        self.ip_address = ip_address
        NotificationClient.validate_ip(ip_address)

    @staticmethod
    def validate_ip(ip: str) -> bool:
        """
        Validates if the given string is a valid IPv4 address.

        >>> NotificationClient.validate_ip("192.168.1.1")
        True
        >>> NotificationClient.validate_ip("1.256.1.1")
        Traceback (most recent call last):
        ValueError: Invalid IP address: each octet must be between 0 and 255
        >>> NotificationClient.validate_ip("192")
        Traceback (most recent call last):
        ValueError: Invalid IP address format
        >>> NotificationClient.validate_ip("192.1.1.1.1")
        Traceback (most recent call last):
        ValueError: Invalid IP address format
        >>> NotificationClient.validate_ip("0.1.1.1")
        Traceback (most recent call last):
        ValueError: Invalid IP address: first octet must be between 1 and 254
        >>> NotificationClient.validate_ip("255.1.1.1")
        Traceback (most recent call last):
        ValueError: Invalid IP address: first octet must be between 1 and 254
        """
        pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        if not re.match(pattern, ip):
            raise ValueError("Invalid IP address format")
        parts = ip.split('.')
        for i, part in enumerate(parts):
            num = int(part)
            if i == 0:
                if not 1 <= num <= 254:
                    raise ValueError("Invalid IP address: first octet must be between 1 and 254")
            else:
                if not 0 <= num <= 255:
                    raise ValueError("Invalid IP address: each octet must be between 0 and 255")

        return True

    def connect(self, auth_token: AuthToken):
        print(f"Connected to {self.ip_address} with auth token {auth_token}")

    def authenticate(self) -> AuthToken:
        return AuthToken()

    def send(self, message: Message, target: str):
        print(f"Message '{message.content}' sent to {target}")

class NotificationSystem:
    def send_message(self, message: str, target: str):
        print(f"Sending message to {target} ...")
        client = NotificationClient(target)
        token = client.authenticate()
        client.connect(token)

        msg = Message(message)
        client.send(msg, target)

if __name__ == "__main__":
    system = NotificationSystem()
    system.send_message("Hello, World!", "192.168.1.1")
