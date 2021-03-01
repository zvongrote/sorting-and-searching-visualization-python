"""Selection Sort Visualizer

This script creates a random list of integers and sorts it using selection sort.
Each step of the algorithm is shown by coloring the numbers in the list and displaying it to the console.
"""

from sscommon.colored_int import ColoredInt
from colorama import init as color_init
from colorama.ansi import Fore

from sscommon.util import list_of_random_colored_ints, print_list_with_delay, print_underlined, swap, visual_swap

# Options
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

# Selection sort the list
print_underlined("Sorted")
for i in range(len(numbers)):
    # Find the minimum element in the unsorted section of the list
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    # Show the found minimum value in red
    numbers[min_index].color = Fore.RED
    print_list_with_delay(numbers, PRINT_DELAY)

    # Swap minimum value into place
    if min_index != i:
        swap(numbers, min_index, i)
        print_list_with_delay(numbers, PRINT_DELAY)

    # Color the numbers in place green, and reset the other colors
    numbers[min_index].color = Fore.RESET
    numbers[i].color = Fore.GREEN
    print_list_with_delay(numbers, PRINT_DELAY)


print(numbers)
