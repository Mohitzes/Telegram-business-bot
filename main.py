import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
ADMIN_ID = 0

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

db_orders = {
    "1402": {"status": "Pending", "client": "User_A"},
    "1403": {"status": "In Progress", "client": "User_B"}
}

@dp.message(Command("start"))
async def start(msg: types.Message):
    kb = [
        [types.KeyboardButton(text="📦 Orders"), types.KeyboardButton(text="📊 Stats")],
        [types.KeyboardButton(text="➕ New Order"), types.KeyboardButton(text="⚙️ Admin")]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await msg.answer("🔥 System initialized. Use menu.", reply_markup=markup)

@dp.message()
async def router(msg: types.Message):
    if msg.text == "📦 Orders":
        await msg.answer(f"📋 Active: {list(db_orders.keys())}")
        
    elif msg.text == "📊 Stats":
        await msg.answer("📈 Sales: ---\nConversion: ---")
        
    elif msg.text == "⚙️ Admin":
        if msg.from_user.id == ADMIN_ID:
            await msg.answer("🛡 Admin panel active.")
        else:
            await msg.answer("🚫 Access denied.")
            
    elif msg.text == "➕ New Order":
        await msg.answer("✍ Enter order details:")
async def main():
    print("-> System online.")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())