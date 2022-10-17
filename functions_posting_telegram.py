import os
from pathlib import Path

import telegram


def send_photo_to_channel(image_path, chat_id, telegram_token):
    bot = telegram.Bot(telegram_token)
    with open(image_path, 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo
        )


def collect_files_from_folder():
    image_paths_names = []
    files_paths = []
    for element in os.walk('images'):
        image_paths_names.append(element)
    for element in image_paths_names:
        image_path, _, files = element
        for file in files:
            file_path = Path() / f'{image_path}' / f'{file}'
            files_paths.append(file_path)
    return files_paths
