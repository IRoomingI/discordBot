import Logger
from utils import db
from datetime import datetime
from discord import Embed


cmds = {
    "clear": ["number", "Remove multiple messages at once. Limit: 99 messages. Can't be older than 14 days."],
    "ping": ["/", "Get a DM from the bot saying 'Pong!'."],
    "say": ["text", "Let the bot say something."],
    "help": ["command", "Show the help text."],
    "color": ["color_name/list/add/remove", "Set your displayed name color or manage colors."],
    "activity": ["game/streaming/custom", "text", "Change the activity of the bot."],
    "prefix": ["text/list", "GUILD OWNER ONLY! Change the command prefix. Prefix length should be between 1 and 8."],
    "nick": ["text", "Change your nick name. (Can't change the owners nickname)."],
    "poll": ['"description"', '["option1", "option2", "..."]', "Create a poll. You can vote by reacting to the message. The creator of the poll can close it by reacting with a ❌."],
    "autorole": ["add/remove/list" "@role", "Configure the roles that are assigned to users joining the guild."],
    "info": ["/", "Shows some information belonging to the bot."]
}


async def ex(args, message, client, invoke):
    PREFIX = db.fetch_prefix(message.guild.id)
    if len(args) == 0:
        embed = Embed(title="Help", description="For detailed information use: `+help command`", color=0x2cc85e)

        args = ""
        command = ""
        for key in sorted(cmds):
            for arg in cmds[key][:-1]:
                args += "<" + arg + "> "
            args += "\n"
            command += PREFIX + key + "\n"

        embed.add_field(name="Command", value=command)
        embed.add_field(name="Arguments", value=args)
        embed.set_footer(text="Date: %s" % datetime.now().strftime("%X | %A %d %B %Y"))

        await message.channel.send(embed=embed)
        await Logger.info("Successfully sent help text.")
    else:
        cmd = args[0].lower()
        if cmd in cmds.keys():
            desc = f"""`{PREFIX}{cmd} {" ".join(cmds[cmd][:-1])}`\n\n{cmds[cmd][-1]}"""
            embed = Embed(title=args[0].capitalize(), description=desc, color=0x2cc85e)
            await message.channel.send(embed=embed)
            await Logger.info("Successfully sent help text for %s" % cmd)
        else:
            await Logger.error("Command `%s` not found!" % cmd, chan=message.channel)
