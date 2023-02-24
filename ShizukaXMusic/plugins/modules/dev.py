from ShizukaXMusic import app
from pyrogram import filters


@app.on_message(filters.command(["مطور","المطور"]))
    usr = await client.get_users(DEV_BOT)
    name = usr.first_name
    user = await client.get_chat(DEV_BOT)
    Bio = user.bio
    async for photo in client.iter_profile_photos(DEV_BOT, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""Ⴆ᥆ƚ ᥆᭙ꪀᥱᖇ | - [{usr.first_name}](https://t.me/{USER_OWNER}) 🕷
                        
υ᥉ᥱᖇ ᥆᭙ꪀᥱᖇ | - @{USER_OWNER} 🕷
                         
ႦᎥ᥆ | - {Bio} 🕷        

Ꭵժ | - {DEV_BOT} 🕷 """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{USER_OWNER}")
            ],                   
          ]              
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(DEV_BOT, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
                    if await is_on_off(config.LOG):
                       return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}",
                       )                    
