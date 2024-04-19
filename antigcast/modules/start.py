import asyncio

from antigcast import Bot
from pyrogram import filters, enums
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from antigcast.config import *
from antigcast.helpers.database import *


CTYPE = enums.ChatType

# inline buttons
inlinegc = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Owner", url="http://t.me/rewe_anu"),
            InlineKeyboardButton(text="Channel", url="https://t.me/nunagabut2")
        ]
    ]
)

inline = InlineKeyboardMarkup(
    [
        [
                    InlineKeyboardButton(text="Daftarkan Grup", callback_data = "langganan")
        ],
        [
                    InlineKeyboardButton(text="Creator", url=f"https://t.me/rewe_anu"),
                    InlineKeyboardButton(text="Channel", url="https://t.me/nunagabut2") 
        ]
    ]
)

def add_panel(username):
    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Tambahkan Ke Group", url=f"https://t.me/{username}?startgroup=appstart")
            ]
        ]
    )

    return button

def admin_panel():
    buttons = [
        [
            InlineKeyboardButton(text="Hubungi Owner", url=f"https://t.me/rewe_anu")
        ],
    ]

    return buttons

@Bot.on_message(filters.command("start"))
async def start_msgmessag(app : Bot, message : Message):
    bot = await app.get_me()
    username = bot.username
    user = message.from_user.mention
    chat_type = message.chat.type
    if chat_type == CTYPE.PUBLICK:
        msg = f"👋🏻 hai anak anjeng {user}!\n\nBot ini akan menghapus pesan gcast ya anjg tambahin bot ini jadi amin do group lu yang yang ga seberapa itu ya monyet."
        try:
            await message.reply(text=msg, reply_markup=inline)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply(text=msg, reply_markup=inline)
    elif chat_type in [CTYPE.GROUP, CTYPE.SUPERGROUP]:
        msg = f"**woy anjg!**\n\n__minimal adminin gua lah, biar gcast nya ga masuk ke group sampah lo ngentod!__\n\nCreated by @rewe_anu"
        
        try:
            await message.reply(text=msg, reply_markup=inlinegc)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply(text=msg, reply_markup=inlinegc)

@Bot.on_callback_query(filters.regex(r"close"))
async def close_cbq(client: Bot, query: CallbackQuery):
    try:
        await query.message.reply_to_message.delete()
        await client.send_message(query.from_user.id, "**Pendaftaran Dibatalkan anjg**")
    except:
        pass
    try:
        await query.message.delete()
        await client.send_message(query.from_user.id, "**Pendaftaran Dibatalkan anjg**")
    except:
        pass

#edit harganya

@Bot.on_callback_query(filters.regex(r"langganan"))
async def bayar_cbq(client: Bot, query: CallbackQuery):
    btn = InlineKeyboardMarkup(admin_panel())
    text = """**Silahkan pilih lu mau yang berapa bulan anjg **

1 Bulan : `Rp. 25.000,-`  
3 Bulan : `RP. 75.000,-`"""
    await query.edit_message_text(
        text = text,
        reply_markup = btn
    )
