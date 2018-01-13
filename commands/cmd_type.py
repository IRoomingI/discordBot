import asyncio

async def ex(args, message, client, invoke):
    args = args.__str__()[1:-1].replace("'", "")
    args = args.__str__().replace(",", "")
    prev_msg = await client.send_message(message.channel, args[0])
    await client.delete_message(message)
    prev_cont = prev_msg.content
    for letter in range(1, len(args)):
        await asyncio.sleep(0.25)
        new_cont = prev_cont + args[letter]
        await client.edit_message(prev_msg, new_content=new_cont)
        prev_cont = new_cont
