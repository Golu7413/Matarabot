#CREATED BY @KIRITO1240
#API CREDITS: @KIRITO1240
#PROVIDED BY https://github.com/Team-ProjectCodeX

#IMPORTS
import requests as r
from pyrogram import *
from pyrogram.types import *

#BOT FILE IMPORTS
#Name -> Your Bots File Name (Eg. From Liaa import pbot as app)
from pyrogram import Client as app


#AI IMAGE GENERATION FUNCTION
@app.on_message(filters.command("aigen"), group=95)
async def generateai(_, message):
    if len(message.text.split()) < 2:
        return await message.reply_text("No Prompt Given!")
    textt = message.text.split(maxsplit=1)[1]
    b = await message.reply("Wait For 1-2 Mins Generating Your Image...")
    
    resp = r.post("https://novax-api-7c5f1d45a2f2.herokuapp.com/ai", json={'type' : "aai", "prompt" : f"{textt}","auth_key" : "Yash_Yash__@"}).json()
    
    a = resp['image_url']
    await message.reply_photo(a, caption=f"**Generated BY:** @{app.me.username}\nCredits: @NovaXMod")
    await b.delete()