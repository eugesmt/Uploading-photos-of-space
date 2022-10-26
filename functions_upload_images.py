import os.path
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def saved_image(url, image_path, image_name, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    Path(image_path).mkdir(parents=True, exist_ok=True)
    file_path = Path() / image_path / image_name
    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_image_extension(link):
    image_link_path = urlsplit(link).path
    replacement_escape_link = unquote(image_link_path)
    _, image_path_tail = os.path.split(replacement_escape_link)
    _, image_ext = os.path.splitext(image_path_tail)
    return image_ext
