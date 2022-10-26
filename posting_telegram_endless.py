import argparse
import os
import random
import time

from dotenv import load_dotenv

import functions_posting_telegram as posting_tg

import telegram


def posting_images_to_telegram(tg_token, chat_id, seconds, size):
    while True:
        image_paths = posting_tg.get_files_paths()
        random.shuffle(image_paths)
        filtered_file_paths = posting_tg.filter_files_size(size, image_paths)
        for file_path in filtered_file_paths:
            while True:
                try:
                    posting_tg.send_photo_to_channel(
                        file_path,
                        chat_id,
                        tg_token
                    )
                except telegram.error.NetworkError:
                    time.sleep(4)
                    continue
                break
            time.sleep(float(seconds))


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
    posting_images_to_telegram(
        telegram_token,
        chat_id,
        args.seconds_amount,
        image_size
    )


if __name__ == '__main__':
    main()
