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
