import argparse
import os
import random
from pathlib import Path

from dotenv import load_dotenv

import functions_posting_telegram as posting_tg


def collect_files_paths(image_size, images_paths):
    collected_file_paths = []
    for image_path in images_paths:
        if os.path.getsize(image_path) < image_size:
            collected_file_paths.append(image_path)
    return collected_file_paths


def check_file_size(image_size, image_path):
    if os.path.getsize(image_path) < image_size:
        image_path_head, image_path_tail = os.path.split(image_path)
        file_path = Path() / f'{image_path_head}' / f'{image_path_tail}'
        return file_path
    else:
        return


def main():
    image_size = 20971520
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    parser = argparse.ArgumentParser(
        description='Отправляет фото в телеграм канал'
    )
    parser.add_argument('-img_path', '--image_path', help='Путь до фото')
    args = parser.parse_args()
    image_path = args.image_path
    if image_path is not None:
        file_path = check_file_size(image_size, image_path)
        if file_path is not None:
            posting_tg.send_photo_to_channel(
                file_path,
                chat_id,
                telegram_token
            )
        elif file_path is None:
            print("Файл слишком большой, выберете другой")
    elif image_path is None:
        images_paths = posting_tg.collect_files_from_folder()
        collected_file_paths = collect_files_paths(image_size, images_paths)
        random_file_to_send = random.choice(collected_file_paths)
        posting_tg.send_photo_to_channel(
            random_file_to_send,
            chat_id,
            telegram_token
        )


if __name__ == '__main__':
    main()
