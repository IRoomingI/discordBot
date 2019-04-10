import discord
from utils import config


async def ex(args, message, client, invoke):
    invite_url = "https://discordapp.com/oauth2/authorize?client_id=%s&scope=bot&permissions=8" % client.user.id
    github_url = "https://github.com/IRoomingI/discordBot"
    rooming_avatar = "https://cdn.discordapp.com/avatars/239147465104818176/f602083b260afe220c9fe655ba22a448.webp?size=1024"
    rooming_invite = "https://discord.gg/NfGEYrU"
    bot_avatar = client.user.avatar_url

    embed = discord.Embed(title=client.user.name,
                          description="A Discord bot coded by **Rooming** aka BIG WEEB :D\nType `%shelp` to get help with the commands" % config.CONFIG["PREFIX"], color=0x2cc85e)
    embed.set_author(name="Rooming", url=rooming_invite,
                     icon_url=rooming_avatar)
    embed.set_thumbnail(url=bot_avatar)
    embed.add_field(name="Invite Link 🔗",
                    value="[Invite this bot to your guild 💯](%s)" % invite_url, inline=False)
    embed.add_field(name="Github Repo ⏫",
                    value="[Watch this project on Github or clone it yourself](%s)" % github_url, inline=False)
    await message.channel.send(embed=embed)
