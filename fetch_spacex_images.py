import argparse

from functions_upload_images import check_image_extension, saved_image

import requests


def fetch_spacex_images(launch_id):
    image_path_spacex = 'images/spacex'
    url_spacexdata = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url_spacexdata)
    response.raise_for_status()
    launch_image_links = response.json()['links']['flickr']['original']
    for link_mumber, link in enumerate(launch_image_links):
        image_extension = check_image_extension(link)
        image_name_spacex = f'spacex_{link_mumber}{image_extension}'
        saved_image(link, image_path_spacex, image_name_spacex)


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
