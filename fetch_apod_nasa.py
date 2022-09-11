import argparse
import os

from dotenv import load_dotenv

from functions_upload_images import check_image_extension, saved_image

import requests


def fetch_apod_nasa(nasa_token, amount_images_apod=None):
    path_spacex_image = 'images/apod_nasa'
    url_apod_nasa = 'https://api.nasa.gov/planetary/apod'
    if amount_images_apod is None:
        amount_images_apod = 1
    payload = {
        'api_key': nasa_token,
        'count': amount_images_apod
    }
    response = requests.get(url=url_apod_nasa, params=payload)
    response.raise_for_status()
    links_images_apod = response.json()
    for link_mumber, link in enumerate(links_images_apod):
        url_image = link['url']
        extension_image = check_image_extension(url_image)
        if extension_image:
            name_apode_image = f'apod_{link_mumber}{extension_image}'
            saved_image(url_image, path_spacex_image, name_apode_image)
        else:
            pass


def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    parser = argparse.ArgumentParser(
        description='Скачивание красивых снимков от NASA'
    )
    args = parser.add_argument(
        '-amount',
        '--amount_images_apod',
        help='Количество скачиваемых изображений'
    )

    args = parser.parse_args()
    try:
        fetch_apod_nasa(nasa_token, args.amount_images_apod)
    except KeyError:
        pass


if __name__ == '__main__':
    main()
