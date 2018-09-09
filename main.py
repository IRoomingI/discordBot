import discord
from discord import Game, Embed, Color
from commands import cmd_ping, cmd_clear, cmd_type, cmd_say, cmd_help, cmd_color, cmd_game, cmd_prefix
import utils

client = discord.Client()


commands = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "say": cmd_say,
    "help": cmd_help,
    "color": cmd_color,
    "game": cmd_game,
    "prefix": cmd_prefix

}


@client.event
async def on_ready():

    utils.log("%s started successfully. Running on server(s):" %
        client.user.name, "info")
    for s in client.servers:
        utils.log("  - %s (%s)" % (s.name, s.id), "")

    await client.change_presence(game=Game(name=utils.getGame()))


@client.event
async def on_message(message):
    if message.content.startswith(utils.getPrefix()):
        invoke = message.content[len(utils.getPrefix()):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            utils.log("Executing command %s" % invoke, "info")
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.send_message(message.author, embed=Embed(color=Color.red(), description=("This command doesn't exist: %s" % invoke)))
            utils.log("Command - %s - not found!" % invoke, "error")


client.run(utils.getToken())
