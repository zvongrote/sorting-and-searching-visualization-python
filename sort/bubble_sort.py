"""Bubble Sort Visualizer

This script creates a random list of integers and sorts it using bubble sort.
Each step of the algorithm is shown by coloring the numbers in the list and displaying it to the console.
"""

from random import randint
from time import sleep

from colorama import Fore
from colorama import init as color_init

from sscommon.colored_int import ColoredInt
from sscommon.util import list_of_random_colored_ints, print_list_with_delay, print_underlined, visual_swap

# Options
SORT_ORDER = "asc"          # "asc" for ascending, or "desc" for descending
SPEED = 2                   # The higher the number, the faster the sorting animation
PRINT_DELAY = 1 / SPEED
SWAP_DELAY = 1 * PRINT_DELAY
LIST_SIZE = 10
MIN_VALUE = -100
MAX_VALUE = 100

# Initialize colorama
color_init(autoreset=True)

# Create a list of random colored integers
numbers = list_of_random_colored_ints(LIST_SIZE, MIN_VALUE, MAX_VALUE)

# Show the unsorted array
print()
print_underlined("Unsorted numbers")
print(numbers, '\n')

# Bubble sort the list
print_underlined("Sorted")
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        # Change the colors of the numbers being compared to red
        numbers[j].color = Fore.RED
        numbers[j + 1].color = Fore.RED

        # Print and pause for a certain time based on the SPEED value
        print_list_with_delay(numbers, PRINT_DELAY)

        # Swap values based on sorting order. Defaults to ascending
        if SORT_ORDER == "desc":
            if numbers[j] < numbers[j + 1]:
                visual_swap(numbers, j, j + 1, SWAP_DELAY)
        else:
            if numbers[j] > numbers[j + 1]:
                visual_swap(numbers, j, j + 1, SWAP_DELAY)

        # Reset the colors
        numbers[j].color = Fore.RESET
        numbers[j + 1].color = Fore.RESET

    # Print and change the "bubbled" number color to green
    numbers[len(numbers) - 1 - i].color = Fore.GREEN
    line_end = '\r' if i != len(numbers) - 1 else '\n'
    print(numbers, end=line_end)

print()
