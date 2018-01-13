INFO = '\x1b[0;0;32m'
ERROR = '\x1b[0;0;31m'
COLOR_END = '\x1b[0m'

def log(message, logtype):
    if logtype == "error":
        pref = "[ " + ERROR + logtype.upper() + COLOR_END + " ]"
    elif logtype == "info":
        pref = "[ " + INFO + logtype.upper() + COLOR_END + " ]"
    else:
        pref = ""
    output = pref + "  " + message
    print(output)
