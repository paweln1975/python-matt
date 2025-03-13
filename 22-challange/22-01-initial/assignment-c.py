class Celsius:
    """A class to represent temperatures in Celsius."""

    def __init__(self, temperature=0):
        """Initializes the Celsius object with a default temperature of 0."""
        self.temperature = float(temperature)  # Store as float for flexibility

    @property
    def temperature(self):
        """Returns the current temperature in Celsius."""
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        """Sets the temperature in Celsius.

        Args:
            value: The temperature value to set.
        """
        self._temperature = float(value) #ensure it is a float.

    def to_fahrenheit(self):
        """Converts the Celsius temperature to Fahrenheit.

        Returns:
            The temperature in Fahrenheit.
        """
        return (self._temperature * 9 / 5) + 32

c = Celsius(37)
c.temperature = 10
print(c.temperature)
print(c.to_fahrenheit())