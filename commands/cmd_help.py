from utils import log, get_prefix
from datetime import datetime


cmds = {
        "clear": ["number", "Remove multiple messages at once. Limit: 99 messages, Can't be older than 14 days."],
        "ping": ["", "Get a DM from the Bot saying 'Pong!'."],
        "say": ["text", "Let the Bot say something."],
        "help": ["", "Show the help text."],
        "color": ["color name", "Set your displayed name color. Type 'color help' to show supported colors."],
        "game": ["text", "Change the game that the bot is currently playing."],
        "prefix": ["text", "OWNER ONLY! Change the command prefix. Prefix length should be between 1 and 8."],
        "nick": ["text", "Change your nick name. (Can't change the owners nickname)."],
        "poll": ['"description" ["option1", "option2", "..."]', "Create a poll with up to 6 options."]
}


async def ex(args, message, client, invoke):
    msg = "```--- Help ---\n\n"
    msg += "Date: " + str(datetime.now()).split(".")[0] + "\n\n"
    for key in sorted(cmds):
        msg += "\t" + get_prefix() + key + "  " + "<" + cmds[key][0] + ">  »" + cmds[key][1] + "« \n"
    msg += "\n------------```"
    await client.send_message(message.channel, msg)
    await log("Successfully sent help text.", "info")
