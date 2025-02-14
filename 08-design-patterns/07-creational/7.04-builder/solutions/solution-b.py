class Email:
    recipient: str
    sender: str
    subject: bytes
    body: bytes

    def with_recipient(self, recipient: str):
        self.recipient = recipient
        return self

    def with_sender(self, sender: str):
        self.sender = sender
        return self

    def with_subject(self, subject):
        self.subject = subject.encode('utf-8')
        return self

    def with_body(self, body):
        self.body = body.encode('utf-8')
        return self