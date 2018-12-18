import discord, uuid, Logger, copy


# openPolls = {
#     poll_id : ---> Poll Class <---
#         description = "Some text right here",
#         message = message,
#         creator = creator.id,
#         voters = {1: [user1.id, user2.id], 2: [user3.id], 3: []}
#         options = {
#             1 : "Option text here...",
#             2 : "Another option here..."
# }

openPolls = {}
unicodeEmojis = {1: "\U00000031\U000020E3", 2: "\U00000032\U000020E3", 3: "\U00000033\U000020E3", 4: "\U00000034\U000020E3", 5: "\U00000035\U000020E3", 6: "\U00000036\U000020E3"}
closed = ["\U0001f1e8", "\U0001f1f1", "\U0001f1f4", "\U0001f1f8", "\U0001f1ea", "\U0001f1e9"]


class Poll:
    def __init__(self, desc, options):
        self.description = desc
        self.options = options
        self.message = None
        self.creator = None
        self.voters = {}
        for num in options:
            self.voters.update({num : []})

    def add_voter(self, user, vote):
        self.voters[vote].append(user.id)


async def ex(args, message, client, invoke):
    if len(args) > 0:
        poll_id, new_poll = generate_poll(args)
        if 6 >= len(new_poll.options) > 1:
            out = "Vote With Reactions: \n\n**" + new_poll.description + "**\n\n`Options`\n"
            for key in new_poll.options:
                out += unicodeEmojis[key] + "  " + new_poll.options[key] + " : **0**\n"
            poll = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description=out))
            new_poll.message = poll
            new_poll.creator = message.author.id
            openPolls.update({poll_id: new_poll})
            for uni in new_poll.options:
                await client.add_reaction(poll, unicodeEmojis[uni])
            await Logger.info("Successfully created poll with uuid '%s'." % poll_id)
        elif len(new_poll.options) < 2:
            await Logger.error("Can't create polls with less than two (2) options.", chat=True, chan=message.channel)
        else:
            await Logger.error("Can't create polls with more than six (6) options.", chat=True, chan=message.channel)
    else:
        await Logger.error("You need to enter the poll's description and its options.", chat=True, chan=message.channel)



async def vote(message, user, client, reaction):
    poll_id = get_poll_id(message)
    poll = openPolls[poll_id]
    already_voted = False
    for users in poll.voters.values():
        if user.id in users:
            already_voted = True
    if reaction.emoji in unicodeEmojis.values() and not already_voted:
        emoji = reaction.emoji.encode("unicode_escape")
        content = message.embeds[0]["description"]
        option_number = int(str(emoji)[2])
        old_votes = copy.deepcopy(poll.voters)
        poll.add_voter(user, option_number)
        await client.edit_message(message, embed=discord.Embed(color=discord.Color.blue(), description=change_message(content, poll_id, old_votes)))
    elif reaction.emoji == "\U0000274C":
        if user.id == poll.creator:
            await close_poll(message, client)
    await client.remove_reaction(message, reaction.emoji, user)


def get_poll_id(message):
    for poll_id in openPolls:
        if openPolls[poll_id].message.id == message.id:
            return poll_id


async def close_poll(message, client):
    poll_id = get_poll_id(message)
    await client.clear_reactions(openPolls[poll_id].message)
    for e in closed:
        await client.add_reaction(openPolls[poll_id].message, e)
    await Logger.info("Successfully closed poll '%s'." % poll_id)


def change_message(content, poll_id, old_votes):
    newmsg = content
    for option_number in openPolls[poll_id].options:
        votes = len(openPolls[poll_id].voters[option_number])
        if len(old_votes[option_number]) != votes:
            string = openPolls[poll_id].options[option_number]
            newmsg = list(newmsg)
            start = content.find(string) + len(string) + 5
            end = start + len(str(votes))
            if votes == 10:
                newmsg.insert(end - 1, " ")
            elif votes == 100:
                newmsg.insert(end - 1, " ")
            for i in range(start,end):
                newmsg[i] = str(votes)[i - start]
            newmsg = "".join(newmsg)
    return newmsg


def generate_poll(args):
    poll_id = str(uuid.uuid4())
    temp = " ".join(args).split('"')
    for i in temp:
        if i in ["", " ", " [", "]", ", "]:
            temp.remove(i)
    description = temp[0]
    no_dupes = []
    for e in temp[1:]:
        if e not in no_dupes:
            no_dupes.append(e)
    options = {}
    for e in range(1, len(no_dupes) + 1):
        options[e] = temp[e]
    return poll_id,  Poll(description, options)
