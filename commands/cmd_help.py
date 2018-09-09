from utils import log, getPrefix


async def ex(args, message, client, invoke):
    msg = "```--- Help ---\n\n"
    cmds = {
        "clear": ["number", "Remove multiple messages at once. Limit: 99 messages, Can't be older than 14 days."],
        "ping": ["", "Get a DM from the Bot saying 'Pong!'."],
        "say": ["text", "Let the Bot say something."],
        "help": ["", "Show the help text."],
        "color": ["color name", "Set your displayed name color. Type 'color help' to show supported colors."],
        "game": ["text", "Change the game that the bot is currently playing."],
        "prefix": ["text", "OWNER ONLY! Change the command prefix. Prefix length should be between 1 and 8."]
    }

    for key in cmds:
        msg += "    " + getPrefix() + key +" "+ cmds[key][0] +" "+ cmds[key][1] + "\n"
    msg += "\n------------```"
    await client.delete_message(message)
    await client.send_message(message.channel, msg)
    log("Successfully sent help text", "info")
