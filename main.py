import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5447819631:AAHj4uaV5K3RiNY90bI3_96QghhaStAMMTk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    user = message.from_user.full_name
    await message.reply(f"Salom {user}  Wikipedia Bot ga xush kelibsiz! \nMen sizga istalgan mavzudagi maqolani topib beraman. \n\nQayta boshlash - /start \nYordam olish uchun - /help")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    user = message.from_user.full_name
    await message.reply(f"Hurmatli {user} \nMaqola mavzusini o'zbek tilida va lotin alifbosida kiriting! \nSo'zlarni imlo jihatdan to'g'ri yozing, aks xolda maqola topilmasligi mumkin! \nBot haqida savol yoki taklifingiz bo'lsa @Bekjon_Buriboyev ga yozishingiz mumkin!")


@dp.message_handler()
async def sendWiki(message: types.Message):
    wikipedia.set_lang('uz')
    try:
        res = wikipedia.summary(message.text)
        await message.reply(res)
    except:
        await message.reply("Bu mavzuga oid maqola topilmadi 😔")    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)