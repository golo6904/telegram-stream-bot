from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("37275832"))
API_HASH = os.environ.get("E802ea1204d1a9a217c180fa8c7f0352 ")
BOT_TOKEN = os.environ.get("8583078307:AAG1CmdKQEvCrhTdWK-v9gCswbgSV43ShNk")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🤖 Bot is working!\n\nUse /reel <link> to download Instagram reel.")

@app.on_message(filters.command("reel"))
async def reel(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /reel link")

    url = message.command[1]

    msg = await message.reply("📥 Downloading reel...")

    try:
        os.system(f"yt-dlp -o reel.mp4 {url}")

        if os.path.exists("reel.mp4"):
            await message.reply_video("reel.mp4", caption="🔥 Here is your reel")
            os.remove("reel.mp4")
            await msg.delete()
        else:
            await msg.edit("❌ Failed to download")

    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
from pyrogram import idle
import asyncio

async def main():
    await app.start()
    print("Bot started")
    await idle()

asyncio.run(main())
