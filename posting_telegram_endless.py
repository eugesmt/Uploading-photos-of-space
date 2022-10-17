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
        '--seconds_amount',
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
            image_path, direct, files = element
            del direct
            if len(files) > 0:
                random.shuffle(files)
                for image_name in files:
                    file_path = Path() / f'{image_path}' / f'{image_name}'
                    if os.path.getsize(file_path) < image_size:
                        while True:
                            try:
                                send_photo_to_channel(
                                    image_path,
                                    image_name,
                                    chat_id,
                                    telegram_token
                                )
                            except telegram.error.NetworkError:
                                time.sleep(2)

                                continue
                            break
                    time.sleep(float(args.seconds_amount))


if __name__ == '__main__':
    main()
