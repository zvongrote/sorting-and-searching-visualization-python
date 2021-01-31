from colorama import Fore


class ColoredInt:
    def __init__(self, value, color=Fore.RESET):
        self.value = value
        self.color = color

    def __str__(self):
        return self.color + str(self.value) + Fore.RESET

    def __repr__(self):
        return self.color + str(self.value) + Fore.RESET

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

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
