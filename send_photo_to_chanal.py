import os

from dotenv import load_dotenv

import telegram


def main():
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(telegram_token)
    bot.send_photo(
        chat_id=chat_id,
        photo=open('apod_nasa/apod_0.jpg', 'rb')
    )


if __name__ == '__main__':
    main()
