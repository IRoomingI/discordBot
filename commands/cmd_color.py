from utils import log
import asyncio

colorList = ["red", "green", "blue", "orange", "purple"]


def get_new_role(roles, args):
    for r in roles:
        if r.name == args:
            return r


def get_old_roles(message):
    out = []
    for r in message.author.roles:
        if r.name in colorList:
            out.append(r)
    return out


async def color_help(chan, client):
    msg = "All colors: "
    for element in colorList:
        if element is not colorList[-1]:
            msg += element + ", "
        else:
            msg += element + ", default"

    await log(msg, "info", chat=True, chan=chan, client=client, delete=False)


async def ex(args, message, client, invoke):
    roles = message.server.roles
    args = args[0] if len(args) > 0 else "help"
    args = args.lower()
    if args == "help":
        await color_help(message.channel, client)
    elif args == "default" or args == "clear":
        roles = get_old_roles(message)
        if len(roles) > 0:
            for r in roles:
                await client.remove_roles(message.author, r)
        await log("Successfully cleared color.", "info")
    else:
        oldrole = get_old_roles(message)
        role = get_new_role(roles, args)

        if role is not None:
            if len(oldrole) > 0:
                for r in oldrole:
                    await client.remove_roles(message.author, r)
            await asyncio.sleep(0.5)
            await client.add_roles(message.author, role)
            await log("Successfully changed to color: '%s'" % args, "info")
        else:
            if len(args) > 0:
                await log("Couldn't change to color because it doesn't exist: '%s'" % args, "error", chat=True, chan=message.channel, client=client)
            else:
                await color_help(message.channel, client)
