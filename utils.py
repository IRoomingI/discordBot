from colorama import Fore, Style, init
import json

# Colorama init

init()

# Load config and data

mode = "prod"


def load():
    with open("CONFIG.json" if mode != "dev" else "devCONFIG.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    return config


config = load()


# Update config and data

def update():
    with open("CONFIG.json" if mode != "dev" else "devCONFIG.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

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
