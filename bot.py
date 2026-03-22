from flask import Flask
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, InputAudioStream, InputVideoStream
import os

API_ID = 37275832
API_HASH = "E802ea1204d1a9a217c180fa8c7f0352"
BOT_TOKEN = "8583078307:AAG1CmdKQEvCrhTdWK-v9gCswbgSV43ShNk"

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

@app.on_message(filters.command("play"))
async def play(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /play link")

    link = message.command[1]

    await message.reply("Downloading...")

    os.system(f"yt-dlp -o video.mp4 {link}")

    await call.join_group_call(
        message.chat.id,
        InputStream(
            InputAudioStream("video.mp4"),
            InputVideoStream("video.mp4")
        )
    )

    await message.reply("Streaming started 🔥")

app.start()
call.start()
app.idle()
import threading
from flask import Flask
app_web = Flask('')

@app_web.route('/')
def home():
    return "Bot is running!"

def run():
    app_web.run(host='0.0.0.0', port=10000)

threading.Thread(target=run).start()






