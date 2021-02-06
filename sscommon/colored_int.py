from colorama import Fore


class ColoredInt:
    """
    A wrapper class that can print an integer to the console with color.

    Attributes
    ----------
    value: int
        The integer value
    color: colorama.Fore
        The color of the integer text. Use a constant from colorama.Fore.COLOR
    """

    def __init__(self, value, color=Fore.RESET):
        self.value = value
        self.color = color

    def __str__(self):
        return self.color + str(self.value) + Fore.RESET

    def __repr__(self):
        return self.color + str(self.value) + Fore.RESET

    def __eq__(self, o):
        if isinstance(o, ColoredInt):
            return self.value == o.value
        elif isinstance(o, int):
            return self.value == o

    def __gt__(self, other):
        if isinstance(other, ColoredInt):
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other
        else:
            raise TypeError(f"Can't use > with {type(other)}")

    def __lt__(self, other):
        if isinstance(other, ColoredInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            raise TypeError(f"Can use < with {type(other)}")

    def __eq__(self, o):
        if isinstance(o, ColoredInt):
            return self.value == o.value
        elif isinstance(o, int):
            return self.value == o

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise TypeError('The value must be of type "int"')
        self._value = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color
