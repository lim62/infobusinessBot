from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.lexicon import lexRU

def get_start_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=
                                    [
                                        [
                                            InlineKeyboardButton(text=lexRU.button.mailing, callback_data='mailing'),
                                            InlineKeyboardButton(text=lexRU.button.contacts, callback_data='contacts')
                                        ],
                                        [
                                            InlineKeyboardButton(text=lexRU.button.database, callback_data='database')
                                        ]
                                    ]
                                )

def get_cancel_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=
                                    [
                                        [
                                            InlineKeyboardButton(text=lexRU.button.cancel, callback_data='cancel')
                                        ]
                                    ]
                                )