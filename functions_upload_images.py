import os.path
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def saved_image(url, image_path, image_name, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    Path(image_path).mkdir(parents=True, exist_ok=True)
    file_path = Path() / f'{image_path}' / f'{image_name}'
    with open(file_path, 'wb') as file:
        file.write(response.content)


def check_image_extension(link):
    image_link_path = urlsplit(link).path
    link_replacement_escape = unquote(image_link_path)
    image_path_head, image_path_tail = os.path.split(link_replacement_escape)
    del image_path_head
    image_root, image_ext = os.path.splitext(image_path_tail)
    del image_root
    return image_ext
