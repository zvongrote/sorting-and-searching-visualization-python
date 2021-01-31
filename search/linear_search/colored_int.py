from colorama import Fore


class ColoredInt:
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
