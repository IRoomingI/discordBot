from colorama import Fore, Style, init
import discord
import asyncio
import json


# Colorama init

init()

# Load config

mode = "prod"


def load_config():
    if mode == "dev":
        config_file = open("devconf.json", "r", encoding="utf-8")
    else:
        config_file = open("CONFIG.json", "r", encoding="utf-8")
    config = json.load(config_file)
    config_file.close()
    return config


config = load_config()


def insert_config(newconf):
    if mode == "dev":
        config_file = open("devconf.json", "w", encoding="utf-8")
    else:
        config_file = open("CONFIG.json", "w", encoding="utf-8")
    json.dump(newconf, config_file, ensure_ascii=False, indent=4)
    config_file.close()


# Logger

async def log(message, logtype, chat=False, chan=None, client=None, delete=True):
    """Used for logging in terminal and if wanted also to the Discord channel."""
    if logtype == "error":
        pref = "[ " + color(logtype.upper(), "red") + " ]"
        col = discord.Color.red()
    elif logtype == "info":
        pref = "[ " + color(logtype.upper(), "green") + " ]"
        col = discord.Color.green()
    else:
        pref = ""
        col = discord.Color.blue()
    output = pref + "  " + message
    print(output)

    if chat:
        return_msg = await client.send_message(chan, embed=discord.Embed(color=col, description=message))
        if delete:
            await asyncio.sleep(2.5)
            await client.delete_message(return_msg) 


def color(string, color):
    """Choose a color for terminal output."""
    if color == "red":
        string = Fore.RED + string
    elif color == "green":
        string = Fore.GREEN + string
    elif color == "blue":
        string = Style.BRIGHT + Fore.BLUE + string
    elif color == "white":
        string = Fore.WHITE + string
    elif color == "code":
        string = Style.DIM + Fore.YELLOW + string
    else:
        print(Fore.RED + "Color %s not found" % color + Fore.RESET)
        return string
    string += Style.RESET_ALL
    return string


# List to string / sentence

def stringify(input):
    """Convert list to sentence. Used for converting 'args' to a sentence."""
    out = ""
    if len(input) > 0:
        for word in input:
            out += word + " "
        out = out[:-1]
    return out


# Config getters and setters

def get_token():
    return config["TOKEN"]


def get_prefix():
    return config["PREFIX"]


def get_owner():
    return config["OWNER_ID"]


async def set_prefix(pref, channel, userid, client):
    if str(userid) == config["OWNER_ID"]:
        if isinstance(pref, str) and len(pref) <= 8:
            config["PREFIX"] = pref
            insert_config(config)
            await log("Successfully changed prefix to: %s" % color(pref, "white"), "info", chat=True, chan=channel, client=client, delete=False)  
        else:
            await log("Longer than 8 characters.", "error", chat=True, chan=channel, client=client)
    else:
        await log("Failed because the user isn't the owner.", "error", chat=True, chan=channel, client=client)


def get_game():
    return config["GAME"]


def set_game(newgame):
    config["GAME"] = str(newgame)
    insert_config(config)