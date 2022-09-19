import argparse
import os
import random
import time

from dotenv import load_dotenv

from functions_posting_telegram import send_photo_to_channel


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
    print(args.amount_seconds)
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
                for name_image in files:
                    if os.path.getsize(
                            f'{path_image}{name_image}') < image_size:
                        send_photo_to_channel(
                            path_image,
                            name_image,
                            chat_id,
                            telegram_token
                        )
                        time.sleep(args.amount_seconds)
                    else:
                        pass
        random.shuffle(image_paths_names)


if __name__ == '__main__':
    main()
