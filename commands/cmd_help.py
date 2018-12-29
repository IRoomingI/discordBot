import Logger, discord
from utils import get_prefix
from datetime import datetime


cmds = {
        "clear": ["number", "Remove multiple messages at once. Limit: 99 messages, Can't be older than 14 days."],
        "ping": ["", "Get a DM from the Bot saying 'Pong!'."],
        "say": ["text", "Let the Bot say something."],
        "help": ["", "Show the help text."],
        "color": ["color_name/clear/list/add/remove", "Set your displayed name color or manage colors."],
        "game": ["text", "Change the game that the bot is currently playing."],
        "prefix": ["text", "OWNER ONLY! Change the command prefix. Prefix length should be between 1 and 8."],
        "nick": ["text", "Change your nick name. (Can't change the owners nickname)."],
        "poll": ['"description" ["option1", "option2", "..."]', "Create a poll with up to 6 options."],
        "autorole": ["add/remove", "Configure the roles that are assigned to users joining the server."]
}

porn = ["http://www.xvideos.com/", "http://www.youporn.com/","http://xhamster.com/","http://www.xnxx.com/", "http://www.youjizz.com/",
        "http://www.mofosex.com/","http://www.befuck.com/","http://www.pornhub.com/","http://xxxbunker.com/","http://www.drtuber.com/",
        "http://www.pornhost.com/","http://www.tube8.com/","http://spankbang.com/"]


async def ex(args, message, client, invoke):
    otaku = discord.utils.find(lambda r: r.name == "Otaku", message.author.roles)
    if otaku.name != "Otaku" and str(args[0]).lower() == "me":
        msg = "```--- Help ---\n\n"
        msg += "Date: " + str(datetime.now()).split(".")[0] + "\n\n"
        for key in sorted(cmds):
            msg += "\t" + get_prefix() + key + "  " + "<" + cmds[key][0] + ">  »" + cmds[key][1] + "« \n"
        msg += "\n------------```"
    else:
        msg = "``` Stop it, get some help:\n\n"
        for p in porn:
            msg += "- %s\n" % p
        msg += "```"
    await client.send_message(message.channel, msg)
    await Logger.info("Successfully sent help text.")
