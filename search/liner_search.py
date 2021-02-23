"""Linear Search Visualizer

This script creates a random list of integers and uses a linear search 
to find a value that may or may not be in the list.
Each step of the algorithm is shown by coloring the numbers in the 
list and displaying it to the console.
"""

from random import randint, random
from sscommon.util import list_of_random_colored_ints, print_list_with_delay, random_number_to_search
from time import sleep

from colorama import Fore
from colorama import init as colorama_init

from sscommon.colored_int import ColoredInt

# Options
LIST_SIZE = 10
MIN_VALUE = -100
MAX_VALUE = 100
SPEED = 2
PRINT_DELAY = 1 / SPEED

# Setup
colorama_init(autoreset=True)

# Create a random list of colored integers
numbers = list_of_random_colored_ints(LIST_SIZE, MIN_VALUE, MAX_VALUE)

# Pick a number to search for
number_to_search = random_number_to_search(numbers, MIN_VALUE, MAX_VALUE)

# Search the list for the selected number
print()
print(f"Searching for {number_to_search}:")
print_list_with_delay(numbers, PRINT_DELAY)
for i, number in enumerate(numbers):
    # Highlight the current number being checked in yellow
    numbers[i].color = Fore.YELLOW
    print_list_with_delay(numbers, PRINT_DELAY)

    if number == number_to_search:
        numbers[i].color = Fore.GREEN
        print(numbers, end='\n')
        break
    else:
        numbers[i].color = Fore.RED
        end = '\r' if i != len(numbers) - 1 else '\n'
        print_list_with_delay(numbers, PRINT_DELAY)


print()
