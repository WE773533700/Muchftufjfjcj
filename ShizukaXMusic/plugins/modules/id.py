from ShizukaXMusic import app
from pyrogram import filters


@app.on_message(filters.command(["ايدي","ا","id"],""))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"◂ 𝙸𝙳 : »  `{message.from_user.id}`\n\n◂ 𝙸𝙳 𝙶𝚁𝙾𝚄𝙿 : » `{message.chat.id}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝙼𝙸𝚂𝚂𝙸𝙽𝙶 𝚆𝙾𝚁𝙳𝚂", url=f"https://t.me/FH_KP"),
                ],
                [  
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
@app.on_message(filters.command(["السورس","سورس"],""))
def sourc(client: Client, message: Message):
        photo=f"https://telegra.ph/file/10dfb95793ff3d40e0a90.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂 ♪\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [ᴋɪʙʀɪᴀ¹](t.me/FH_KN) \n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝚁𝙰𝚂𝙺𝙾²](t.me/AA969622) \n• ᴄʜᴀɴɴᴇʟ 𝙻𝙸𝙽𝙳𝙰 » [ᴄʜᴀɴɴᴇʟ](t.me/A1122ll)\n\n**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات لندا", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )    
