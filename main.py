import Logger
import discord
from utils import paint, config, db
from commands import ping, clear, say, help, color, activity, prefix, nick, poll, autorole, info

client = discord.Client()

commands = {

    "ping": ping,
    "clear": clear,
    "say": say,
    "help": help,
    "color": color,
    "activity": activity,
    "prefix": prefix,
    "nick": nick,
    "poll": poll,
    "autorole": autorole,
    "info": info

}


@client.event
async def on_ready():

    await Logger.info("%s started successfully. Running on guild(s):" % client.user.name)
    for s in client.guilds:
        print("  - %s (%s)" % (s.name, s.id))
        db.create_guild(s.id, s.name, s.owner.id)

    converted = list(config.CONFIG["ACTIVITY"].items())[0]
    converted = [converted[0], converted[1]]
    await activity.ex(converted, None, client, None)


@client.event
async def on_message(message):
    if message.guild is not None and not message.author.bot:  # if guild is None it's a DM, don't react to bot messages
        if message.content.startswith(db.fetch_prefix(message.guild.id)):
            invoke = message.content[len(db.fetch_prefix(message.guild.id)):].split(" ")[0]
            args = message.content.split(" ")[1:]
            if invoke in commands:
                if invoke != "clear":
                    await message.delete()
                await Logger.info("%s: %s is executing command %s" % (paint.color(message.guild.name, "yellow"), paint.color(message.author.name + " (%s)" % message.author.id, "white"), paint.color(invoke, "blue")))
                await commands.get(invoke).ex(args, message, client, invoke)
                config.update()
            else:
                await message.delete()
                await Logger.error("Command not found: %s" % invoke, chan=message.channel)


# Voting for polls

@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if user.id != client.user.id and message.author.id == client.user.id:
        await poll.vote(message, user, client, reaction)


# Autorole / Join

@client.event
async def on_member_join(member):
    role_ids = db.fetch_autoroles(member.guild.id)
    not_found = False
    msg = "==> %s%s (%s) joined %s." % (paint.color("BOT ", "green") if member.bot else "", paint.color(member.name, "white"), member.id, paint.color(member.guild.name, "blue"))
    if len(role_ids) > 0:
        if not member.bot:
            auto_roles = []
            for r in role_ids:
                result = member.guild.get_role(r)
                if result is not None:
                    auto_roles.append(result)
            if len(auto_roles) > 0:
                try:
                    for r in auto_roles:
                        await member.add_roles(r)
                except discord.Forbidden:
                    await Logger.error("No Permission to add autoroles on `%s`. Please make sure the bot's role is placed above the roles you want to add in the Discord guild settings." % member.guild.name, chan=member.guild.owner, delete=False)
                else:
                    role_names = []
                    for r in auto_roles:
                        role_names.append(r.name)
                    msg += " Automatically assigned the role(s): %s" % ", ".join(role_names)
            else:
                not_found = True
        else:
            await Logger.warn("A new bot (%s) joined your guild. Autorole does not automatically assign roles to bots since they can have their own roles." % member.name, chan=member.guild.owner, delete=False)
    await Logger.info(msg)
    if not_found:
        await Logger.warn("Could not find any of the entered Role IDs for Autorole.")


# Bot guild join / leave

@client.event
async def on_guild_join(guild):
    db.create_guild(guild.id, guild.name, guild.owner.id)
    await Logger.info("%s joined a new guild: %s" % (client.user.name, paint.color(guild.name + " (%s)" % guild.id, "white")))


@client.event
async def on_guild_remove(guild):
    db.delete_guild(guild.id)
    await Logger.info("%s left a guild: %s" % (client.user.name, paint.color(guild.name + " (%s)" % guild.id, "white")))

try:
    client.loop.run_until_complete(client.start(config.CONFIG["TOKEN"]))
except ConnectionResetError:
    Logger.warn("Connection reset by peer... Everything should still be fine")
except discord.LoginFailure:
    print("It seems like no %s was given or it was incorrect. Please check the %s!" % (
        paint.color("Discord Bot Token", "red"), paint.color("CONFIG.json", "blue")))
    client.loop.run_until_complete(client.logout())
except KeyboardInterrupt:
    client.loop.run_until_complete(client.logout())
finally:
    client.loop.close()
    print("\nShutting down...")
