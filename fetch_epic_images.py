import argparse
import os

from dotenv import load_dotenv

from functions_upload_image import saved_images

import requests


def fetch_epic_images(nasa_token):
    path_epic_image = 'epic'
    ext_epic_image = '.png'
    url_epic = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {
        'api_key': nasa_token
    }
    response = requests.get(url=url_epic, params=payload)
    response.raise_for_status()
    link_epic_images = response.json()
    for number_epic_image, epic_image in enumerate(link_epic_images):
        date_creat, image_name = epic_image['date'], epic_image['image']
        year_creat, month_creat, day_creat = date_creat.split(' ')[
            0].split('-')
        name_epic_image = f'epic_{number_epic_image}{ext_epic_image}'
        url_epic_enriched = (
            f'https://api.nasa.gov/EPIC/archive/natural/'
            f'{year_creat}/{month_creat}/{day_creat}'
            f'/png/{image_name}{ext_epic_image}'
        )
        saved_images(
            url_epic_enriched,
            path_epic_image,
            name_epic_image,
            nasa_token
        )


def main():
    parser = argparse.ArgumentParser(
        description='Скачивание последних фото планеты от NASA')
    parser.parse_args()
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_epic_images(nasa_token)


if __name__ == '__main__':
    main()
