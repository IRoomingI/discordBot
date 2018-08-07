from colorama import Fore, init
color.init()

def log(message, logtype):
    if logtype == "error":
        pref = "[ " + Fore.RED + logtype.upper() + Fore.RESET + " ]"
    elif logtype == "info":
        pref = "[ " + Fore.GREEN + logtype.upper() + Fore.RESET + " ]"
    else:
        pref = ""
    output = pref + "  " + message
    print(output)
