import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 1. API KEY-ро аз скриншоти аввалатон гузоред (ки бо ...3u20 тамом мешавад)
genai.configure(api_key="ИНҶО_API_KEY_ГУЗОРЕД")

# 2. Токени ботро аз @BotFather (Телеграм) гузоред
TELEGRAM_TOKEN = "ИНҶО_ТОКЕНИ_ТЕЛЕГРАМ_ГУЗОРЕД"

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
model = genai.GenerativeModel('gemini-1.5-flash')

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("🚀 Салом! Мавзӯъро навис, ман бароят цитатаи зур меёбам.")

@dp.message_handler()
async def send_quote(message: types.Message):
    await types.ChatActions.typing()
    prompt = f"Напиши мудрую пацанскую цитату на тему: {message.text}. Отвечай на языке запроса."
    try:
        response = model.generate_content(prompt)
        await message.reply(response.text)
    except:
        await message.answer("Хатогӣ шуд, боз кӯшиш кун.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
