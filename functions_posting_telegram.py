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


def get_files_paths(images_dir):
    files_paths = []
    for root, _, files in os.walk(images_dir):
        for file in files:
            file_path = Path() / root / file
            files_paths.append(file_path)
    return files_paths


def filter_files_size(image_size, images_paths):
    filtered_files_paths = [
        path for path in images_paths if os.path.getsize(path) < image_size
    ]
    return filtered_files_paths
