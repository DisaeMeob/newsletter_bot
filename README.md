# 📢 Telegram Newsletter Bot

Простой и эффективный Telegram-бот для рассылок, созданный с использованием Python и библиотеки Aiogram 2.x. Поддерживает регистрацию пользователей, админ-панель и отправку сообщений всем подписчикам через SQLite-базу данных.

## 🚀 Возможности

- 📩 Массовая рассылка сообщений по базе пользователей
- 👤 Автоматическая регистрация пользователей при старте
- 🛠 Простая админ-панель через кнопки
- 💾 Хранение пользователей в SQLite
- 🔒 Ограничение доступа к админ-функциям по `ADMIN_ID`

## ⚙️ Установка и запуск

1. Установи зависимости:
   ```bash
   pip install aiogram
Создай файл config.py и добавь туда:

python
Копировать
Редактировать
TOKEN = "Твой токен от BotFather"
ADMIN_ID = твой_telegram_id
Запусти бота:

bash
Копировать
Редактировать
python main.py
🛠 Стек технологий
Python 3.10+

Aiogram 2.25.1

SQLite

Git / GitHub

📂 Структура проекта
bash
Копировать
Редактировать
newsletter_bot/
├── main.py         # Основная логика бота
├── db.py           # Работа с базой данных
├── config.py       # Конфигурация (в .gitignore)
├── .gitignore      # Игнорируемые файлы
└── README.md       # Описание проекта
📬 Автор
Telegram: @feaagff
GitHub: https://github.com/DisaeMeob

