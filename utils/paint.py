from colorama import Fore, Style, init

# Colorama init

init()

# Color stuff


colors = {
    "red": Fore.RED, "green": Fore.GREEN, "blue": Style.BRIGHT + Fore.BLUE,
    "white": Fore.WHITE, "yellow": Fore.YELLOW, "code": Style.DIM + Fore.YELLOW
}


def color(string, color):
    """Choose a color for terminal output. Red, Green, Blue, White and 'Code'"""

    color = color.lower()  # For dummies that capitalize color names

    if color in colors:
        string = colors[color] + string
    else:
        print(Fore.RED + "Color %s not found" % color + Fore.RESET)
        return string
    string += Style.RESET_ALL
    return string
