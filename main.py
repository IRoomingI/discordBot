import discord
from discord import Game, Embed, Color
import utils
from commands import cmd_ping, cmd_clear, cmd_say, cmd_help, cmd_color, cmd_game, cmd_prefix, cmd_nick, cmd_poll

client = discord.Client()

commands = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "say": cmd_say,
    "help": cmd_help,
    "color": cmd_color,
    "game": cmd_game,
    "prefix": cmd_prefix,
    "nick": cmd_nick,
    "poll": cmd_poll

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
            if invoke != "clear": await client.delete_message(message)
            await utils.log("%s is executing command %s" % (utils.color(message.author.name + " (%s)" % message.author.id, "white"), utils.color(invoke, "blue")), "info")
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.delete_message(message)
            await utils.log("Command not found: %s" % invoke, "error", chat=True, chan=message.channel, client=client, delete=True)


@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if user.id != client.user.id and message.author.id == client.user.id:
        await commands.get("poll").vote(message, user, client, reaction)


client.run(utils.getToken())
