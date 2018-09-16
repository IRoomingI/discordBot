import discord
from discord import Game, Embed, Color
import utils
from commands import cmd_ping, cmd_clear, cmd_say, cmd_help, cmd_color, cmd_game, cmd_prefix, cmd_nick

client = discord.Client()

commands = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "say": cmd_say,
    "help": cmd_help,
    "color": cmd_color,
    "game": cmd_game,
    "prefix": cmd_prefix,
    "nick": cmd_nick

}


@client.event
async def on_ready():

    await utils.log("%s started successfully. Running on server(s):" %
        client.user.name, "info")
    for s in client.servers:
        await utils.log("  - %s (%s)" % (s.name, s.id), "")

    await client.change_presence(game=Game(name=utils.getGame()))


@client.event
async def on_message(message):
    if message.content.startswith(utils.getPrefix()):
        invoke = message.content[len(utils.getPrefix()):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            await client.delete_message(message)
            await utils.log("Executing command %s" % invoke, "info")
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.delete_message(message)
            await utils.log("Command not found: %s" % invoke, "error", chat=True, chan=message.channel, client=client, delete=True)


client.run(utils.getToken())
