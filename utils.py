from colorama import Fore, init
init()      # Colorama init


# Logger
def log(message, logtype):
    if logtype == "error":
        pref = "[ " + Fore.RED + logtype.upper() + Fore.RESET + " ]"
    elif logtype == "info":
        pref = "[ " + Fore.GREEN + logtype.upper() + Fore.RESET + " ]"
    else:
        pref = ""
    output = pref + "  " + message
    print(output)


# List to string / sentence
def stringify(input):
    out = ""
    for word in input:
        out += word + " "
    out = out[:-1]
    return out
