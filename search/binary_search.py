"""Binary Search Visualizer

This script creates a random list of integers, sorts the list, and uses binary search
to find a value that may or may not be in it.
Each step of the algorithm is shown by coloring the numbers in the list and 
displaying it to the console.
"""

from random import randint
from time import sleep

from colorama import Fore
from colorama import init as colorama_init

from sscommon.colored_int import ColoredInt
from sscommon.util import change_color_in_range

# Options
LIST_SIZE = 20
MIN_VALUE = -100
MAX_VALUE = 100
SPEED = 1
PRINT_DELAY = 1 / SPEED

# Setup
colorama_init(autoreset=True)

# Create a random list of integers, then sort it in ascending order
numbers = list()
for _ in range(LIST_SIZE):
    random_int = randint(MIN_VALUE, MAX_VALUE)
    colored_number = ColoredInt(random_int)
    numbers.append(colored_number)
numbers.sort()

# Pick a number to search for
number_to_search = None
pick_number_in_list = randint(1, 2) == 1
if pick_number_in_list:
    index = randint(0, LIST_SIZE - 1)
    number_to_search = numbers[index].value
else:
    x = randint(MIN_VALUE, MAX_VALUE)
    while x in numbers:
        x = randint(MIN_VALUE, MIN_VALUE)
    number_to_search = x

# Perfrom the binary search
print()
print(f"Searching for {number_to_search}:")
print(numbers, end='\r')
sleep(PRINT_DELAY)
low = 0
high = len(numbers) - 1
# These "previous" values are used for coloring, they don't affect the algorithm
previous_low = low
previous_high = high
while low <= high:
    # Change the low and high bounds to blue
    numbers[low].color = Fore.BLUE
    numbers[high].color = Fore.BLUE

    print(numbers, end='\r')
    sleep(PRINT_DELAY)

    # Calculate the midpoint and change it to yellow
    mid = (low + high) // 2
    numbers[mid].color = Fore.YELLOW
    print(numbers, end='\r')
    sleep(PRINT_DELAY)

    # Search for the desired number.
    # If it's found, change it to green.
    # If not, adjust the low or high pointer
    # and change all the values outside the new bounds to red.
    if numbers[mid] == number_to_search:
        numbers[mid].color = Fore.GREEN
        print(numbers)
        break
    elif number_to_search > numbers[mid]:
        low = mid + 1
        change_color_in_range(numbers, previous_low, low, Fore.RED)
        previous_low = low

    else:
        high = mid - 1
        change_color_in_range(numbers, high + 1, previous_high + 1, Fore.RED)
        previous_high = high

    end = '\n' if low > high else '\r'
    print(numbers, end=end)
    sleep(PRINT_DELAY)

print()
