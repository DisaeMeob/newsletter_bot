from aiogram import Bot, Dispatcher, executor, types
import logging
  
from config import TOKEN
from db import create_table, add_user, get_all_users

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

create_table()

ADMIN_ID = 5992332951
admin_kb = types.InlineKeyboardMarkup()
admin_kb.add(
  types.InlineKeyboardButton(text='Рассылка', callback_data='send_message'),
  types.InlineKeyboardButton(text='Статистика бота', callback_data='stats'),
  types.InlineKeyboardButton(text='Выход', callback_data = 'exit')
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
  await message.answer("Привет, вы зарегестрированы в системе")
  user_id = message.from_user.id
  add_user(user_id)

@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
  if message.from_user.id == ADMIN_ID:
    await message.answer("Вы вошли в адми-панель", reply_markup=admin_kb)
  else:
    await message.answer("Вам не доступна эта фонкция")
    return
  
@dp.callback_query_handler(lambda call: call.data == 'exit')
async def exit(call: types.CallbackQuery):
  await call.message.delete()
  await call.message.answer("Вы вышли из админ-панели")

@dp.callback_query_handler(lambda call: call.data == 'send_message')
async def send_message(call: types.CallbackQuery):
  await call.answer()
  if call.from_user.id == ADMIN_ID:
    await call.message.answer("Введите текст сообщения для рассылки")
  else: 
    await call.message.answer("Вам не доступна эта функция")
    return
  
  @dp.message_handler()
  async def send(message: types.Message):
    users = get_all_users()
    success = 0
    fail = 0

    if message.from_user.id == ADMIN_ID:
      try:
        for user in users:
          await bot.send_message(user, message.text)
          success += 1
      except:
        fail += 1
    else:
      return
    
    await message.answer(f"✅ Рассылка завершена \nУспешно: {success}\nНеудачно: {fail}")


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)