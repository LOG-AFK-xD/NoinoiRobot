import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NoinoiRobot.events import register as MEMEK
from NoinoiRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/0afc9401213cab54fadca.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Hello I Am Azuka!** \n\n"
  LUNA += "✨ **I'm Working Properly** \n\n"
  LUNA += "✨ **My Master : [𐏓〬⃝ ⸙‌ٖٖٖٖٖٖٜٖٖٖٖٖٖ Official ➣LOG⛦ AFK xͮD ⸙‌ٖٖٖٖٖٖٜٖٖٖٖٖٖ ااـ꯭](https://T.ME/official_afk_xD)** \n\n"
  LUNA += f"✨ **Telethon Version : {tlhver}** \n\n"
  LUNA += f"✨ **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Thans For Adding Me Hear.**"
  BUTTON = [[Button.url("• Help", "https://t.me/azuka_robot?start=help"), Button.url("Creator •", "https://t.me/Piro_x_Power")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/cmd"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "✅ **Hear The Some Command For Azuka Music & Video & External Features 📌**"
  buttons = [
    [
        InlineKeyboardButton(text="Command 📚", callback_data="luna_"),
    ],
            ]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
