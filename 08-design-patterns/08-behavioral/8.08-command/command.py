from abc import ABC, abstractmethod


class Command(ABC):

    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass

class PingCommand(Command):

    def execute(self):
        self.receiver.ping()

class TracerouteCommand(Command):

    def execute(self):
        self.receiver.traceroute()

class NetworkDevice:

    def ping(self):
        print("Pinging the network device...")

    def traceroute(self):
        print("Performing traceroute on the network device...")

class CommandExecutor:

    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()
        self.commands.clear()

if __name__ == "__main__":
    device = NetworkDevice()

    ping_command = PingCommand(device)
    traceroute_command = TracerouteCommand(device)

    executor = CommandExecutor()
    executor.add_command(ping_command)
    executor.add_command(traceroute_command)

    executor.execute_commands()
