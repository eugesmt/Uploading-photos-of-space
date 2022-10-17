import argparse
import os
from pathlib import Path

from dotenv import load_dotenv

from functions_upload_images import check_image_extension, saved_image

import requests


def fetch_apod_nasa(nasa_token, images_apod_amount):
    apod_nasa_image_path = Path() / 'images' / 'apod_nasa'
    apod_nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_token,
        'count': images_apod_amount
    }
    response = requests.get(url=apod_nasa_url, params=payload)
    response.raise_for_status()
    apod_nasa_response = response.json()
    for image_number, content in enumerate(apod_nasa_response):
        media_type = content['media_type']
        if media_type == 'image':
            image_url = content['url']
            image_extension = check_image_extension(image_url)
            if image_extension:
                apode_image_name = f'apod_{image_number}{image_extension}'
                params = {
                    'api_key': nasa_token
                    }
                saved_image(
                    image_url,
                    apod_nasa_image_path,
                    apode_image_name,
                    params=params
                )


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser(
        description='Скачивание красивых снимков от NASA'
    )
    args = parser.add_argument(
        '-amount',
        '--images_apod_amount',
        default=1,
        help='Количество скачиваемых изображений'
    )

    args = parser.parse_args()
    fetch_apod_nasa(nasa_token, args.images_apod_amount)


if __name__ == '__main__':
    main()
