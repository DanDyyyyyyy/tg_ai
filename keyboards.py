from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = [
            [
                types.KeyboardButton(text="Разговор по душам с роботом")],
                [types.KeyboardButton(text="Покажу тебе картинку, но не пошлую")]
            ]

KEYBOARD = types.ReplyKeyboardMarkup(
    keyboard=main_keyboard,
    resize_keyboard=True,
    input_field_placeholder="Ну выбери уже что-нибудь"
    )

inline_btn_ahaha = InlineKeyboardButton('ахахахаха', callback_data='button1')
INLINE_KB_AHAHA = InlineKeyboardMarkup().add(inline_btn_ahaha)
inline_btn_crap = InlineKeyboardButton('отстой(((', callback_data='button2')
INLINE_KB_CRAP = InlineKeyboardMarkup().add(inline_btn_crap)