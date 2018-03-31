import discord
from discord import Game, Embed, Color
import CONFIG
from commands import cmd_ping, cmd_clear, cmd_type, cmd_say, cmd_help, cmd_color
from logger import log

client = discord.Client()


commands = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "type": cmd_type,
    "say": cmd_say,
    "help": cmd_help,
    "color": cmd_color

}


@client.event
async def on_ready():

    log("%s started successfully. Running on server(s):" % client.user.name, "info")
    for s in client.servers:
        log("  - %s (%s)" % (s.name, s.id), "")

    await client.change_presence(game=Game(name=CONFIG.GAME))


@client.event
async def on_message(message):
    if message.content.startswith(CONFIG.PREFIX):
        invoke = message.content[len(CONFIG.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            log("Executing command %s" % invoke, "info")
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.send_message(message.author, embed=Embed(color=Color.red(), description=("This command doesn't exist: %s" % invoke)))
            log("Command - %s - not found!" % invoke, "error")


client.run(CONFIG.TOKEN)
