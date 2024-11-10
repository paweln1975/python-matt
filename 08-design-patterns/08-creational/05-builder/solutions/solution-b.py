
class Email:
    recipient: str
    sender: str
    subject: str
    body: str
    attachment: bytes

    def with_recipient(self, recipient):
        self.recipient = recipient
        return self

    def with_sender(self, sender):
        self.sender = sender
        return self

    def with_subject(self, subject):
        self.subject = subject
        return self

    def with_body(self, body):
        self.body = body
        return self

    def with_attachment(self, attachment):
        self.attachment = b64encode(attachment)
        return self
