from utils import log, stringify, color
import discord
import asyncio


# openPolls = {
#     poll_id: {
#         "description":"Some important topic.",
#         "options":{
#             "Save The World": 3,
#             "Just Don't": 10,
#             "Maybe": 21
#         }
#     }
# }

# usersVoted = {
#     user.id:{
#         poll_id : option_string
#     }
# }

openPolls = {}
usersVoted = {}
unicodeEmojis = {1 :"\U00000031\U000020E3", 2 : "\U00000032\U000020E3", 3 : "\U00000033\U000020E3", 4 : "\U00000034\U000020E3", 5 : "\U00000035\U000020E3", 6 : "\U00000036\U000020E3"}


async def ex(args, message, client, invoke):
    exists = False
    try:
        poll_id = args[0]
    except IndexError:
        await log("You have to enter the poll's id, description and options.", "error", chat=True, chan=message.channel, client=client)
        return
    for key in openPolls:
        if poll_id == key:
            await log("Poll with same name already exists. Please choose another one.", "error", chat=True, chan=message.channel, client=client)
            exists = True
    if not exists:
        newentry = convert(args)
        if len(newentry[poll_id]["options"]) <= 6 and len(newentry[poll_id]["options"]) > 1:
            openPolls.update(newentry)
            out = "Vote With Reactions:`(id:%s)` \n" % poll_id + openPolls[poll_id]["description"] + "\n\n`Options`\n"
            num = 1
            for key in openPolls[poll_id]["options"]:
                out += unicodeEmojis[num] + "  " + key + " : " + str(openPolls[poll_id]["options"][key]) + "\n"
                num += 1
            poll = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description=out))
            uni = 1
            for key in openPolls[poll_id]["options"]:
                await client.add_reaction(poll, unicodeEmojis[uni])
                uni += 1
        elif len(newentry[poll_id]["options"]) < 2:
            await log("Can't create polls with less than two (2) options", "error", chat=True, chan=message.channel, client=client)
        else:
            await log("Can't create polls with more than six (6) options", "error", chat=True, chan=message.channel, client=client)


async def vote(message, user, client, reaction):
    try:
        content = message.embeds[0]["description"]
        start = content.find("id:") + 3
        end = content.find(")`")
        poll_id = content[start:end]
        emoji = reaction.emoji.encode("unicode_escape")
        option_number = int(str(emoji)[2])
        num = 1
        for key in openPolls[poll_id]["options"]:
            if num == option_number:
                option_string = key
            num += 1
        if user.id in usersVoted and poll_id in usersVoted[user.id]:
            old_option_number = 1
            for key in openPolls[poll_id]["options"]:
                if usersVoted[user.id][poll_id] == key:
                    old_option_string = key
                    break
                else:
                    old_option_number += 1
            content = changeMessage(content, -1, old_option_number, poll_id)
            openPolls[poll_id]["options"][old_option_string] -= 1
            out = changeMessage(content, 1, option_number, poll_id)
        else:
            out = changeMessage(content, 1, option_number, poll_id)
        openPolls[poll_id]["options"][option_string] += 1
        if user.id not in usersVoted:
            usersVoted.update({user.id: {poll_id:option_string}})
        else:
            usersVoted[user.id][poll_id] = option_string
        await client.edit_message(message, embed=discord.Embed(color=discord.Color.blue(), description=out))
        await client.remove_reaction(message, reaction.emoji, user)
    except (ValueError, KeyError):
        pass


def changeMessage(content, change_by, option_number, poll_id):
    num = 1
    for key in openPolls[poll_id]["options"]:
        if num == option_number:
            newmsg = list(content)
            start = content.find(key) + len(key) + 3
            if openPolls[poll_id]["options"][key] < 9:
                end = content.find(key) + len(key) + 4
            elif openPolls[poll_id]["options"][key] < 99:
                end = content.find(key) + len(key) + 5
            else:
                end = content.find(key) + len(key) + 6
            newnum = int("".join(newmsg[start:end])) + change_by
            if newnum >= 0:
                newnum = str(newnum)
                if openPolls[poll_id]["options"][key] == 9:
                    newmsg.insert(end, "\n")
                elif openPolls[poll_id]["options"][key] == 99:
                    newmsg.insert(end, "\n")
                index = 0
                for i in range(start,end):
                    newmsg[i] = newnum[index]
                    index += 1
                newmsg = "".join(newmsg)
            else:
                newmsg = content
        num += 1
    return newmsg



def convert(args):
    poll_id = args[0]
    args.remove(args[0])
    temp = []
    while not args[0].endswith('"'):
        temp.append(args[0])
        args.remove(args[0])
    temp.append(args[0])
    args.remove(args[0])
    description = stringify(temp)
    description = description.replace('"', "")
    options = []
    temp = stringify(args)
    options = temp.split('"')
    for e in options:
        if "[" in e or "," in e or "]" in e:
            options.remove(e)
    temp = {}
    for e in options:
        temp[e] = 0

    out = {poll_id: {"description": description, "options":temp}}
    return out
