import os
import re

import yt_dlp
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaAudio,
    InputMediaVideo,
    Message,
)

from config import BANNED_USERS, SONG_DOWNLOAD_DURATION, SONG_DOWNLOAD_DURATION_LIMIT
from strings import get_command
from ShizukaXMusic import YouTube, app
from ShizukaXMusic.utils.decorators.language import language, languageCB
from ShizukaXMusic.utils.formatters import convert_bytes
from ShizukaXMusic.utils.inline.song import song_markup

# Command
SONG_COMMAND = get_command("SONG_COMMAND")


@app.on_message(
    filters.command(SONG_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@language
async def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("- **ابشر جاري البحث ..**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("- **للاسف ما اثرت على شي تأكد من كتابة اسم الفنان مع الاغنية**")
        print(str(e))
        return
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**✧ [𝘀𝗼𝘂𝗿𝗰𝗲 𝗹𝗶𝗻𝗱𝗮](t.me/FH_KP)**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("- **جاري لتحميـل ..**")
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("خطأ ، تواصل مع مطور البوت - @FH_KN")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@app.on_message(filters.regex('^(.*) !!'))
def song232(_, message):
  text = message.text
  if '!!!' in text:
      print("Error")
  else:
    g = text.split(" ")
    query = str(g[0])
    m = message.reply("🔎")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("✗ لم اجد شيئا.\n\nاعطني اسم المغني كامل.")
        print(str(e))
        return
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**- Ch** [تحديثات لندا ♪](t.me/FH_KP)"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("- **جاري التحميـل ..**")
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("خطأ ، تواصل مع مطور البوت")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
