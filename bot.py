import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, filename= 'mylog.log')

def russian_text_to_english(text):
    lower_rus = ['а','б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 
                            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ъ', 'э', 'ю', 'я', 'ь']
    lower_en = ['a','b', 'v', 'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 'o', 
                            'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', 'y', 'ie', 'e', 'iu', 'ia', '']
    upper_rus = [x.upper() for x in lower_rus]
    upper_en = [x.upper() for x in lower_en]
    lower_rus_to_en = dict(zip(lower_rus, upper_en))
    upper_rus_to_en = dict(zip(upper_rus, upper_en))
    result = []
    for word in text.split():
        new_word = []
        for letter in word:
            if letter.isalpha and letter not in lower_rus and letter not in upper_rus:
                return f'Бот предназначен для перевода инициалов написанных на кириллице на латиницу. В строке "{text}" присутствует слово "{word}", которое содержит символ "{letter}", не относящийся к кириллице!!!'
            if letter in lower_rus:
                new_word.append(lower_rus_to_en[letter])
            else:
                new_word.append(upper_rus_to_en[letter])
        result.append(''.join(new_word))
    return ' '.join(result)

@dp.message(Command(commands=['start']))
async def processing_command_start(message: Message):
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_full_name}!\nДля перевода ФИО на латиницу, напиши фамилию, имя и отчество через пробел.'
    logging.info(f'{user_full_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_answer(message: Message):
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_full_name} {user_id}: {text}')
    await message.answer(text=russian_text_to_english(text))


if __name__ == '__main__':
    dp.run_polling(bot)