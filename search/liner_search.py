from random import randint
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
numbers = list()
for _ in range(LIST_SIZE):
    random_int = randint(MIN_VALUE, MAX_VALUE)
    colored_number = ColoredInt(random_int)
    numbers.append(colored_number)

# Pick a number to search for
number_to_search = None
pick_number_in_list = randint(1, 2) == 1
if pick_number_in_list:
    index = randint(0, LIST_SIZE - 1)
    number_to_search = numbers[index].value
else:
    x = randint(MIN_VALUE, MAX_VALUE)
    while x in numbers:
        x = randint(MIN_VALUE, MAX_VALUE)
    number_to_search = x

# Search the list for the selected number
print()
print(f"Searching for {number_to_search}:")
print(numbers, end='\r')
sleep(PRINT_DELAY)
for i, number in enumerate(numbers):
    # Highlight the current number being checked in yellow
    numbers[i].color = Fore.YELLOW
    print(numbers, end='\r')
    sleep(PRINT_DELAY)

    if number == number_to_search:
        numbers[i].color = Fore.GREEN
        print(numbers, end='\n')
        break
    else:
        numbers[i].color = Fore.RED
        end = '\r' if i != len(numbers) - 1 else '\n'
        print(numbers, end=end)
        sleep(PRINT_DELAY)

print()
