from aiogram import Bot,Dispatcher, executor,types
from aiogram.dispatcher.filters import Text
from config import *
from keyboard import *
from random import *

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)


async def on_startup(_):
    print('The bot is working')

@dp.message_handler(commands=['start'])
async def cmd_start(message:types.Message):
    await message.answer(text=START_TEXT,reply_markup=kb)

@dp.message_handler(commands=['help'])
async def cmd_start(message:types.Message):
    await message.answer(text=HELP_TEXT)

@dp.message_handler(commands=['description'])
async def cmd_start(message:types.Message):
    await message.answer(text=DESCRIPTION_TEXT)

@dp.message_handler(commands=['start_signing'])
async def start(message: types.Message):
    await message.answer(text='Напишіть своє ПІБ та вік через кому')

@dp.message_handler(commands=['choose_license_type'])
async def start(message: types.Message):
    await message.answer('Оберіть тип прав натиснувши на кнопку Вид Прав', reply_markup=kb1)

@dp.message_handler(Text(equals='Вид Прав'))
async def license_type_check(message: types.Message):
    await message.answer(text=license_type,reply_markup=kbp)
    await message.answer('Ви завершили реєстрацію. Натисніть на команду /help щоб отримати подальшу інформацію.')

@dp.callback_query_handler()
async def license_type_check(callback: types.CallbackQuery):
    if callback.data == "button_a":
        await callback.answer("мотоцикли, прекрасний вибір")
    elif callback.data == "button_b":
        await callback.answer("легкові автомобілі, прекрасний вибір")
    elif callback.data == "button_c":
        await callback.answer("грузові автомобілі, прекрасний вибір")
    elif callback.data == "button_d":
        await callback.answer("пассажирскі автобусы, прекрасний вибір")
    elif callback.data == "button_be":
        await callback.answer("легкові авто з прицепом, прекрасний вибір")
    elif callback.data == "button_ce":
        await callback.answer("автогрузові  з прицепом, прекрасний вибір")
    elif callback.data == "button_de":
        await callback.answer("пассажирські автобусы з прицепом, прекрасний вибір")

@dp.message_handler(commands=["location"])
async def send_location(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=50.5132, longitude=30.4965)

@dp.message_handler(commands=['photo_of_school'])
async def send_school_photo(message: types.Message):
        await bot.send_photo(chat_id=message.chat.id,
                             photo=choice(PHOTO_LIST))

@dp.message_handler(commands=['colleagues'])
async def send_info_colleagues(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://mc.today/wp-content/uploads/2023/12/Maksym-Gorbatok.jpg')
    await message.answer(text=collegi[1])
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://img.freepik.com/free-photo/portrait-of-young-beautiful-businesswoman-smiling_176420-9911.jpg')
    await message.answer(text=collegi[2])
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://mc.today/wp-content/uploads/2023/10/Dmytro-Lashin.jpg')
    await message.answer(text=collegi[3])
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://images.kinorium.com/movie/shot/777549/h280_39287910.jpg?21575999024')
    await message.answer(text=collegi[4])

@dp.message_handler()
async def pib_control(message: types.Message):
    data = message.text.split(',')
    if len(data[0].split()) == 3 and data[1].strip().isdigit():
        if int(data[1])>=18:
            await message.answer(text=f'{data[0]} - {data[1]}. Ви зареєстровані.Натисніть на команду /choose_license_type ')
        else:
            await message.answer(text=f'Ви за маленькі щоб поступити в нашу школу.')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           allowed_updates=["message", "inline_query", "callback_query"])

