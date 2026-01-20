class ChatRoom:
    def __init__(self):
        self.participants = []

    def join(self, participant):
        print(f"{participant.name} joined the chat room.")
        self.participants.append(participant)

    def leave(self, participant):
        print(f"{participant.name} left the chat room.")
        self.participants.remove(participant)

    def broadcast(self, message, sender):
        for participant in self.participants:
            if participant != sender:
                participant.receive(message, sender)

class User:
    def __init__(self, name):
        self.name = name
        self.chat_room = None

    def join_chat(self, chat_room):
        self.chat_room = chat_room
        chat_room.join(self)

    def leave_chat(self):
        if self.chat_room:
            self.chat_room.leave(self)
            self.chat_room = None

    def send(self, message):
        print(f"{self.name} sends: {message}")
        if self.chat_room:
            self.chat_room.broadcast(message, self)

    def receive(self, message, sender):
        print(f"{self.name} receives from {sender.name}: {message}")


if __name__ == "__main__":
    chat_room = ChatRoom()

    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    alice.join_chat(chat_room)
    bob.join_chat(chat_room)
    charlie.join_chat(chat_room)

    alice.send("Hello, everyone!")
    bob.send("Hi Alice!")
    charlie.send("Hey folks, what's up?")

    bob.leave_chat()
    alice.send("Bob has left the chat.")
