from colorama import Fore, Style, init
import discord, json, Logger

# Colorama init

init()

# Load config and data

mode = "dev"


def load():
    with open("CONFIG.json" if mode != "dev" else "devCONFIG.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    with open("data.json" if mode != "dev" else "devdata.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return config, data


config, data = load()


# Insert config and data

def insert_config(newconf):
    with open("CONFIG.json" if mode != "dev" else "devCONFIG.json", "w", encoding="utf-8") as f:
        json.dump(newconf, f, ensure_ascii=False, indent=4)


def insert_data(newdata):
    with open("data.json" if mode != "dev" else "devdata.json", "w", encoding="utf-8") as f:
        json.dump(newdata, f, ensure_ascii=False, indent=4)


# Color stuff

def color(string, color):
    """Choose a color for terminal output. Red, Green, Blue, White and 'Code'"""
    if color == "red":
        string = Fore.RED + string
    elif color == "green":
        string = Fore.GREEN + string
    elif color == "blue":
        string = Style.BRIGHT + Fore.BLUE + string
    elif color == "white":
        string = Fore.WHITE + string
    elif color == "yellow":
        string = Fore.YELLOW + string
    elif color == "code":
        string = Style.DIM + Fore.YELLOW + string
    else:
        print(Fore.RED + "Color %s not found" % color + Fore.RESET)
        return string
    string += Style.RESET_ALL
    return string


# Config getters and setters

def get_token():
    return config["TOKEN"]


def get_prefix():
    return config["PREFIX"]


def get_owner():
    return config["OWNER_ID"]


def get_autorole_ids():
    return data["AUTOROLE_IDS"]

def set_autorole_ids(ids):
    data["AUTOROLE_IDS"] = ids
    insert_data(data)

def get_colors():
    return data["COLOR_ROLES"]


def set_colors(roles):
    data["COLOR_ROLES"] = roles
    insert_data(data)


async def set_prefix(pref, channel, userid, client):
    if str(userid) == config["OWNER_ID"]:
        if isinstance(pref, str) and len(pref) <= 8:
            config["PREFIX"] = pref
            insert_config(config)
            await Logger.info("Successfully changed prefix to: **%s**" % pref, chat=True, chan=channel, delete=False)
        else:
            await Logger.error("Longer than 8 characters.", chat=True, chan=channel)
    else:
        await Logger.error("Failed because the user isn't the owner.", chat=True, chan=channel)


def get_game():
    return config["GAME"]


def set_game(newgame):
    config["GAME"] = str(newgame)
    insert_config(config)
