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
                        InlineKeyboardButton("π‘ HELP", callback_data="help_data"),
                        InlineKeyboardButton("π ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton("π½ π²πΈπ½π΄π·ππ±", url="https://t.me/cinehub_family"),
                        InlineKeyboardButton("π SHARE US", url="https://telegram.me/share/url?url=https://t.me/cinehub_family"),
                    ],
                    [
                        InlineKeyboardButton("β Add Me to a Group β", url="http://t.me/CINEHUB_Searching_2_bot?startgroup=start"),
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
                        InlineKeyboardButton("β¬οΈ BACK", callback_data="start_data"),
                        InlineKeyboardButton("π ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "π½ π²πΈπ½π΄π·ππ± α΄α΄α΄α΄α΄Ι΄Ιͺα΄Κ", url="https://t.me/cinehub_family")
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
                        InlineKeyboardButton("β¬οΈ BACK", callback_data="help_data"),
                        InlineKeyboardButton("π START", callback_data="start_data"),
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command('sinhala_sub'))
async def play(bot, message):
    msg = await message.reply("πΏ **Movie | Series time**\n\n\nπ¬ ΰΆΰΆ±ΰ·ΰΆ± ΰΆΰΆ­ΰ·ΰΆ±ΰ· ΰΆΰΆΊΰΆ½ΰΆΰ· ΰΆ΄ΰ·ΰ·ΰ·ΰ·ΰΆ§ ΰΆΰΆ΄ΰ· ΰ·ΰ·ΰΆΰ·ΰΆ½ ΰΆΰΆ΄ΰ·ΰ·ΰΆ»ΰ·ΰ·ΰ· ΰΆΆΰ·ΰΆ§ΰ· ΰΆΰ·ΰΆ±ΰ·ΰΆΰ·ΰ·ΰΆ­ΰ· ΰ·ΰΆ―ΰΆ½ΰ· ΰΆ­ΰ·ΰΆΊΰ·ΰΆ±ΰ·ΰ· \n\nΰΆΰΆ»ΰΆ±ΰ·ΰΆ± ΰΆ­ΰ·ΰΆΊΰ·ΰΆ±ΰ·ΰΆ±ΰ· ΰΆΈΰ· ΠΌΟΞ½ΞΉΡ | ΡΞ½ ΡΡΡΞΉΡΡ ΰΆΆΰ·ΰΆ§ΰ·ΰ· ΰΆΰΆΊΰ· ΰΆ΄ΰ·ΰ·ΰΆ ΰ·ΰΆ ΰ· ΰΆΰΆ»ΰΆ΄ΰ· ΰ·ΰ·ΰΆ―ΰ·ΰΆΊΰΆ§ΰΆΈ α΄α΄α΄ Ιͺα΄ ΰΆΰΆΰ· ΰ·ΰ· sα΄ΚΙͺα΄s ΰΆΰΆΰ· Name ΰΆΰΆ English ΰ·ΰΆ½ΰ·ΰΆ±ΰ· type ΰΆΰΆ»ΰΆ± ΰΆΰΆΰΆΊΰ· \n\n\nβ‘ **ΰΆΰΆ΄ΰ·ΰ·ΰΆ»ΰ·ΰ·ΰ· Κα΄α΄; @sub_searcher_bot** \n\n\n<a href='https://t.me/sub_searcher_bot'>π€</a> | Powered By; Β© <a href='https://t.me/cinehub_family'>π²πΈπ½π΄π·ππ±</a>", quote=True)
    msg = await message.reply("π")

@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...β³", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'π Saved files: {total} \n\n Boss ΰΆ­ΰ· Movie & Series ΰΆ§ΰ·ΰΆΰΆΰ· Add ΰΆΰΆ½ΰ· ΰΆ±ΰΆΈΰ· ΰ·ΰΆ»ΰ·ΰΆ±ΰ· π')
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
