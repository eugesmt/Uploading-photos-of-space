import os

from dotenv import load_dotenv

import telegram


def main():
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    chat_id = '@BeautifulSpacePhotos'
    text_to_bot = "Классный канал!!!"
    bot = telegram.Bot(telegram_token)
    bot.send_message(
        chat_id=chat_id,
        text=text_to_bot
    )


if __name__ == '__main__':
    main()
