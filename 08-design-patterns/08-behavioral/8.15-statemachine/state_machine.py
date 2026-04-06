from abc import ABC, abstractmethod

class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class RedLightState(TrafficLightState):
    def handle(self, context: TrafficLight):
        print("Traffic light is RED. STOP")
        context.set_state(GreenLightState())

class GreenLightState(TrafficLightState):
    def handle(self, context: TrafficLight):
        print("Traffic light is GREEN. Go!")
        context.set_state(YellowLightState())

class YellowLightState(TrafficLightState):
    def handle(self, context: TrafficLight):
        print("Traffic light is YELLOW. Prepare to stop.")
        context.set_state(RedLightState())

class TrafficLight:
    def __init__(self):
        self._state = RedLightState()

    def set_state(self, state):
        self._state = state

    def change_state(self):
        self._state.handle(self)

if __name__ == "__main__":
    traffic_light = TrafficLight()

    for _ in range(6):
        traffic_light.change_state()



