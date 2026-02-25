"""
Event Planner Telegram Bot.
При /start выводит приветственное сообщение со ссылкой.
"""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message, MenuButtonWebApp, WebAppInfo
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не задан. Создайте файл .env и укажите BOT_TOKEN.")

# Текст, который показывается в описании бота (под кнопкой «Старт»)
START_DESCRIPTION = (
    "Создавайте планы, приглашайте друзей и встречайтесь"
)

# Ответ при нажатии /start или кнопки «Старт»
START_REPLY = (
    "Создавайте планы, приглашайте друзей и встречайтесь.\n\n"
    "Для начала нажмите «Открыть» внизу слева или ссылку t.me/planvmeste_bot/direclink"
)

# Текст на кнопке меню (слева внизу). Telegram ограничивает до 64 символов.
MENU_BUTTON_TEXT = "Создавайте планы. Нажмите Открыть внизу слева."
MINI_APP_URL = "https://t.me/planvmeste_bot/direclink"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
@dp.message(F.text == "/start")
async def cmd_start(message: Message) -> None:
    """Обработка /start — отправляем статичный текст."""
    try:
        await message.answer(START_REPLY)
    except (TelegramForbiddenError, TelegramBadRequest) as e:
        # Пользователь заблокировал бота или чат удалён — просто игнорируем
        logger.debug("Не удалось отправить сообщение (чат недоступен): %s", e)


async def set_bot_description(bot: Bot) -> None:
    """Устанавливаем описание бота (видно при открытии чата)."""
    try:
        await bot.set_my_description(START_DESCRIPTION)
        logger.info("Описание бота обновлено.")
    except Exception as e:
        logger.warning("Не удалось установить описание бота: %s", e)


async def set_menu_button(bot: Bot) -> None:
    """Меняем текст кнопки меню (Открыть) внизу слева на нужный."""
    try:
        current = await bot.get_chat_menu_button()
        if hasattr(current, "web_app") and current.web_app:
            web_app = current.web_app
        else:
            web_app = WebAppInfo(url=MINI_APP_URL)
        await bot.set_chat_menu_button(
            menu_button=MenuButtonWebApp(text=MENU_BUTTON_TEXT, web_app=web_app)
        )
        logger.info("Текст кнопки меню обновлён: %s", MENU_BUTTON_TEXT)
    except Exception as e:
        logger.warning("Не удалось установить кнопку меню: %s", e)


async def main() -> None:
    await set_bot_description(bot)
    await set_menu_button(bot)
    logger.info("Бот запущен.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
