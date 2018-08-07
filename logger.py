import colorama as color
color.init()

#INFO = '\x1b[0;0;32m'
#ERROR = '\x1b[0;0;31m'
#COLOR_END = '\x1b[0m'


def log(message, logtype):
    if logtype == "error":
        pref = "[ " + color.Fore.RED + logtype.upper() + " ]"
    elif logtype == "info":
        pref = "[ " + color.Fore.GREEN + logtype.upper() + " ]"
    else:
        pref = ""
    output = pref + "  " + message
    print(output)
