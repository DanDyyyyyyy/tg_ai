from asyncio import exceptions

import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher#, FSMContext
from aiogram.utils import executor
from keyboards import KEYBOARD, INLINE_KB_REPEAT, INLINE_KB_CRAP
from dallee import prompt, get_Image
#from dallee import get_Image

from aiogram.utils.markdown import hide_link

from config import telegram_token, openai_api_key

token = telegram_token
openai.api_key = openai_api_key

bot = Bot(token)
dp = Dispatcher(bot)

messages = []

async def start_bot(_):
    print('Бот запущен, вот, не теряй')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Привет! Выбери, что именно ты бы хотел получить от меня. Приятный разговор или отменный рисунок.")
    await message.answer('Здесь можно выбрать мои дополнительные функции', reply_markup=KEYBOARD)
    # удаляем клавиатуру
    # try:
    #     # Пытаемся удалить кнопку
    #     await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    # except exceptions.MessageToDeleteNotFound:
    #     # Если кнопка уже удалена, то продолжаем выполнение кода
    #
    #     pass


# Чат бот # все работает - верни
# @dp.message_handler(text='Разговор по душам с роботом')
# #@dp.message_handler()
# async def send(message: types.Message):
#     await bot.send_message(message.from_user.id)
#     messages.append({"role": "user", "content": message.text})
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )
#     response = completion.choices[0].message.content
#     messages.append({"role": "assistant", "content": response}) #здесь response позволяет не терять контекст
#
#     await message.answer(completion.choices[0].message.content)

#затычка для первой кнопки
@dp.message_handler(text = 'Разговор по душам с роботом')
async def process_guess_int_command(message: types.Message):
    await message.reply('Все работает, но это временная затычка, ибо кнопки пока не очень дружат', reply_markup=INLINE_KB_CRAP)


#Получение изображения
@dp.message_handler(text='Покажу тебе картинку, но не пошлую') #декоратор - действие, которое его вызывает
@dp.message_handler()
async def send(message: types.Message):
    prompt = message.text
    await bot.send_photo(chat_id=message.chat.id, photo=get_Image(prompt))


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
