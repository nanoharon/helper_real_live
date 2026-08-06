
код буду добавлять по мере обновления тоесь тут обновление кода будет не сразу 


import telebot
from telebot import types
import random
import datetime

BOT_TOKEN = "а зачем он тебе?"
bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_ID = 1882231668  
GROUP_ID = -1003941453582

@bot.message_handler(commands=['start'])
def start_command(message):
    user_name = message.from_user.first_name
    text = f"""♥️ Привет, {user_name} ♥️!

Ты попал в бот по поддержке твоей прекрасной жизни!

Данный бот является независимым и некоммерческим со своей инфраструктурой.

канал бота: https://t.me/helper_live_channel

канал создателя: https://t.me/nanoharon_tgk

Исходный код на GitHub https://github.com/nanoharon/helper_real_live

Тех поддержка @suppoorthelper_real_live_bot

Бот работает 24/7.

Добро пожаловать!

Бот находится в бете могут быть ошибки:(

команды:
/start — перезапуск/запуск
/help — помощь
/info — информация о боте
/profile — твой профиль
/donate — поддержать проект)
/quote — цитата...
/joke — шутка:)
/ping — проверка
/feedback — отзыв
/rules — правила
/privacy — политика
/status — статус
/wikipedia — Википедия
/stats — статистика

в скором времени появится:
красивое оформление
больше любви
больше инлайн кнопок (автомизация)"""

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("👤 создатель проекта", url="https://t.me/nanoharon"))
    kb.add(types.InlineKeyboardButton("📦 исходный код GitHub", url="https://github.com/nanoharon/helper_real_live"))
    kb.add(types.InlineKeyboardButton("💳 Поддержать проект (TON)", url="https://app.tonkeeper.com/transfer/UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2"))
    kb.add(types.InlineKeyboardButton("📝 Обратная связь", callback_data="feedback"))
    kb.add(types.InlineKeyboardButton("🔒 Политика конфиденциальности", callback_data="privacy"))

    bot.send_message(message.chat.id, text, reply_markup=kb)

@bot.message_handler(commands=['help'])
def help_command(message):
    text = """📖 Помощь и команды

🤖 Основные команды:
/start — главное меню и приветствие
/help — этот список команд
/info — информация о боте
/profile — твой профиль
/donate — поддержать проект
/quote — цитата
/joke — шутка
/time — время
/ping — проверка
/feedback — отзыв
/rules — правила
/privacy — политика
/status — статус
/wikipedia — Википедия
/stats — статистика

ℹ️ О системе бота:
 os: arch linux
 memory: 16
 GPU: zeon v3

🔗 Полезные ссылки:
• Создатель: @nanoharon
• GitHub: https://github.com/nanoharon/helper_real_live
• Поддержать: /donate
 поддержка: @suppoorthelper_real_live_bot
 
💙 Спасибо, что пользуетесь ботом! ❤️"""

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("👤 Создатель", url="https://t.me/nanoharon"))
    kb.add(types.InlineKeyboardButton("📦 GitHub", url="https://github.com/nanoharon/helper_real_live"))
    kb.add(types.InlineKeyboardButton("💳 Поддержать", url="https://app.tonkeeper.com/transfer/UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2"))

    bot.send_message(message.chat.id, text, reply_markup=kb)

@bot.message_handler(commands=['info'])
def info_command(message):
    text = """ℹ️ Информация о боте

🤖 Название: helper_real_live
📅 Версия: 1.0 (бета)
📆 запущен впервые 6 августа 2026г.
👨‍💻 Разработчик: @nanoharon

🔗 Исходный код: https://github.com/nanoharon/helper_real_live

⚡ Статус: Работает 24/7
💡 Лицензия: Некоммерческий проект

💬 Тех поддержка: @suppoorthelper_real_live_bot

Спасибо, что пользуетесь ботом! ❤️"""

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['profile'])
def profile_command(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_nick = message.from_user.username or "нет ника"

    text = f"""👤 Ваш профиль

📛 Имя: {user_name}
🆔 ID: {user_id}
🔗 Ник: @{user_nick}

Спасибо, что с нами! ❤️"""

    bot.send_message(message.chat.id, text)
    
@bot.message_handler(commands=['donate'])
def donate_command(message):
    text = """💳 Поддержать проект

Вы можете поддержать развитие бота и проекта.

📌 Кошелёк (TON):
`UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2`

📲 Как перевести:
1. Откройте приложение Tonkeeper
2. Нажмите "Отправить"
3. Вставьте адрес выше
4. Укажите сумму и отправьте

🔗 Ссылка для перевода:
https://app.tonkeeper.com/transfer/UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2

💙 Спасибо за поддержку! ❤️"""

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("💳 Открыть Tonkeeper", url="https://app.tonkeeper.com/transfer/UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2"))

    bot.send_message(message.chat.id, text, reply_markup=kb)

