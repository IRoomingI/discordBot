import discord
from utils import log, color


async def ex(args, message, client, invoke):
    if len(args) > 0:
        out = " ".join(args)
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=out))
        out = out.replace("\n", " / ")
        if out.startswith("`") and out.endswith("`"):
            if out.startswith("```") and out.endswith("```"):
                out = out[3:-3]
                await log("Successfully said: '%s'" % color(out, "code"), "info")
            else:
                out = out[1:-1]
                await log("Successfully said: '%s'" % color(out, "code"), "info")
        else:
            await log("Successfully said: '%s'" % out, "info")
    else:
        await log("Doesn't accept empty messages.", "error")
