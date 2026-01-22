from abc import ABC, abstractmethod

class Component:
    def __init__(self, name:str, mediator=None):
        self._mediator = mediator
        self._name = name

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

    def send(self, message):
        if self._mediator:
            self._mediator.notify(self, message)

    def receive(self, message):
        print(f"{self.__class__.__name__} {self._name} received message: {message}")


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: Component, message: str):
        pass

    @abstractmethod
    def register(self, component: Component):
        pass

class ComponentMediator(Mediator):
    def __init__(self):
        self._components: list[Component] = []

    def register(self, component: Component):
        component.mediator = self
        self._components.append(component)

    def notify(self, sender: Component, message: str):
        for component in self._components:
            if component != sender:
                component.receive(message)

if __name__ == "__main__":
    my_mediator = ComponentMediator()

    component1 = Component("Component1")
    component2 = Component("Component2")
    component3 = Component("Component3")

    my_mediator.register(component1)
    my_mediator.register(component2)
    my_mediator.register(component3)

    component1.send("Message from Component 1")
    component2.send("Message from Component 2")