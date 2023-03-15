import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards import KEYBOARD, INLINE_KB_AHAHA
from dallee import prompt, get_Image

from config import telegram_token, openai_api_key

token = telegram_token
openai.api_key = openai_api_key

bot = Bot(token)
dp = Dispatcher(bot)

messages = []


async def start_bot(_):
    print('Бот запущен, вот, не теряй ')


# получаем клавиатуру
def get_address_keyboard():
    get_keyboard = types.ReplyKeyboardMarkup(
        input_field_placeholder="Тыкни",
        one_time_keyboard=True
    )
    button = types.KeyboardButton(
        "тык сюда",
        request_location=True,
        one_time_keyboard=True)
    get_keyboard.add(button)
    return get_keyboard


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           """Привет! Я бот с ChatGPt, просто напиши мне сообщение и я что-нибудь тебе отвечу\n 
                           или выбери что-то из выпадающего списка""")
    await message.answer('Здесь можно выбрать мои дополнительные функции', reply_markup=KEYBOARD)


@dp.message_handler(text='Разговор по душам с роботом')
async def send(message: types.Message):
    messages.append({"role": "user", "content": message.text})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})

    await message.answer(completion.choices[0].message.content)


@dp.message_handler(text='Покажу тебе картинку, но не пошлую')
async def send(message: types.Message):
    #messages.append()
    await bot.send_message(message.from_user.id, get_Image(prompt))


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
