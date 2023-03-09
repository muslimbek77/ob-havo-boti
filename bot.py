from aiogram.types import Message, User, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
from aiogram import Router, Dispatcher, Bot
from aiogram.filters.command import Command
from asyncio import run
from abc import ABC, abstractmethod
from weather import get_date
from config import BOT_TOKEN

City = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text='Tashkent',callback_data='Tashkent'),
        InlineKeyboardButton(text='Fergana',callback_data='Fergana'),
        InlineKeyboardButton(text='Andijan',callback_data='Andijan'),
    ],
    [
        InlineKeyboardButton(text='Namangan',callback_data='Namangan'),
        InlineKeyboardButton(text='Qashqadaryo',callback_data='Qashqadaryo'),
        InlineKeyboardButton(text='Sirdaryo',callback_data='Sirdaryo'),
    ],
        ],
)

greet = Router()

@greet.message(Command(commands=["start"]))
async def greet_message(msg: Message, bot: Bot):
    await msg.answer("Bu 12 viloyat ob-havo ma'lumoti boti ⛅️",reply_markup=City)

@greet.callback_query()
async def get_weather(call: CallbackQuery):
  city = call.data
  weather = round(get_date(city),2)
  await call.answer(f"{weather}°C")




async def start():
    dp = Dispatcher()
    bot = Bot(BOT_TOKEN)
    dp.include_router(greet)
    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()

if __name__ == "__main__":
    run(start())