#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💡 HELP", callback_data="help_data"),
                        InlineKeyboardButton("📕 ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton("📽 🄲🄸🄽🄴🄷🅄🄱", url="https://t.me/cinehub_family"),
                        InlineKeyboardButton("🔀 SHARE US", url="https://telegram.me/share/url?url=https://t.me/cinehub_family"),
                    ],
                    [
                        InlineKeyboardButton("➕ Add Me to a Group ➕", url="http://t.me/CINEHUB_Searching_2_bot?startgroup=start"),
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⬅️ BACK", callback_data="start_data"),
                        InlineKeyboardButton("📕 ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "📽 🄲🄸🄽🄴🄷🅄🄱 ᴄᴏᴍᴍᴜɴɪᴛʏ", url="https://t.me/cinehub_family")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⬅️ BACK", callback_data="help_data"),
                        InlineKeyboardButton("🔄 START", callback_data="start_data"),
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command('sinhala_sub'))
async def play(bot, message):
    msg = await message.reply("🍿 **Movie | Series time**\n\n\n🎬 ඔන්න ඉතින් ඔයලගෙ පහසුවට අපි සිංහල උපසිරැසි බොට් කෙනෙක්වත් හදලා තියෙනවා \n\nකරන්න තියෙන්නෙ මේ мσνιє | тν ѕєяιєѕ බොට්ව ඔයා පවිච්චි කරපු විදියටම ᴍᴏᴠɪᴇ එකේ හෝ sᴇʀɪᴇs එකේ Name එක English වලින් type කරන එකයි \n\n\n⚡ **උපසිරැසි ʙᴏᴛ; @sub_searcher_bot** \n\n\n<a href='https://t.me/sub_searcher_bot'>🤖</a> | Powered By; © <a href='https://t.me/cinehub_family'>🄲🄸🄽🄴🄷🅄🄱</a>", quote=True)
    msg = await message.reply("😇")

@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total} \n\n Boss තව Movie & Series ටිකක් Add කලා නම් හරිනේ 😜')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))
