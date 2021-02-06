from colorama import Fore
from time import sleep


def change_color_in_range(list, min, max, color):
    for i in range(min, max):
        list[i].color = Fore.RED


def swap(list, index1, index2):
    """ Swaps two elements in a list """

    list[index1], list[index2] = list[index2], list[index1]


def print_underlined(str):
    """
    Prints an underlined version of a string. For example:

    This is a test string
    ---------------------
    """

    print(str)
    print('-' * len(str))


def change_to_swapped_colors(list, index1, index2):
    """ Changes the colors of the two integers being swapped """

    list[index1].color = Fore.YELLOW
    list[index2].color = Fore.BLUE


def swap_operation(list, index1, index2, delay):
    """
    Swaps two numbers in the list with visualization.
    1) Change the numbers' color to different colors
    2) Show the numbers in their original positions
    3) Swap the numbers
    4) Show the numbers in their new positions
    """

    change_to_swapped_colors(list, index1, index2)
    print(list, end='\r')
    sleep(delay)
    swap(list, index1, index2)
    print(list, end='\r')
    sleep(delay)