@bot.message_handler(commands=['quote'])
def quote_command(message):
    quotes = [
        "Жизнь — это то, что с тобой происходит, пока ты строишь планы.",
        "Будь изменением, которое хочешь видеть в мире.",
        "Успех — это способность идти от неудачи к неудаче, не теряя энтузиазма.",
        "Счастье не в деньгах, а в их количестве.",
        "Лучший способ предсказать будущее — создать его.",
        "Не бойся медленного движения, бойся стоять на месте.",
        "Ты получаешь то, что даёшь.",
        "Важно не количество дней в жизни, а жизнь в этих днях.",
        "Сделай сегодня то, что другие не хотят — завтра будешь жить так, как другие не могут.",
        "Смысл жизни в том, чтобы найти свой дар. Цель жизни — подарить его.",
        "Жизнь — это не ожидание, а приключение.",
        "Чем сложнее победа, тем больше счастья от неё.",
        "Путь в тысячу миль начинается с одного шага.",
        "Вдохновение приходит только во время работы.",
        "Если хочешь добиться цели, не бойся менять путь."
    ]
    
    text = random.choice(quotes)
    bot.send_message(message.chat.id, f"💬 {text}")

@bot.message_handler(commands=['joke'])
def joke_command(message):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что 31 окт = 25 дек.",
        "Как назвать бота, который всегда врёт? Лже-бот.",
        "Сколько программистов нужно, чтобы заменить лампочку? Ни одного — это аппаратная проблема.",
        "Что сказал один бит другому? Мне тебя не хватает.",
        "Почему у программистов вечно мерзнут ноги? Потому что они постоянно ищут баги.",
        "Бесплатный Wi-Fi — это как бесплатный сыр, только в мышеловке.",
        "Я не ленивый, я энергоэффективный.",
        "Лучший способ отдохнуть — поспать на работе.",
        "Что общего между программистом и зомби? И те, и другие боятся крестов (crosses).",
        "Вчера я написал код, который работал. Сегодня я его переписал. Теперь он работает красивее.",
        "Программист просыпается — 404, сон не найден.",
        "Чем отличается программист от обычного человека? Обычный человек думает, что если что-то работает, не надо это трогать."
    ]
    
    text = random.choice(jokes)
    bot.send_message(message.chat.id, f"😂 {text}")

@bot.message_handler(commands=['time'])
def time_command(message):
    now = datetime.datetime.now()
    text = f"🕐 Текущее время:\n\n{now.strftime('%d.%m.%Y %H:%M:%S')}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['ping'])
def ping_command(message):
    bot.send_message(message.chat.id, "🏓 Понг! Бот работает!")

@bot.message_handler(commands=['feedback'])
def feedback_command(message):
    uid = message.from_user.id
    uname = message.from_user.first_name
    txt = message.text.replace("/feedback", "").strip()
    
    if txt:
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("✏️ Ответить", callback_data=f"reply_{uid}"))
        bot.send_message(GROUP_ID, f"📝 Отзыв от {uname} (ID: {uid}):\n\n{txt}", reply_markup=kb)
        bot.send_message(message.chat.id, "✅ Спасибо за отзыв! Он передан администратору.")
    else:
        bot.send_message(message.chat.id, "❌ Напиши текст отзыва после команды.\n\nПример: /feedback Бот отличный!")

