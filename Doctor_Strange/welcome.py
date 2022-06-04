from pyrogram import filters


@app.on_message(filters.command(["setwelcome"]) & filters.group)
async def setWelcome(client, message):
    if(message.reply_to_message):
        DB.groups.setWelcome(message.chat.id, message.reply_to_message)
        await message.reply_text("Successfully set the welcome message")
    else:
        message.text = " ".join(message.command[1:])
        DB.groups.setWelcome(message.chat.id, message)
        await message.reply_text(f"Successfully set the welcome message to: {' '.join(message.command[1:])}")

