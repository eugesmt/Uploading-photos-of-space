import argparse
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from functions_upload_images import saved_image

import requests


def fetch_epic_images(nasa_token):
    epic_image_path = Path() / 'images' / 'epic'
    epic_image_ext = '.png'
    epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {
        'api_key': nasa_token
    }
    response = requests.get(url=epic_url, params=payload)
    response.raise_for_status()
    epic_images_link = response.json()
    for epic_image_number, epic_image in enumerate(epic_images_link):
        created_date, image_name = epic_image['date'], epic_image['image']
        parse_date = datetime.fromisoformat(created_date)
        epic_image_name = f'epic_{epic_image_number}{epic_image_ext}'
        enriched_epic_url = (
            f'https://api.nasa.gov/EPIC/archive/natural/'
            f'{parse_date.year}/{parse_date.month}/{parse_date.day}'
            f'/png/{image_name}{epic_image_ext}'
        )
        saved_image(
            enriched_epic_url,
            epic_image_path,
            epic_image_name,
            params=payload
        )


def main():
    parser = argparse.ArgumentParser(
        description='Скачивание последних фото планеты от NASA')
    parser.parse_args()
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    fetch_epic_images(nasa_token)


if __name__ == '__main__':
    main()
