import asyncio
import random

from userbot import CMD_HELP
from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


que = {}


@bot.on(admin_cmd(incoming=True))
@bot.on(sudo_cmd(incoming=True, allow_sudo=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    counter = int(random.choice(REBELBOT.NUMBER))
    if counter == 0:
        async with event.client.action(event.chat_id, "typing"):
            await event.client.send_message(
                entity=event.chat_id,
                message="""{}""".format(random.choice(REBELBOT.RRAID)),
                reply_to=event.message.id,
            )
    if counter == 1:
        caption = random.choice(REBELBOT.RRAID)
        async with event.client.action(event.chat_id, "typing"):
            await event.client.send_message(event.chat_id, caption)


@bot.on(admin_cmd(pattern="replyraid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="replyraid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")


@bot.on(admin_cmd(pattern="dreplyraid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="dreplyraid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")


CmdHelp("replyraid").add_command(
  "replyraid", "<username>", "Replies the user globally on every chat with random abuses.",
).add_command(
    "dreplyraid", "<username>", "Deactivates the reply raid."
).add()