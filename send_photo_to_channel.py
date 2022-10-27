import argparse
import os
import random
from pathlib import Path

from dotenv import load_dotenv

import functions_posting_telegram as posting_tg


def main():
    image_size = 20971520
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    parser = argparse.ArgumentParser(
        description='Отправляет фото в телеграм канал'
    )
    parser.add_argument('-img_path', '--image_path', help='Путь до фото')
    parser.add_argument(
        '-dir',
        '--images_dir',
        help='Директория изображений'
    )
    args = parser.parse_args()
    image_path = args.image_path
    images_dir = args.images_dir
    if image_path is not None:
        if os.path.getsize(image_path) < image_size:
            image_path_head, image_path_tail = os.path.split(image_path)
            file_path = Path() / image_path_head / image_path_tail
            posting_tg.send_photo_to_channel(
                file_path,
                chat_id,
                telegram_token
            )
        else:
            print("Файл слишком большой, выберете другой")
    elif image_path is None:
        if images_dir is None:
            images_dir = os.environ['IMAGES_DIR']
        images_paths = posting_tg.get_files_paths(images_dir)
        filtered_files_size = posting_tg.filter_files_size(
            image_size, images_paths
        )
        random_file_to_send = random.choice(filtered_files_size)
        posting_tg.send_photo_to_channel(
            random_file_to_send,
            chat_id,
            telegram_token
        )


if __name__ == '__main__':
    main()
