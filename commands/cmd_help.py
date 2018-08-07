import CONFIG
from utils import log


async def ex(args, message, client, invoke):
    msg = "```--- Help ---\n\n"
    cmd_list = [
        "clear [args/number]",
        "ping",
        "say [args/text]",
        "type [args/text]",
        "help",
        "color [args/color]",
        "game [args/text]"
    ]
    for element in cmd_list:
        msg += "    " + CONFIG.PREFIX + element + "\n"
    msg += "\n------------```"
    await client.delete_message(message)
    await client.send_message(message.channel, msg)
    log("Successfully sent help text", "info")
