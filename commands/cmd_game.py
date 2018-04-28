import discord

async def ex(args, message, client, invoke):
    args = args.__str__()[1:-1].replace("'", "")
    args = args.__str__().replace(",", "")
    await client.change_presence(game=discord.Game(name=args))
