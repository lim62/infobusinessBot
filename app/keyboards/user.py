from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.lexicon import lexRU

def get_final_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=\
                                    [
                                        [
                                            InlineKeyboardButton(text=lexRU.button.contact, url='https://t.me/shtankomedia'),
                                            InlineKeyboardButton(text=lexRU.button.reviews, url='https://t.me/teletemprivate')
                                        ]
                                    ]
                                )