import discord

colorList = ["red", "green", "blue", "orange"]

async def ex(args, message, client, invoke):
    roles = message.server.roles
    args = args.__str__()[1:-1].replace("'", "")
    args = args.__str__().replace(",", "")
    oldrole = hasRole(message)
    role = check(roles, args)

    if(not role == None):
        await client.add_roles(message.author, role)
    if(not oldrole == None):
        await client.remove_roles(message.author, oldrole)


def check(roles, args):
    for r in roles:
        if r.name == args:
            return r

def hasRole(message):
    for r in message.author.roles:
        if r.name in colorList:
            return r
