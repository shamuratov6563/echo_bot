from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "6262625216:AAG4BZlsn8E2RQ20SGMXwhJwKuUQfdfVIFk"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)

# new
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(text="Qalaysan")


# @dp.message_handler()
# async def echo_answer(message: types.Message):
#     await message.answer(text=message.text.upper())


@dp.message_handler(Text(equals="commands"))
async def get_commands(message: types.Message):
    text = """
        /start - start bot
        /help - help command
    """
    await message.answer(text=text)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)

