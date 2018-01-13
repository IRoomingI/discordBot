import discord
from discord import Game, Embed, Color
import SECRETS
import STATICS
from commands import cmd_ping, cmd_clear, cmd_type, cmd_say

client = discord.Client()


commands = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "type": cmd_type,
    "say": cmd_say,

}


@client.event
async def on_ready():

    print("Bot started successfully. Running on server(s):\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))

    await client.change_presence(game=Game(name="keine Musik D:"))


@client.event
async def on_message(message):
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.send_message(message.author, embed=Embed(color=Color.red(), description=("This command doesn't exist: %s" % invoke)))


client.run(SECRETS.TOKEN)
