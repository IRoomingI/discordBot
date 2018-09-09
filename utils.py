from colorama import Fore, init
import discord
import asyncio
import json


# Colorama init

init()

# Load config

def loadConfig():
    config_file = open("CONFIG.json", "r", encoding="utf-8")
    config = json.load(config_file)
    config_file.close()
    return config

config = loadConfig()

def insertConfig(newconf):
    config_file = open("CONFIG.json", "w", encoding="utf-8")
    json.dump(newconf, config_file, ensure_ascii=False, indent=4)
    config_file.close()


# Logger

async def log(message, logtype, chat=False, chan=None, client=None):
    if logtype == "error":
        pref = "[ " + Fore.RED + logtype.upper() + Fore.RESET + " ]"
        col = discord.Color.red()
    elif logtype == "info":
        pref = "[ " + Fore.GREEN + logtype.upper() + Fore.RESET + " ]"
        col = discord.Color.green()
    else:
        pref = ""
        col = discord.Color.blue()
    output = pref + "  " + message
    print(output)

    if chat:
        #await send_chat(client, col, chan, message)
        return_msg = await client.send_message(chan, embed=discord.Embed(color=col, description=message))
        await asyncio.sleep(2.5)
        await client.delete_message(return_msg) 


async def send_chat(client, col, chan, message):
    # return_msg = await client.send_message(chan, embed=discord.Embed(color=col, description=message))
    # await asyncio.sleep(2.5)
    # await client.delete_message(return_msg)
    pass


# List to string / sentence

def stringify(input):
    out = ""
    if len(input) > 0:
        for word in input:
            out += word + " "
        out = out[:-1]
    return out


# Config getters and setters

def getToken():
    return config["TOKEN"]


def getPrefix():
    return config["PREFIX"]


def setPrefix(pref, channel, userid, client):
    if userid is config["OWNER_ID"]:
        if isinstance(pref, str) and len(pref) <= 8:
            config["PREFIX"] = pref
            insertConfig(config)
            await log("Successfully changed prefix to: %s" % pref, "info")  
        else:
            await log("Not a string or longer than 8 characters", "error", chat=True, chan=channel)
    else:
        await log("Failed because the user isn't the owner.", "error", chat=True, chan=channel, client=client)


def getGame():
    return config["GAME"]


def setGame(newgame):
    config["GAME"] = str(newgame)
    insertConfig(config)