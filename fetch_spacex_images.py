import argparse
from pathlib import Path

from functions_upload_images import get_image_extension, saved_image

import requests


def fetch_spacex_images(launch_id):
    spacex_image_path = Path() / 'images' / 'spacex'
    spacexdata_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(spacexdata_url)
    response.raise_for_status()
    launch_image_links = response.json()['links']['flickr']['original']
    for link_number, link in enumerate(launch_image_links):
        image_extension = get_image_extension(link)
        spacex_image_name = f'spacex_{link_number}{image_extension}'
        saved_image(link, spacex_image_path, spacex_image_name)


def main():
    parser = argparse.ArgumentParser(
        description='Загрузит фото от SpaceX по указанному ID запуска.'
    )
    parser.add_argument(
        '-id',
        '--launch_id',
        default='latest',
        help='ID запуска'
    )
    args = parser.parse_args()
    fetch_spacex_images(args.launch_id)


if __name__ == '__main__':
    main()
