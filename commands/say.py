import discord
import Logger
from utils import paint

async def ex(args, message, client, invoke):
    if len(args) > 0:
        out = " ".join(args)
        await message.channel.send(embed=discord.Embed(color=discord.Color.green(), description=out))
        out = out.replace("\n", " / ")
        if out.startswith("`") and out.endswith("`"):
            if out.startswith("```") and out.endswith("```"):
                out = out[3:-3]
                await Logger.info("Successfully said: '%s'" % paint.color(out, "code"))
            else:
                out = out[1:-1]
                await Logger.info("Successfully said: '%s'" % paint.color(out, "code"))
        else:
            await Logger.info("Successfully said: '%s'" % out)
    else:
        await Logger.error("Doesn't accept empty messages.")
