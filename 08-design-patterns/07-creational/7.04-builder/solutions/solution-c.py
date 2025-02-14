class Email:
    recipient: str
    sender: str
    subject: bytes
    body: bytes

    def with_recipient(self, recipient: str):
        if not re.match(r'^[a-z]+@nasa.gov$', recipient):
            raise ValueError(f'Invalid recipient')
        self.recipient = recipient
        return self

    def with_sender(self, sender: str):
        if not re.match(r'^[a-z]+@nasa.gov$', sender):
            raise ValueError(f'Invalid sender')
        self.sender = sender
        return self

    def with_subject(self, subject):
        self.subject = subject.encode()
        return self

    def with_body(self, body):
        self.body = body.encode()
        return self