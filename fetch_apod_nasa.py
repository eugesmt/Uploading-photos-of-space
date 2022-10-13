import argparse
import os
from pathlib import Path

from dotenv import load_dotenv

from functions_upload_images import check_image_extension, saved_image

import requests


def fetch_apod_nasa(nasa_token, amount_images_apod):
    path_spacex_image = Path() / 'images' / 'apod_nasa'
    url_apod_nasa = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_token,
        'count': amount_images_apod
    }
    response = requests.get(url=url_apod_nasa, params=payload)
    response.raise_for_status()
    apod_nasa_response = response.json()
    for image_mumber, content in enumerate(apod_nasa_response):
        media_type = content['media_type']
        if media_type == 'image':
            url_image = content['url']
            extension_image = check_image_extension(url_image)
            if extension_image:
                name_apode_image = f'apod_{image_mumber}{extension_image}'
                params = {
                    'api_key': nasa_token
                    }
                saved_image(
                    url_image,
                    path_spacex_image,
                    name_apode_image,
                    params=params
                )
            else:
                pass
        else:
            pass


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser(
        description='Скачивание красивых снимков от NASA'
    )
    args = parser.add_argument(
        '-amount',
        '--amount_images_apod',
        default=1,
        help='Количество скачиваемых изображений'
    )

    args = parser.parse_args()
    fetch_apod_nasa(nasa_token, args.amount_images_apod)


if __name__ == '__main__':
    main()
