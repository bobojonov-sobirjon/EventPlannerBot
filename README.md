# Event Planner Telegram Bot

Telegram-бот на Python (aiogram 3). При нажатии **Старт** или команды `/start` отправляет статичное приветственное сообщение со ссылкой.

## Тексты

- **Описание бота** (видно при открытии чата):  
  «Создавайте планы, приглашайте друзей и встречайтесь. Нажмите Открыть внизу слева.»

- **Ответ на /start**:  
  Создавайте планы, приглашайте друзей и встречайтесь.  
  Для начала нажмите «Открыть» внизу слева или ссылку t.me/planvmeste_bot/direclink

---

## Требования

- Python 3.10+
- Токен бота от [@BotFather](https://t.me/BotFather)

---

## Установка и запуск локально

### 1. Клонировать или скопировать проект

```bash
cd D:\Projects\Bots\EventPlanerBot
```

### 2. Создать виртуальное окружение (рекомендуется)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Настроить токен

Скопировать пример конфига и подставить свой токен:

```bash
copy .env.example .env
```

Открыть `.env` и заменить `your_bot_token_here` на токен от BotFather:

```
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 5. Запустить бота

```bash
python bot.py
```

В консоли должно появиться: `Бот запущен.` — после этого бот отвечает на `/start`.

---

## Запуск на сервере (Linux)

### Вариант 1: screen (простой способ)

```bash
cd /path/to/EventPlanerBot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env   # вставить BOT_TOKEN

screen -S eventbot
python bot.py
# Отключиться: Ctrl+A, затем D
# Подключиться снова: screen -r eventbot
```

### Вариант 2: systemd (автозапуск при перезагрузке)

1. Создать unit-файл:

```bash
sudo nano /etc/systemd/system/eventplaner-bot.service
```

2. Вставить (подставьте свой путь и пользователя):

```ini
[Unit]
Description=Event Planner Telegram Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/EventPlanerBot
ExecStart=/home/ubuntu/EventPlanerBot/venv/bin/python bot.py
Restart=always
RestartSec=10
Environment=PATH=/home/ubuntu/EventPlanerBot/venv/bin

[Install]
WantedBy=multi-user.target
```

3. Включить и запустить:

```bash
sudo systemctl daemon-reload
sudo systemctl enable eventplaner-bot
sudo systemctl start eventplaner-bot
sudo systemctl status eventplaner-bot
```

Логи:
```bash
journalctl -u eventplaner-bot -f
```

---

## Структура проекта

```
EventPlanerBot/
├── bot.py           # основной код бота
├── requirements.txt
├── .env.example     # пример .env (скопировать в .env)
├── .env             # ваш токен (не коммитить!)
├── .gitignore
└── README.md
```

---

## Изменение текстов

Тексты заданы в `bot.py`:

- `START_DESCRIPTION` — описание бота при открытии чата.
- `START_REPLY` — ответ на команду `/start`.

После правок перезапустите бота (при использовании systemd: `sudo systemctl restart eventplaner-bot`).
