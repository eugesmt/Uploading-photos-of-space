import argparse

from functions_upload_image import check_image_extension, saved_images

import requests


def fetch_spacex_last_launch(launch_id=None):
    image_path_spacex = 'spacex'
    if launch_id is None:
        url_spacexdata = 'https://api.spacexdata.com/v5/launches/latest'
        response = requests.get(url_spacexdata)
        response.raise_for_status
    else:
        url_spacexdata = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        response = requests.get(url_spacexdata)
        response.raise_for_status
    launch_image_links = response.json()['links']['flickr']['original']
    for link_mumber, link in enumerate(launch_image_links):
        image_extension = check_image_extension(link)
        image_name_spacex = f'spacex_{link_mumber}{image_extension}'
        saved_images(link, image_path_spacex, image_name_spacex)


def main():
    parser = argparse.ArgumentParser(
        description='Згрузит фото от SpaceX по указанному ID запуска.'
    )
    parser.add_argument('-id', '--launch_id', help='ID запуска')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == '__main__':
    main()
