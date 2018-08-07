import discord

async def ex(args, message, client, invoke):
    #args = args.__str__()[1:-1].replace("'", "")
    #args = args.__str__().replace(",", "")
    out = ""
    for word in args:
        out += word + " "
    await client.delete_message(message)
    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=(out)))
