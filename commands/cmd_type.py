import asyncio


async def ex(args, message, client, invoke):
    out = ""
    for word in args:
        out += word + " "
    prev_msg = await client.send_message(message.channel, out[0])
    await client.delete_message(message)
    prev_cont = prev_msg.content
    for letter in range(1, len(out)):
        await asyncio.sleep(0.25)
        new_cont = prev_cont + out[letter]
        await client.edit_message(prev_msg, new_content=new_cont)
        prev_cont = new_cont
