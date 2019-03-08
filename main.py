import Logger, discord, utils
from commands import cmd_ping, cmd_clear, cmd_say, cmd_help, cmd_color, cmd_game, cmd_prefix, cmd_nick, cmd_poll, cmd_autorole

client = discord.Client()

# Sending client to the Logger

Logger.set_client(client)

commands = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "say": cmd_say,
    "help": cmd_help,
    "color": cmd_color,
    "game": cmd_game,
    "prefix": cmd_prefix,
    "nick": cmd_nick,
    "poll": cmd_poll,
    "autorole": cmd_autorole

}


@client.event
async def on_ready():

    await Logger.info("%s started successfully. Running on server(s):" % client.user.name)
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))

    await client.change_presence(game=discord.Game(name=utils.config["GAME"]))


@client.event
async def on_message(message):
    if message.content.startswith(utils.config["PREFIX"]):
        invoke = message.content[len(utils.config["PREFIX"]):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if invoke in commands:
            if invoke != "clear": await client.delete_message(message)
            await Logger.info("%s is executing command %s" % (utils.color(message.author.name + " (%s)" % message.author.id, "white"), utils.color(invoke, "blue")))
            await commands.get(invoke).ex(args, message, client, invoke)
            utils.update()
        else:
            await client.delete_message(message)
            await Logger.error("Command not found: %s" % invoke, chat=True, chan=message.channel)


# Voting for polls

@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if user.id != client.user.id and message.author.id == client.user.id:
        await commands.get("poll").vote(message, user, client, reaction)


# Autorole / Join

@client.event
async def on_member_join(member):
    role_ids = utils.data["AUTOROLE_IDS"]
    not_found = False
    msg = "==> %s (%s) joined %s." % (utils.color(member.name, "white"), member.id, utils.color(member.server.name, "blue"))
    if len(role_ids) > 0:
        auto_roles = []
        for r in role_ids:
            found = discord.utils.find(lambda add: add.id == r , member.server.roles)
            if found != None:
                auto_roles.append(found)
        if len(auto_roles) > 0:
            await client.add_roles(member, auto_roles)
            role_names = []
            for r in auto_roles:
                role_names.append(r.name)
            msg += " Automatically assigned the role(s): %s" % ", ".join(role_names)
        else:
            not_found = True
    await Logger.info(msg)
    if not_found:
        await Logger.warn("Could not find any of the entered Role IDs for Autorole.")

try:
    client.run(utils.config["TOKEN"])
except ConnectionResetError():
    Logger.warn("Connection reset by peer... Everything should still be fine")
except discord.LoginFailure:
    print("It seems like no %s was given or it was incorrect. Please check the %s!" % (utils.color("Discord Bot Token", "red"), utils.color("CONFIG.json", "blue")))
except RuntimeError:
    print("\nShutting down...")
