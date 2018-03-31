import discord
import CONFIG

async def ex(args, message, client, invoke):
    msg = "```--- Help ---\n\n"
    cmd_list = [
            "clear [args/number]",
            "ping",
            "say [args/text]",
            "type [args/text]",
            "help",
            "color [args/color]"
                ]
    for element in cmd_list:
        msg += "    " + CONFIG.PREFIX + element + "\n"
    msg += " ```"
    await client.delete_message(message)
    await client.send_message(message.channel, msg)
