from pyrogram import filters, Client
from Cluster.sql import setWelcome

@Client.on_message(filters.command(["setwelcome"]) & filters.group & filters.reply)
async def setWelcome(client, message):
    if(message.reply_to_message):
        setWelcome(message.chat.id, message.reply_to_message)
        await message.reply_text("Successfully set the welcome message")
    else:
        await message.reply_text("reply to text")
       # message.text = " ".join(message.command[1:])
       # setWelcome(message.chat.id, message)
      #  await message.reply_text(f"Successfully set the welcome message to: {' '.join(message.command[1:])}")