@bot.message_handler(commands=['rules'])
def rules_command(message):
    text = """📜 **Правила проекта**

1️⃣ Бот создан для поддержки пользователей.
2️⃣ Запрещён спам и оскорбления.
3️⃣ Администратор всегда на связи. (ну если не спят все:)
4️⃣ Бот работает 24/7.
5️⃣ Все отзывы и предложения приветствуются!

💙 Спасибо, что вы с нами!"""
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['status'])
def status_command(message):
    text = """⚡ **Статус бота**

✅ Бот работает
✅ Подключение к Telegram: есть
⏰ Время работы: 24/7

Всё отлично! 🚀"""
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['privacy'])
def privacy_command(message):
    text = """🔒 **Политика конфиденциальности**

1. Какие данные мы собираем
• Ваш ID в Telegram
• Ваше имя и никнейм
• Текст сообщений, отправленных боту

2. Как мы используем данные
• Для обработки ваших запросов
• Для связи с вами (ответы администратора)
• Для улучшения работы бота

3. Передача данных третьим лицам
• Мы НЕ передаём ваши данные третьим лицам
• Данные хранятся только в Telegram

4. Хранение данных
• Данные хранятся до тех пор, пока вы пользуетесь ботом
• Вы можете удалить все данные, написав администратору

5. Ваши права
• Вы можете запросить удаление всех данных
• Вы можете отказаться от использования бота в любой момент

6. Контакты
 создатель: @nanoharon
поддержка: @suppoorthelper_real_live_bot
• GitHub: https://github.com/nanoharon/helper_real_live

💙 Используя бота, вы соглашаетесь с данной политикой."""
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['wikipedia'])
def wikipedia_command(message):
    q = message.text.replace("/wikipedia", "").strip()
    
    if q:
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(f"📖 Открыть Википедию: {q}", url=f"https://ru.wikipedia.org/wiki/{q}"))
        bot.send_message(message.chat.id, f"🔍 Ищем в Википедии: {q}", reply_markup=kb)
    else:
        bot.send_message(message.chat.id, "❌ Что ищем? /wikipedia Python")

@bot.message_handler(commands=['stats'])
def stats_command(message):
    text = """📊 **Статистика бота**

🤖 Название: helper_real_live
📅 Версия: 1.0
📋 Команд: 15
⚡ Статус: Работает 24/7

⏰ Время работы: с 2026 года
💙 Создатель: @nanoharon

📌 Список команд:
/start — главное меню
/help — помощь
/info — о боте
/profile — профиль
/donate — поддержать
/quote — цитата
/joke — шутка
/ping — проверка
/feedback — отзыв
/rules — правила
/privacy — политика
/wikipedia — Википедия

💙 Спасибо, что пользуетесь ботом!"""
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['reply'])
def reply_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "❌ ты не админ-_-")
        return
    
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        bot.send_message(message.chat.id, "❌ Использование: /reply ID_пользователя Текст")
        return
    
    try:
        target_id = int(parts[1])
    except:
        bot.send_message(message.chat.id, "❌ ID должен быть числом!")
        return
    
    reply_text = parts[2]
    bot.send_message(target_id, f"🤖 Администратор:\n\n{reply_text}")
    bot.send_message(message.chat.id, f"✅ Ответ отправлен пользователю {target_id}")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    data = call.data
    
    if data == "feedback":
        bot.send_message(call.message.chat.id, "📝 Напиши свой отзыв командой:\n\n/feedback Твой текст здесь")
    
    elif data == "privacy":
        text = """🔒 **Политика конфиденциальности**

1. Какие данные мы собираем
• Ваш ID в Telegram
• Ваше имя и никнейм
• Текст сообщений, отправленных боту

2. Как мы используем данные
• Для обработки ваших запросов
• Для связи с вами (ответы администратора)
• Для улучшения работы бота

3. Передача данных третьим лицам
• Мы НЕ передаём ваши данные третьим лицам
• Данные хранятся только в Telegram

4. Хранение данных
• Данные хранятся до тех пор, пока вы пользуетесь ботом
• Вы можете удалить все данные, написав администратору

5. Ваши права
• Вы можете запросить удаление всех данных
• Вы можете отказаться от использования бота в любой момент

6. Контакты
• По всем вопросам: @nanoharon
• GitHub: https://github.com/nanoharon/helper_real_live

💙 Используя бота, вы соглашаетесь с данной политикой."""
        
        bot.send_message(call.message.chat.id, text)
    
    elif data == "donate":
        text = """💳 Поддержать проект

📌 Кошелёк (TON):
`UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2`

🔗 Ссылка:
https://app.tonkeeper.com/transfer/UQBb1QOkN9HxwInFOJv1XRimVB-9ZmCA4uQmmFZpzTM6Apl2"""
        
        bot.send_message(call.message.chat.id, text)
    
    elif data.startswith("reply_"):
        target_uid = data.replace("reply_", "")
        bot.send_message(call.message.chat.id, f"📝 Чтобы ответить пользователю, напиши в группе:\n\n/reply {target_uid} Текст ответа")
    
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda m: True)
def forward_to_group(message):
    if message.chat.id == GROUP_ID:
        return

    if message.text and message.text.startswith('/'):
        return
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    text = message.text or "Сообщение без текста"
    
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("✏️ Ответить", callback_data=f"reply_{user_id}"))
