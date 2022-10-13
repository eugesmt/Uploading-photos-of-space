from pathlib import Path

import telegram


def send_photo_to_channel(image_path, image_name, chat_id, telegram_token):
    bot = telegram.Bot(telegram_token)
    with open(Path() / f'{image_path}' / f'{image_name}', 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo
        )
