from utils import log, stringify
import discord


# openPolls = {
#     poll_id : {
#         "description" : "Some text right here",
#         "message" : message,
#         "voters": {user1.id : 2, user2.id : 1, user3.id : 2}
#         "options" : {
#             1 : "Option text here...",
#             2 : Another option here..."
#          }
#     }
# }


openPolls = {}
unicodeEmojis = {1: "\U00000031\U000020E3", 2: "\U00000032\U000020E3", 3: "\U00000033\U000020E3", 4: "\U00000034\U000020E3", 5: "\U00000035\U000020E3", 6: "\U00000036\U000020E3"}
closed = ["\U0001f1e8", "\U0001f1f1", "\U0001f1f4", "\U0001f1f8", "\U0001f1ea", "\U0001f1e9"]


async def ex(args, message, client, invoke):
    if invoke == "poll":
        if len(args) > 0:
            poll_id = args[0]
            if poll_id not in openPolls:
                newentry = convert(args)
                if 6 >= len(newentry[poll_id]["options"]) > 1:
                    openPolls.update(newentry)
                    out = "Vote With Reactions:`(id:%s)` \n\n" % poll_id + "**" + openPolls[poll_id]["description"] + "**\n\n`Options`\n"
                    for key in openPolls[poll_id]["options"]:
                        out += unicodeEmojis[key] + "  " + openPolls[poll_id]["options"][key] + " : **0**\n"
                    poll = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description=out))
                    openPolls[poll_id]["message"] = poll
                    for uni in openPolls[poll_id]["options"]:
                        await client.add_reaction(poll, unicodeEmojis[uni])
                    await log("Successfully created poll '%s'" % poll_id, "info")
                elif len(newentry[poll_id]["options"]) < 2:
                    await log("Can't create polls with less than two (2) options.", "error", chat=True, chan=message.channel, client=client)
                else:
                    await log("Can't create polls with more than six (6) options.", "error", chat=True, chan=message.channel, client=client)
            else:
                await log("Poll with same name already exists. Please choose another one.", "error", chat=True, chan=message.channel, client=client)
        else:
            await log("You need to enter the poll's id, description and options.", "error", chat=True, chan=message.channel, client=client)
    else:
        if len(args) > 0:
            poll_id = args[0]
            if poll_id in openPolls:
                await client.clear_reactions(openPolls[poll_id]["message"])
                for e in range(len(closed)):
                    await client.add_reaction(openPolls[poll_id]["message"], closed[e])
                await log("Successfully closed poll '%s'." % poll_id, "info", chat=True, chan=message.channel, client=client)
            else:
                await log("The poll you entered doesn't exist.", "error", chat=True, chan=message.channel, client=client)
        else:
            await log("You need to enter the poll's id you want to close.", "error", chat=True, chan=message.channel, client=client)
        del openPolls[poll_id]


async def vote(message, user, client, reaction):
    try:
        content = message.embeds[0]["description"]
        start = content.find("id:") + 3
        end = content.find(")`")
        poll_id = content[start:end]
        emoji = reaction.emoji.encode("unicode_escape")
        option_number = int(str(emoji)[2])
        if user.id in openPolls[poll_id]["voters"]:
            old_option_number = openPolls[poll_id]["voters"][user.id]
            content = change_message(content, -1, old_option_number, poll_id)
            del openPolls[poll_id]["voters"][user.id]
            out = change_message(content, 1, option_number, poll_id)
        else:
            out = change_message(content, 1, option_number, poll_id)
        openPolls[poll_id]["voters"].update({user.id : option_number})
        await client.edit_message(message, embed=discord.Embed(color=discord.Color.blue(), description=out))
        await client.remove_reaction(message, reaction.emoji, user)
    except (ValueError, KeyError):
        pass


def change_message(content, change_by, option_number, poll_id):
    string = openPolls[poll_id]["options"][option_number]
    newmsg = list(content)
    start = content.find(string) + len(string) + 5
    votes = 0
    for v in openPolls[poll_id]["voters"]:
        if openPolls[poll_id]["voters"][v] == option_number:
            votes += 1
    if votes <= 9:
        end = content.find(string) + len(string) + 6
    elif votes < 99:
        end = content.find(string) + len(string) + 7
    else:
        end = content.find(string) + len(string) + 8
    newnum = votes + change_by
    if newnum >= 0:
        newnum = str(newnum)
        if votes == 9:
            newmsg.insert(end, "\n")
        elif votes == 99:
            newmsg.insert(end, "\n")
        index = 0
        for i in range(start,end):
            newmsg[i] = newnum[index]
            index += 1
        newmsg = "".join(newmsg)
    else:
        newmsg = content
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
    temp = stringify(args)
    options = temp.split('"')
    for e in options:
        if "[" in e or "," in e or "]" in e:
            options.remove(e)
    ndo = []
    for e in options:
        if e not in ndo:
            ndo.append(e)
    temp = {}
    for e in range(len(ndo)):
        temp[e + 1] = options[e]

    out = {poll_id: {"description": description, "voters": {}, "options": temp}}
    return out
