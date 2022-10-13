import argparse
import os
import random
import time
from pathlib import Path


from dotenv import load_dotenv

from functions_posting_telegram import send_photo_to_channel

import telegram


def main():
    image_size = 20971520
    parser = argparse.ArgumentParser(
        description='Программа публикует все фото'
        'из директории в бесконечном цикле'
    )
    parser.add_argument(
        '-second',
        '--amount_seconds',
        default=14400,
        help='Количество секунд'
    )
    args = parser.parse_args()
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    image_paths_names = []
    for element in os.walk('images'):
        image_paths_names.append(element)
    while True:
        for element in image_paths_names:
            path_image, direct, files = element
            del direct
            if len(files) > 0:
                random.shuffle(files)
                for name_image in files:
                    file_path = Path() / f'{path_image}' / f'{name_image}'
                    if os.path.getsize(file_path) < image_size:
                        while True:
                            try:
                                send_photo_to_channel(
                                    path_image,
                                    name_image,
                                    chat_id,
                                    telegram_token
                                )
                            except telegram.error.NetworkError:
                                time.sleep(2)

                                continue
                            break
                    time.sleep(float(args.amount_seconds))


if __name__ == '__main__':
    main()
