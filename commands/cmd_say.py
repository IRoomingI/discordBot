import discord

async def ex(args, message, client, invoke):
    out = ""
    for word in args:
        out += word + " "
    await client.delete_message(message)
    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=(out)))
