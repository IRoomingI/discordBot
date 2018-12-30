import Logger, discord
from utils import config
from datetime import datetime


cmds = {
        "clear": ["number", "Remove multiple messages at once. Limit: 99 messages, Can't be older than 14 days."],
        "ping": ["", "Get a DM from the Bot saying 'Pong!'."],
        "say": ["text", "Let the Bot say something."],
        "help": ["", "Show the help text."],
        "color": ["color_name/list/add/remove", "Set your displayed name color or manage colors."],
        "game": ["text", "Change the game that the bot is currently playing."],
        "prefix": ["text", "OWNER ONLY! Change the command prefix. Prefix length should be between 1 and 8."],
        "nick": ["text", "Change your nick name. (Can't change the owners nickname)."],
        "poll": ['"description" ["option1", "option2", "..."]', "Create a poll with up to 6 options."],
        "autorole": ["add/remove/list", "Configure the roles that are assigned to users joining the server."]
}

porn = ["http://www.xvideos.com/", "http://www.youporn.com/","http://xhamster.com/","http://www.xnxx.com/", "http://www.youjizz.com/",
        "http://www.mofosex.com/","http://www.befuck.com/","http://www.pornhub.com/","http://xxxbunker.com/","http://www.drtuber.com/",
        "http://www.pornhost.com/","http://www.tube8.com/","http://spankbang.com/"]


async def ex(args, message, client, invoke):
    otaku = discord.utils.find(lambda r: r.name == "Otaku", message.author.roles)
    if len(args) > 0 and otaku is not None:
        if str(args[0]).lower() == "me":
            msg = help_text("otaku")
        else:
            msg = help_text()
    else:
        msg = help_text()
    await client.send_message(message.channel, msg)
    await Logger.info("Successfully sent help text.")
        

def help_text(type = "normal"):
    if type == "normal":
        msg = "```--- Help ---\n\n"
        msg += "Date: " + datetime.now().strftime("%X | %A %d %B %Y") + "\n\n"
        for key in sorted(cmds):
            msg += "\t" + config["PREFIX"] + key + "  " + "<" + cmds[key][0] + ">  »" + cmds[key][1] + "« \n"
        msg += "\n------------```"
    elif type == "otaku":
        msg = "``` Stop it, get some help:\n\n"
        for p in porn:
            msg += "- %s\n" % p
        msg += "```"
    return msg
