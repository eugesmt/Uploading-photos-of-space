import os.path
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def saved_image(url, image_path, image_name, api_key=None):
    payload = {
        'api_key': api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    try:
        Path(image_path).mkdir(parents=True, exist_ok=False)
        with open(f'{image_path}/{image_name}', 'wb') as file:
            file.write(response.content)
    except FileExistsError:
        if Path(f'{image_path}/{image_name}').is_file():
            pass
        else:
            with open(f'{image_path}/{image_name}', 'wb') as file:
                file.write(response.content)


def check_image_extension(link):
    image_link_path = urlsplit(link).path
    link_replacement_escape = unquote(image_link_path)
    image_path_head, image_path_tail = os.path.split(link_replacement_escape)
    del image_path_head
    image_root, image_ext = os.path.splitext(image_path_tail)
    del image_root
    return image_ext
