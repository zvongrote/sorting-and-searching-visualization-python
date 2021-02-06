from colorama import Fore
from time import sleep


def change_color_in_range(data, start, stop, color):
    """Changes the colors of all the numbers within the given range of the list.
    
    Parameters
    ----------
    data: list[ColoredInt]
        The list containing the numbers
    start: int
        Index of the first item (inclusive)
    stop: int
        Index of the last item (exclusive)
    """

    for i in range(start, stop):
        data[i].color = color


def swap(data, index1, index2):
    """Swaps two elements in a list.

    Parameters
    ----------
    data: list[Object]
        The list containing the items
    index1: int
        Index of the first item
    index2: int
        Index of the second item
    """

    data[index1], data[index2] = data[index2], data[index1]


def print_underlined(string):
    """Prints an underlined version of a string.

    For example:
        This is a test string
        ---------------------

    Parameter
    ---------
    string: str
        The string to print
    """

    print(string)
    print('-' * len(string))


def change_to_swapped_colors(data, index1, index2):
    """Changes the colors of the two integers being swapped.
    
    Parameters
    ----------
    data: list[ColoredInts]
        The list containing the numbers
    index1: int
        The index of the first item, changes the color to YELLOW
    index2: int
        The index of the second item, changes the color to BLUE
    """

    data[index1].color = Fore.YELLOW
    data[index2].color = Fore.BLUE


def visual_swap(data, index1, index2, delay):
    """Swaps two numbers in the list with visualization.

    1) Change the numbers' color to different colors
    2) Show the numbers in their original positions
    3) Swap the numbers
    4) Show the numbers in their new positions

    Parameters
    ----------
    data: list[ColoredInt]
        The list containing numbers to swap
    index1: int
        The index of the first item
    index2: int
        The index of the second item
    delay: float
        The time to sleep in between steps of the visualization
    """

    change_to_swapped_colors(data, index1, index2)
    print(data, end='\r')
    sleep(delay)
    swap(data, index1, index2)
    print(data, end='\r')
    sleep(delay)
