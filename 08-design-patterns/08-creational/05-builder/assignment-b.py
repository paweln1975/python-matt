"""
* Assignment: DesignPatterns Creational BuilderEmail
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create class `Email`
    2. Use builder pattern to set:
        a. `recipient: str` verify email address using regex
        b. `sender: str` verify email address using regex
        c. `subject: str` encode to bytes
        d. `body: str` encode to bytes
        e. `attachment: bytes` base64 encoded
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Email`
    2. Użyj wzorca builder, aby ustawić:
         a. `recipient: str` zweryfikuj adres e-mail za pomocą wyrażenia regularnego
         b. `sender: str` zweryfikuj adres e-mail za pomocą wyrażenia regularnego
         c. `subject: str` koduje do bajtów
         d. `body: str` koduje na bajty
         e. `attachment: bytes` zakodowane w standardzie base64
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = (
    ...     Email()
    ...     .with_recipient('mwatney@nasa.gov')
    ...     .with_sender('mlewis@nasa.gov')
    ...     .with_subject('Hello from Mars')
    ...     .with_body('Greetings from Red Planet')
    ...     .with_attachment('myfile.txt'.encode())
    ... )

    >>> pprint(vars(result), width=72, sort_dicts=False)
    {'recipient': 'mwatney@nasa.gov',
     'sender': 'mlewis@nasa.gov',
     'subject': 'Hello from Mars',
     'body': 'Greetings from Red Planet',
     'attachment': b'bXlmaWxlLnR4dA=='}
"""
from base64 import b64encode


class Email:
    recipient: str
    sender: str
    subject: str
    body: str
    attachment: bytes

    def with_recipient(self, recipient: str):
        self.recipient = recipient
        return self

    def with_sender(self, sender: str):
        self.sender = sender
        return self

    def with_subject(self, subject: str):
        self.subject = subject
        return self

    def with_body(self, body: str):
        self.body = body
        return self


