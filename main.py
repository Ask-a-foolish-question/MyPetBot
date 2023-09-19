from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

from config import TOKEN
from pet import Pet
from player import Player

import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

pets = {}
players = {}

pet = Pet()
player = Player()

# Define reply keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard.add(KeyboardButton("Feed 🍔"), KeyboardButton("Bath 🛁"))
keyboard.add(KeyboardButton("Play ⚽"), KeyboardButton("Sleep 💤"))
keyboard.add(KeyboardButton("Status 📋"))

# Define confirmation keyboard
confirmation_keyboard = InlineKeyboardMarkup(row_width=2)
confirmation_keyboard.add(InlineKeyboardButton("Yes", callback_data="yes"), InlineKeyboardButton("No", callback_data="no"))

@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    pets[message.from_user.id] = Pet()
    players[message.from_user.id] = Player()
    players[message.from_user.id].start_game()
    players[message.from_user.id].id = message.from_user.id
    await message.reply("Welcome to MyPetBot! Your pet is ready to play!\n\n"
                        "Here are the commands you can use:\n"
                        "Feed 🍔: Feed your pet to reduce its hunger.\n"
                        "Bath 🛁: Give your pet a bath to reduce its dirtiness.\n"
                        "Play ⚽: Play with your pet to reduce its boredom.\n"
                        "Sleep 💤: Make your pet sleep to reduce its sleepiness.\n"
                        "Status 📋: Check the current status of your pets[message.from_user.id].\n\n"
                        "You can use these commands by pressing the buttons below.")
    await bot.send_message(message.from_user.id, "What would you like to name your pet?")

@dp.message_handler(lambda message: players[message.from_user.id].game_started and not pets[message.from_user.id].name)
async def get_pet_name(message: types.Message):
    pets[message.from_user.id].name = message.text
    await bot.send_message(message.from_user.id, f"Your pet's name is {pets[message.from_user.id].name}. Are you sure?", reply_markup=confirmation_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'yes')
async def confirm_pet_name(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Great! You can now start taking care of {pets[callback_query.from_user.id].name}.", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'no')
async def reject_pet_name(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Okay, let's try again. What would you like to name your pet?")

@dp.message_handler(lambda message: message.text.lower() == 'feed 🍔')
async def feed_pet(message: types.Message):
    pets[message.from_user.id].feed()
    await bot.send_message(message.from_user.id, f"You fed {pets[message.from_user.id].name}. It's happy! 😊")

@dp.message_handler(lambda message: message.text.lower() == 'bath 🛁')
async def bath_pet(message: types.Message):
    pets[message.from_user.id].bath()
    await bot.send_message(message.from_user.id, f"You gave {pets[message.from_user.id].name} a bath. It's clean now! 🧼")

@dp.message_handler(lambda message: message.text.lower() == 'play ⚽')
async def play_with_pet(message: types.Message):
    pets[message.from_user.id].play()
    await bot.send_message(message.from_user.id, f"You played with {pets[message.from_user.id].name}. It's energy is up! ⚡")

@dp.message_handler(lambda message: message.text.lower() == 'sleep 💤')
async def make_pet_sleep(message: types.Message):
    pets[message.from_user.id].sleep()
    await bot.send_message(message.from_user.id, f"{pets[message.from_user.id].name} is sleeping. It's regaining energy! 🌙")

@dp.message_handler(lambda message: message.text.lower() == 'status 📋')
async def check_pet_status(message: types.Message):
    status = pets[message.from_user.id].status()
    await bot.send_message(message.from_user.id, f"{pets[message.from_user.id].name}'s status:\n{status}")

async def send_notifications():
    print("Starting notifications...")
    while True:
        await asyncio.sleep(1800)
        for user_id, player in players.items():
            if pets[user_id].is_alive() and player.game_started:
                print("Sending notifications...")
                status = pets[user_id].status()
                await bot.send_message(user_id, f"{pets[user_id].name}'s status:\n{status}")
            else:
                await bot.send_message(user_id, f"{pets[user_id].name} has died. 😢 Use /start to restart the game.")

async def on_startup(dp):
    loop = asyncio.get_event_loop()
    loop.create_task(send_notifications())

async def on_shutdown(dp):
    await bot.send_message(player.id, "Bot has been stopped")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
