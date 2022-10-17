import argparse
import os
import random
import time

from dotenv import load_dotenv

import functions_posting_telegram as posting_tg

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
    while True:
        image_paths = posting_tg.collect_files_from_folder()
        random.shuffle(image_paths)
        for image_path in image_paths:
            if os.path.getsize(image_path) < image_size:
                while True:
                    try:
                        posting_tg.send_photo_to_channel(
                            image_path,
                            chat_id,
                            telegram_token
                        )
                    except telegram.error.NetworkError:
                        time.sleep(4)
                        continue
                    break
            time.sleep(float(args.seconds_amount))


if __name__ == '__main__':
    main()
