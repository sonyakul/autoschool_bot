from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/description')
kb.add(b1,b2)

kbp = InlineKeyboardMarkup(row_width=2)
bp1 = InlineKeyboardButton(text='A',callback_data='button_a')
bp2 = InlineKeyboardButton(text='B',callback_data='button_b')
bp3 = InlineKeyboardButton(text='C',callback_data='button_c')
bp4 = InlineKeyboardButton(text='D',callback_data='button_d')
bp5= InlineKeyboardButton(text='BE',callback_data='button_be')
bp6 = InlineKeyboardButton(text='CE',callback_data='button_ce')
bp7 = InlineKeyboardButton(text='DE',callback_data='button_de')
kbp.add(bp1,bp2).add(bp3,bp4).add(bp5).add(bp6,bp7)

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b_1 = KeyboardButton(text='Вид Прав')
kb1.add(b_1)

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
b_photo = KeyboardButton(text="Фото школи")
kb_photo.add(b_photo)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b1_1 = KeyboardButton(text='/help')
kb2.add(b1_1)




