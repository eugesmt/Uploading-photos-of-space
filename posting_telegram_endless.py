import argparse
import os
import random
import time

from dotenv import load_dotenv

from fetch_apod_nasa import fetch_apod_nasa

from fetch_epic_images import fetch_epic_images

from fetch_spacex_images import fetch_spacex_images

from functions_posting_telegram import send_photo_to_channel


def main():
    image_size = 20971520
    parser = argparse.ArgumentParser(
        description='Программа публикует все фото'
        'из директории в бесконечном цикле'
    )
    parser.add_argument('-second', '--amount_seconds',
                        help='Количество секунд')
    args = parser.parse_args()
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_apod_nasa(nasa_token)
    fetch_spacex_images()
    fetch_epic_images(nasa_token)
    image_paths_names = []
    for element in os.walk('images'):
        image_paths_names.append(element)
    while True:
        for element in image_paths_names:
            path_image, direct, files = element
            del direct
            if len(files) > 0:
                for name_image in files:
                    if args.amount_seconds is not None:
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
                    else:
                        if os.path.getsize(
                                f'{path_image}{name_image}') < image_size:
                            send_photo_to_channel(
                                path_image,
                                name_image,
                                chat_id,
                                telegram_token
                            )
                            time.sleep(14400)
                        else:
                            pass
        random.shuffle(image_paths_names)


if __name__ == '__main__':
    main()
