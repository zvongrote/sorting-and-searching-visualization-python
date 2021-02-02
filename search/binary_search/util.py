from colorama import Fore


def change_color_in_range(list, min, max, color):
    for i in range(min, max):
        list[i].color = Fore.RED
