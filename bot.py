import telebot
import os

TOKEN = "###################"

bot = telebot.TeleBot(TOKEN)

# === /start ===
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name

    text = f"""Привет, {user_name}!

Ты попал в бот по поддержке твоей прекрасной жизни!

Данный бот является независимым и некоммерческим со своей инфраструктурой.

Исходной код на GitHub https://github.com/nanoharon/helper_real_live

Тех поддержка (ещё пока нет)

Бот работает 24/7. В случае если не будет свободного администратора бота, вы будете общаться с ИИ. Когда администратор будет в сети, он продолжит общаться с вами.

Добро пожаловать!

Бот находится в бете."""

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("создатель", url="https://t.me/nanoharon"))
    keyboard.add(telebot.types.InlineKeyboardButton("GitHub", url="https://github.com/nanoharon/helper_real_live"))

    bot.send_message(message.chat.id, text, reply_markup=keyboard)

# === /help ===
@bot.message_handler(commands=['help'])
def help_command(message):
    text = """📖 Помощь и команды

/start — главное меню
/help — этот список
/info — о боте
/profile — твой профиль
/donate — поддержать проект

Спасибо, что пользуетесь ботом! ❤️"""
    bot.send_message(message.chat.id, text)

# === /info ===
@bot.message_handler(commands=['info'])
def info_command(message):
    text = """ℹ️ Информация о боте

Версия: 1.0
Создан: 2026 год
Разработчик: @nanoharon
GitHub: https://github.com/nanoharon/helper_real_live"""
    bot.send_message(message.chat.id, text)

# === /profile ===
@bot.message_handler(commands=['profile'])
def profile_command(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_nick = message.from_user.username or "нет ника"

    text = f"""👤 Профиль

Имя: {user_name}
ID: {user_id}
Ник: @{user_nick}"""
    bot.send_message(message.chat.id, text)

# === /donate ===
@bot.message_handler(commands=['donate'])
def donate_command(message):
    text = """💳 Поддержать проект

Кошелёк (TON):
UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2

Ссылка: https://app.tonkeeper.com/transfer/UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2"""
    bot.send_message(message.chat.id, text)

# === ЗАПУСК ===
print("✅ Бот запущен!")
bot.infinity_polling()